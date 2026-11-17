import math
import uuid
from typing import Dict, Any, List
from .database import get_db

GROUND_TRUTH_BENCHMARKS = {
    'ahpi_2024_knee_pricing': {
        'datasetName': 'Association of Healthcare Providers India (AHPI) 2024',
        'metric': 'Mean Inpatient Knee Arthroplasty Package',
        'benchmarkValue': 340000.0,
        'unit': 'INR',
        'tolerancePct': 5.0
    },
    'cghs_tier1_surgical_cap': {
        'datasetName': 'Central Government Health Scheme (CGHS) Tier-1 Ceiling',
        'metric': 'Bundled Knee Replacement Mandate',
        'benchmarkValue': 275000.0,
        'unit': 'INR',
        'tolerancePct': 5.0
    },
    'irdai_claim_deduction_baseline': {
        'datasetName': 'IRDAI Annual Claim Settlement Survey 2024',
        'metric': 'Disallowed Consumables Out-Of-Pocket Ratio',
        'benchmarkValue': 24.1,
        'unit': 'percent',
        'tolerancePct': 2.0
    }
}

class BenchmarkEvaluationEngine:
    @staticmethod
    def evaluate_experiment(experiment_id: str, dataset_key: str, simulated_value: float) -> Dict[str, Any]:
        if dataset_key not in GROUND_TRUTH_BENCHMARKS:
            raise ValueError(f'Unknown benchmark dataset: {dataset_key}')

        bm = GROUND_TRUTH_BENCHMARKS[dataset_key]
        benchmark_val = bm['benchmarkValue']
        mae = abs(simulated_value - benchmark_val)
        delta_pct = round(((simulated_value - benchmark_val) / benchmark_val) * 100, 2)
        within_tolerance = abs(delta_pct) <= bm['tolerancePct']
        verdict = 'CALIBRATED_WITHIN_TOLERANCE' if within_tolerance else 'EMPIRICAL_VARIANCE_EXCEEDED'

        eval_id = f'eval-{uuid.uuid4().hex[:8]}'
        with get_db() as db:
            db.execute(
                '''INSERT INTO benchmark_evaluations
                   (id, experiment_id, dataset_name, target_metric, simulated_value, benchmark_value, error_mae, error_delta_percent, verdict)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                (eval_id, experiment_id, bm['datasetName'], bm['metric'], simulated_value, benchmark_val, mae, delta_pct, verdict)
            )

        return {
            'evaluationId': eval_id,
            'experimentId': experiment_id,
            'datasetName': bm['datasetName'],
            'targetMetric': bm['metric'],
            'simulatedValue': simulated_value,
            'benchmarkValue': benchmark_val,
            'unit': bm['unit'],
            'meanAbsoluteError': round(mae, 2),
            'percentageDelta': delta_pct,
            'toleranceLimitPct': bm['tolerancePct'],
            'calibrationVerdict': verdict
        }

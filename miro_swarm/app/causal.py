from typing import Dict, Any, List

class CausalCascadeEngine:
    @staticmethod
    def calculate_cascade(intervention_type: str, base_procedure_cost: float = 250000.0) -> Dict[str, Any]:
        """
        Calculates deterministic propagation of healthcare policy interventions across 
        connected enterprise variables (Hospital Margin, Out-Of-Pocket Shock, TPA Deductions).
        """
        if intervention_type == 'price_cap':
            consumable_markup = 0.0
            tpa_deduction_rate = 0.065
            avg_bill = base_procedure_cost * 1.05
            oop_shock = avg_bill * tpa_deduction_rate
            hospital_margin_delta = -0.185
            volume_shift = +0.18
            discharge_latency_min = 72
            steps = [
                '1. Mandated bundled surgical cap enforced -> Consumable markup collapsed from 450% to 0%.',
                '2. Upfront price certainty established -> Elective procedure volume shifts by +18.0%.',
                '3. Unit margin compresses by -18.5% -> Compensated by volume scale (+18%) and lower dispute processing overhead.',
                '4. Standardized billing package eliminates TPA friction -> Average discharge latency reduces to 72 min.'
            ]
        elif intervention_type == 'unbundling_ban':
            consumable_markup = 0.15
            tpa_deduction_rate = 0.082
            avg_bill = base_procedure_cost * 1.12
            oop_shock = avg_bill * 0.09
            hospital_margin_delta = -0.075
            volume_shift = +0.10
            discharge_latency_min = 95
            steps = [
                '1. Hospital restricted to statutory 15% handling margin on PPE and disposables.',
                '2. Surprise bill items eliminated at discharge -> TPA dispute rate drops by 65%.',
                '3. Patient out-of-pocket variance narrows to +/-8% across hospital network.'
            ]
        elif intervention_type == 'chaos_boycott':
            consumable_markup = 5.20
            tpa_deduction_rate = 0.38
            avg_bill = base_procedure_cost * 1.65
            oop_shock = avg_bill * 0.42
            hospital_margin_delta = +0.28
            volume_shift = -0.32
            discharge_latency_min = 340
            steps = [
                '1. Hospital network withdraws cashless desk in protest -> Emergency cash-only admissions.',
                '2. TPA rejects unbundled claims -> Catastrophic patient debt alerts surge by +240%.',
                '3. Public defiance rating drops to Grade F -> Elective surgical admissions drop by -32%.'
            ]
        else: # baseline status quo
            consumable_markup = 4.50
            tpa_deduction_rate = 0.242
            avg_bill = base_procedure_cost * 1.48
            oop_shock = avg_bill * tpa_deduction_rate
            hospital_margin_delta = +0.14
            volume_shift = 0.0
            discharge_latency_min = 285
            steps = [
                '1. Baseline status quo: Median consumable markup at 450% above wholesale procurement.',
                '2. TPA disallows unbundled PPE & sterile disposables -> Surprise deduction of 24.2% on total bill.',
                '3. High out-of-pocket shock -> Average settlement delay at 285 min.'
            ]

        return {
            'interventionType': intervention_type,
            'simulatedTotalBill': round(avg_bill, 2),
            'consumableMarkupRate': round(consumable_markup * 100, 1),
            'tpaDeductionRate': round(tpa_deduction_rate * 100, 1),
            'expectedOutOfPocketShock': round(oop_shock, 2),
            'hospitalMarginDeltaPct': round(hospital_margin_delta * 100, 1),
            'volumeShiftPct': round(volume_shift * 100, 1),
            'dischargeLatencyMinutes': discharge_latency_min,
            'causalChain': steps
        }

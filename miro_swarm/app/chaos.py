import uuid
import json
from typing import Dict, Any, List
from .database import get_db

CHAOS_TEMPLATES = {
    'viral_bill_leak': {
        'name': 'Viral Bill Leak & Defiance Stand-Off',
        'target_entity': 'Hospital',
        'severity': 'Critical',
        'impact_description': 'Social media virality triggers regulatory audit and 240% surge in patient billing complaints.'
    },
    'tpa_preauth_blackout': {
        'name': 'Central TPA Outage & Pre-Auth Blackout',
        'target_entity': 'TPA',
        'severity': 'High',
        'impact_description': 'Central TPA portal down for 12 hours; cashless desks revert to emergency cash-only.'
    },
    'shadow_unbundling': {
        'name': 'Regulatory Cap Evasion & Shadow Unbundling',
        'target_entity': 'BillItem',
        'severity': 'Moderate',
        'impact_description': 'Hospital evades procedure caps by re-categorizing PPE into administrative disinfection charges.'
    }
}

class ChaosEngineeringEngine:
    @staticmethod
    def inject_disruption(world_id: str, template_key: str, custom_params: Dict[str, Any] = None) -> Dict[str, Any]:
        if template_key not in CHAOS_TEMPLATES:
            raise ValueError(f'Unknown disruption template: {template_key}')
        
        template = CHAOS_TEMPLATES[template_key]
        event_id = f'chaos-{uuid.uuid4().hex[:8]}'
        payload = {
            'template': template_key,
            'target': template['target_entity'],
            'severity': template['severity'],
            'impact': template['impact_description'],
            'parameters': custom_params or {}
        }
        
        with get_db() as db:
            cur = db.execute(
                'SELECT a.id FROM agents a JOIN worlds w ON w.experiment_id = a.experiment_id WHERE w.id = ? LIMIT 1',
                (world_id,)
            )
            row = cur.fetchone()
            agent_id = row['id'] if row else None

            db.execute(
                '''INSERT INTO simulation_events 
                   (id, world_id, round_index, agent_id, action_type, action_payload_json)
                   VALUES (?, ?, 0, ?, 'CHAOS_DISRUPTION', ?)''',
                (event_id, world_id, agent_id, json.dumps(payload))
            )
            db.execute('UPDATE worlds SET status = "disrupted" WHERE id = ?', (world_id,))

        return {
            'disruptionId': event_id,
            'worldId': world_id,
            'name': template['name'],
            'severity': template['severity'],
            'impact': template['impact_description'],
            'status': 'applied_to_world_only'
        }

import json
import uuid
from typing import Dict, Any, List, Optional
from .database import get_db

ENTITY_TYPES = [
    'Hospital', 'Procedure', 'BillItem', 'TPA', 'Patient',
    'Doctor', 'Regulator', 'PriceBenchmark', 'CommunityBowl'
]

RELATIONSHIP_TYPES = [
    'OFFERS', 'APPLIES', 'UNDERGOES', 'ADJUDICATES',
    'CONSTRAINS', 'REQUIRES', 'FILES', 'CONTESTS'
]

class DigitalTwinManager:
    @staticmethod
    def create_snapshot(project_id: str, version: int, description: str = '') -> str:
        snapshot_id = f'snap-{uuid.uuid4().hex[:8]}'
        with get_db() as db:
            # Mark previous snapshots inactive
            db.execute('UPDATE graph_snapshots SET is_active = 0 WHERE project_id = ?', (project_id,))
            db.execute(
                'INSERT INTO graph_snapshots (id, project_id, version, description, is_active) VALUES (?, ?, ?, ?, 1)',
                (snapshot_id, project_id, version, description)
            )
        return snapshot_id

    @staticmethod
    def add_node(snapshot_id: str, entity_type: str, name: str, properties: Dict[str, Any],
                 source_doc_id: Optional[str] = None, chunk_idx: Optional[int] = None,
                 confidence: float = 1.0) -> str:
        if entity_type not in ENTITY_TYPES:
            raise ValueError(f'Invalid entity type {entity_type}. Must be one of {ENTITY_TYPES}')
        node_id = f'node-{uuid.uuid4().hex[:8]}'
        with get_db() as db:
            db.execute(
                '''INSERT INTO graph_nodes 
                   (id, snapshot_id, entity_type, name, properties_json, source_document_id, source_chunk_index, confidence_score, human_approved)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?, 1)''',
                (node_id, snapshot_id, entity_type, name, json.dumps(properties), source_doc_id, chunk_idx, confidence)
            )
        return node_id

    @staticmethod
    def add_edge(snapshot_id: str, source_id: str, target_id: str, rel_type: str,
                 properties: Dict[str, Any], provenance: str = '') -> str:
        if rel_type not in RELATIONSHIP_TYPES:
            raise ValueError(f'Invalid relationship type {rel_type}. Must be one of {RELATIONSHIP_TYPES}')
        edge_id = f'edge-{uuid.uuid4().hex[:8]}'
        with get_db() as db:
            db.execute(
                '''INSERT INTO graph_edges 
                   (id, snapshot_id, source_node_id, target_node_id, relationship_type, properties_json, provenance_reference)
                   VALUES (?, ?, ?, ?, ?, ?, ?)''',
                (edge_id, snapshot_id, source_id, target_id, rel_type, json.dumps(properties), provenance)
            )
        return edge_id

    @staticmethod
    def get_snapshot_graph(snapshot_id: str) -> Dict[str, Any]:
        with get_db() as db:
            nodes_cur = db.execute('SELECT * FROM graph_nodes WHERE snapshot_id = ?', (snapshot_id,))
            nodes = []
            for r in nodes_cur.fetchall():
                nodes.append({
                    'id': r['id'],
                    'type': r['entity_type'],
                    'name': r['name'],
                    'properties': json.loads(r['properties_json']),
                    'provenance': {
                        'sourceDocId': r['source_document_id'],
                        'chunkIndex': r['source_chunk_index'],
                        'confidence': r['confidence_score']
                    }
                })

            edges_cur = db.execute('SELECT * FROM graph_edges WHERE snapshot_id = ?', (snapshot_id,))
            edges = []
            for r in edges_cur.fetchall():
                edges.append({
                    'id': r['id'],
                    'source': r['source_node_id'],
                    'target': r['target_node_id'],
                    'relationship': r['relationship_type'],
                    'properties': json.loads(r['properties_json']),
                    'provenance': r['provenance_reference']
                })

        return {
            'snapshotId': snapshot_id,
            'nodeCount': len(nodes),
            'edgeCount': len(edges),
            'nodes': nodes,
            'edges': edges
        }

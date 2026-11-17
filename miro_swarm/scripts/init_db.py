import sqlite3
import os
import json

DB_PATH = os.path.join(os.path.dirname(__file__), '../data/miro_swarm.db')

def init_db():
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    conn.execute('PRAGMA journal_mode=WAL;')
    cursor = conn.cursor()

    # 1. Projects
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS projects (
        id TEXT PRIMARY KEY,
        name TEXT NOT NULL,
        domain TEXT NOT NULL,
        decision_question TEXT NOT NULL,
        baseline_description TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    ''')

    # 2. Source Documents
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS source_documents (
        id TEXT PRIMARY KEY,
        project_id TEXT NOT NULL REFERENCES projects(id),
        file_name TEXT NOT NULL,
        file_path TEXT NOT NULL,
        file_size INTEGER NOT NULL,
        sha256 TEXT NOT NULL,
        status TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    ''')

    # 3. Graph Snapshots
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS graph_snapshots (
        id TEXT PRIMARY KEY,
        project_id TEXT NOT NULL REFERENCES projects(id),
        version INTEGER NOT NULL,
        description TEXT,
        is_active BOOLEAN DEFAULT 1,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    ''')

    # 4. Graph Nodes (9 Entity Types)
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS graph_nodes (
        id TEXT PRIMARY KEY,
        snapshot_id TEXT NOT NULL REFERENCES graph_snapshots(id),
        entity_type TEXT NOT NULL,
        name TEXT NOT NULL,
        properties_json TEXT NOT NULL,
        source_document_id TEXT REFERENCES source_documents(id),
        source_chunk_index INTEGER,
        confidence_score REAL DEFAULT 1.0,
        human_approved BOOLEAN DEFAULT 1
    );
    ''')

    # 5. Graph Edges (8 Relationship Types)
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS graph_edges (
        id TEXT PRIMARY KEY,
        snapshot_id TEXT NOT NULL REFERENCES graph_snapshots(id),
        source_node_id TEXT NOT NULL REFERENCES graph_nodes(id),
        target_node_id TEXT NOT NULL REFERENCES graph_nodes(id),
        relationship_type TEXT NOT NULL,
        properties_json TEXT NOT NULL,
        provenance_reference TEXT
    );
    ''')

    # 6. Experiments
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS experiments (
        id TEXT PRIMARY KEY,
        project_id TEXT NOT NULL REFERENCES projects(id),
        graph_snapshot_id TEXT NOT NULL REFERENCES graph_snapshots(id),
        name TEXT NOT NULL,
        rounds INTEGER NOT NULL DEFAULT 5,
        agent_count INTEGER NOT NULL DEFAULT 10,
        status TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    ''')

    # 7. Simulation Worlds (Isolated)
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS worlds (
        id TEXT PRIMARY KEY,
        experiment_id TEXT NOT NULL REFERENCES experiments(id),
        world_key TEXT NOT NULL,
        name TEXT NOT NULL,
        intervention_type TEXT NOT NULL,
        parameters_json TEXT NOT NULL,
        status TEXT NOT NULL
    );
    ''')

    # 8. Synthetic Agents
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS agents (
        id TEXT PRIMARY KEY,
        experiment_id TEXT NOT NULL REFERENCES experiments(id),
        role TEXT NOT NULL,
        persona_prompt TEXT NOT NULL,
        risk_tolerance REAL,
        financial_sensitivity REAL
    );
    ''')

    # 9. World-Scoped Memory (Strict Isolation)
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS world_agent_memories (
        id TEXT PRIMARY KEY,
        world_id TEXT NOT NULL REFERENCES worlds(id),
        agent_id TEXT NOT NULL REFERENCES agents(id),
        round_index INTEGER NOT NULL,
        memory_type TEXT NOT NULL,
        content TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    ''')

    # 10. Simulation Events
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS simulation_events (
        id TEXT PRIMARY KEY,
        world_id TEXT NOT NULL REFERENCES worlds(id),
        round_index INTEGER NOT NULL,
        agent_id TEXT NOT NULL REFERENCES agents(id),
        action_type TEXT NOT NULL,
        action_payload_json TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    ''')

    # 11. Adversarial Debates
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS adversarial_debates (
        id TEXT PRIMARY KEY,
        experiment_id TEXT NOT NULL REFERENCES experiments(id),
        round_index INTEGER NOT NULL,
        speaker_role TEXT NOT NULL,
        argument_text TEXT NOT NULL,
        evidence_citation TEXT,
        assumptions_stated TEXT
    );
    ''')

    # 12. Experiment Metrics
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS experiment_metrics (
        id TEXT PRIMARY KEY,
        experiment_id TEXT NOT NULL REFERENCES experiments(id),
        world_id TEXT REFERENCES worlds(id),
        category TEXT NOT NULL,
        metric_name TEXT NOT NULL,
        metric_value REAL NOT NULL,
        unit TEXT,
        formula_reference TEXT
    );
    ''')

    # 13. Benchmark Evaluations
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS benchmark_evaluations (
        id TEXT PRIMARY KEY,
        experiment_id TEXT NOT NULL REFERENCES experiments(id),
        dataset_name TEXT NOT NULL,
        target_metric TEXT NOT NULL,
        simulated_value REAL NOT NULL,
        benchmark_value REAL NOT NULL,
        error_mae REAL NOT NULL,
        error_delta_percent REAL NOT NULL,
        verdict TEXT NOT NULL,
        evaluated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    ''')

    conn.commit()
    conn.close()
    print("Database successfully initialized at:", DB_PATH)

if __name__ == '__main__':
    init_db()

import sqlite3
import os

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except sqlite3.Error as e:
        print(e)
    return conn

def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except sqlite3.Error as e:
        print(e)

def main():
    database_path = 'database/vex_gpt_source_of_truth.db'
    if not os.path.exists(database_path):
        open(database_path, 'w').close()
    
    sql_create_contexts_table = """
    CREATE TABLE IF NOT EXISTS contexts (
        id INTEGER PRIMARY KEY,
        role TEXT NOT NULL,
        context TEXT NOT NULL,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    );
    """
    
    sql_create_relationships_table = """
    CREATE TABLE IF NOT EXISTS relationships (
        id INTEGER PRIMARY KEY,
        entity_1 TEXT NOT NULL,
        entity_2 TEXT NOT NULL,
        relationship_type TEXT NOT NULL,
        details TEXT,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    );
    """
    
    conn = create_connection(database_path)
    
    if conn is not None:
        create_table(conn, sql_create_contexts_table)
        create_table(conn, sql_create_relationships_table)
    else:
        print("Error! Cannot create the database connection.")
    
    conn.close()

if __name__ == '__main__':
    main()
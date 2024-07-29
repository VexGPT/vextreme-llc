import os
import shutil
import sqlite3

def clear_dynamic_context(base_dir='Contexts'):
    conn = sqlite3.connect('database/vex_gpt_source_of_truth.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM contexts WHERE role='VEXGPT'")
    conn.commit()
    conn.close()

    for root, dirs, _ in os.walk(base_dir):
        for d in dirs:
            if d not in ['initial_context']:
                shutil.rmtree(os.path.join(root, d))

if __name__ == "__main__":
    clear_dynamic_context()
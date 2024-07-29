import json
import sqlite3

class DynamicContextManager:
    def __init__(self):
        self.context = {}

    def load_context(self, context):
        self.context = context

    def process_input(self, user_input):
        # Process the input and update context accordingly
        response = f"Processing: {user_input}"
        self.update_context(user_input)
        return response

    def update_context(self, user_input):
        # Update the context based on user input
        self.context['last_input'] = user_input
        self.save_context()

    def save_context(self):
        with open('Contexts/dynamic_context.json', 'w') as f:
            json.dump(self.context, f)

        conn = sqlite3.connect('Database/vex_gpt_source_of_truth.db')
        c = conn.cursor()
        c.execute('INSERT INTO context (context) VALUES (?)', (json.dumps(self.context),))
        conn.commit()
        conn.close()
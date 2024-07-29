import os
import sqlite3
import logging
from openai import OpenAI
from dynamic_context_manager import process_command

client = OpenAI(api_key=open("api_key.txt").read().strip())

MODEL = "gpt-4o"

logging.basicConfig(filename='vex_gpt.log', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')

def load_context(role):
    db_file = "database/vex_gpt_source_of_truth.db"
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute("SELECT context FROM contexts WHERE role=?", (role,))
    result = cursor.fetchone()
    conn.close()
    if result:
        return result[0]
    return ""

def add_context(role, new_context):
    db_file = "database/vex_gpt_source_of_truth.db"
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO contexts (role, context) VALUES (?, ?)", (role, new_context))
    conn.commit()
    conn.close()

def read_all_text_files_in_directory(directory):
    context_data = ""
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".txt"):
                file_path = os.path.join(root, file)
                with open(file_path, 'r') as f:
                    context_data += f.read() + "\n"
    return context_data

def generate_response(prompt, context):
    response = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "system", "content": context}, {"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

def identify_new_context(user_input, context):
    identify_context_path = "Contexts/identify_new_context.txt"
    if not os.path.exists(identify_context_path):
        return ""
    prompt = open(identify_context_path).read()
    response = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "system", "content": context}, {"role": "user", "content": prompt}, {"role": "user", "content": user_input}]
    )
    return response.choices[0].message.content

def main():
    role = "VEXGPT"
    context = load_context(role)
    if not context:
        context = read_all_text_files_in_directory("Contexts/initial_context/")
        add_context(role, context)
        logging.info(f"Initial context loaded and saved for role: {role}")

    while True:
        user_input = input("You: ")
        new_context_check = identify_new_context(user_input, context)
        if "Command:" in new_context_check:
            command_parts = new_context_check.split("Command:")
            if len(command_parts) > 1:
                command = command_parts[1].strip()
                if process_command(command):
                    print(f"Command executed: {command}")
                    logging.info(f"Command executed: {command}")
                else:
                    print(f"Command failed: {command}")
                    logging.info(f"Command failed: {command}")
            else:
                print("No valid command found in the response.")
                logging.info("No valid command found in the response.")
        else:
            response = generate_response(user_input, context)
            print(f"VEX GPT: {response}")
            logging.info(f"User: {user_input}")
            logging.info(f"VEX GPT: {response}")

if __name__ == "__main__":
    main()
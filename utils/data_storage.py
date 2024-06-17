import json
import os

# Ensure the data directory exists
DATA_FILE_PATH = 'data/interview_data.json'
os.makedirs(os.path.dirname(DATA_FILE_PATH), exist_ok=True)

def store_interview_data(data):
    """
    Stores interview data (questions and answers) to a JSON file.

    Args:
        data (list): A list of tuples containing questions and answers.
    """
    with open(DATA_FILE_PATH, 'w') as file:
        json.dump(data, file, indent=4)

def retrieve_interview_data():
    """
    Retrieves interview data (questions and answers) from a JSON file.

    Returns:
        list: A list of tuples containing questions and answers.
    """
    try:
        with open(DATA_FILE_PATH, 'r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        return []

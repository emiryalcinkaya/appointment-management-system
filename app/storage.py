import json
import os


# Get project root directory
BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

# Create JSON file path
FILE_PATH = os.path.join(
    BASE_DIR,
    "data",
    "appointments.json"
)

# Load appointments from JSON file
def load_appointments():

    with open(FILE_PATH, "r") as file:
        return json.load(file)

# Save appointments into JSON file
def save_appointments(appointments):

    with open(FILE_PATH, "w") as file:
        json.dump(appointments, file, indent=4)
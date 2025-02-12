import json
import os

class FileManager:
    def __init__(self, filename="notes.json"):
        self.filename = filename

    def load_notes(self):
        try:
            with open(self.filename, "r") as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):  # Handle file not found or empty
            return []  # Return an empty list, not None!

    def save_notes(self, notes):
        note_data = [note.to_dict() for note in notes]  # Convert Note objects to dictionaries
        try:
            with open(self.filename, "w") as f:
                json.dump(note_data, f, indent=4)  # Save with indentation for readability
        except Exception as e:
            print(f"Error saving notes: {e}") # Print error message (or handle it more gracefully)
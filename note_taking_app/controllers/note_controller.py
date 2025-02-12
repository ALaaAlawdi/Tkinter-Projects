from models.note import Note
from utils.file_manager import FileManager


class NoteController:
    def __init__(self, view):  # Removed model parameter
        self.view = view
        self.file_manager = FileManager()  # Initialize file manager
        self.notes = []  # List to store notes
        self.load_notes()  # Load notes on startup

    def load_notes(self):
        note_data_list = self.file_manager.load_notes()
        if note_data_list:
          for note_data in note_data_list:
              note = Note.from_dict(note_data)
              self.notes.append(note)
        self.view.update_note_list(self.notes)  # Use self.notes

    def add_note(self):
        new_note = Note()  # Use default values
        self.notes.append(new_note)  # Add to self.notes
        self.view.update_note_list(self.notes)
        self.view.show_note_content(new_note.title, new_note.content)

    def delete_note(self):
        try:
            selected_index = self.view.note_listbox.curselection()[0]
            del self.notes[selected_index]  # Remove from self.notes
            self.view.update_note_list(self.notes)
        except IndexError:
            self.view.show_message("No note selected.")

    def open_note(self, event):
        try:
            selected_index = self.view.note_listbox.curselection()[0]
            selected_note = self.model.get_all_notes()[selected_index]
            self.view.show_note_content(selected_note.title, selected_note.content)
        except IndexError:
            self.view.show_message("No note selected.")

    def save_note(self):
      title, content = self.view.note_window.get_note_data()
      if title:
          note = self.find_note(self.view.note_window.note_title)
          if note:
              note.title = title # Update the title
              note.content = content
              self.file_manager.save_notes(self.notes) # Save self.notes
              self.view.note_window.destroy() # Close the note window
              self.view.update_note_list(self.notes) # Update with self.notes
          else:
              self.view.show_message("Note not found.")
      else:
          self.view.show_message("Title cannot be empty.")

    def find_note(self, title):
        for note in self.notes:
            if note.title == title:
                return note
        return None
    
    def close_note(self, original_title):
        note = self.model.find_note(original_title)
        if note:
            self.view.update_note_list(self.model.get_all_notes())
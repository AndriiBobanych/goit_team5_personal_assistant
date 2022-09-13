import os
from pathlib import Path


class NoteBook:

    @staticmethod
    def add_note(note, tag, text):
        file_name = note + ".txt"
        full_pass = os.path.join(Path().resolve(), "notes", file_name)
        text_for_note = {
            "note": note,
            "tag": tag,
            "text": "\n"+text,
            }
        if not os.path.isfile(full_pass):
            with open(full_pass, 'w', encoding='utf8') as file:
                for key, val in text_for_note.items():
                    file.writelines(f"{key}: {val}\n")
            return f"Your new note with name '{note}' is created in folder 'notes'"
        else:
            return f"Note with name '{note}' is already exist in folder 'notes'"

    @staticmethod
    def read_note(note):
        file_name = note + ".txt"
        full_pass = os.path.join(Path().resolve(), "notes", file_name)
        note = ""
        tag = ""
        text = ""

        if os.path.isfile(full_pass):
            with open(full_pass, 'r', encoding='utf8') as file:
                note_data = file.readlines()
                for index, line in enumerate(note_data):
                    if index == 0:
                        note = line.replace('\n', '')
                    elif index == 1:
                        tag = line.replace('\n', '')
                    else:
                        text += line
            return f"{note}\n{tag}\n{text.strip()}"
        return f"Note with name '{note}' was not found in folder 'notes'"

    @staticmethod
    def update_note(note, tag, text):
        file_name = note + ".txt"
        full_pass = os.path.join(Path().resolve(), "notes", file_name)

        if os.path.isfile(full_pass):
            with open(full_pass, "w", encoding='utf8') as file:
                file.writelines(f"note: {note}\n")
                file.writelines(f"{tag}\n")
                file.writelines(text)
            return f"Note '{note}' was updated successfully!"
        else:
            return f"Note with name '{note}' was not found in folder 'notes'"

    @staticmethod
    def delete_note(note):
        file_name = note + ".txt"
        full_pass = os.path.join(Path().resolve(), "notes", file_name)

        if os.path.isfile(full_pass):
            os.remove(full_pass)
            return f"Your note with name '{note}' was deleted from folder 'notes'"
        else:
            return f"Note with name '{note}' was not found in folder 'notes'"

    @staticmethod
    def show_all_notes():
        folder = os.path.join(Path().resolve(), "notes")
        notes_list = []

        for filename in os.listdir(folder):
            notes_list.append(filename)

        if len(notes_list) == 0:
            return f"Your notebook is still empty.\nPlease add your first note"
        else:
            first_string = "Your notebook has the following notes:\n"
            note_lines = "\n".join(str(record) for record in list(notes_list))
            return first_string + note_lines

    @staticmethod
    def find_by_tag(tag):
        folder = os.path.join(Path().resolve(), "notes")
        list_of_notes = []

        for filename in os.listdir(folder):
            note_to_do = NoteBook.read_note(filename.split('.')[0])
            tags = note_to_do.split('\n')[1].split()
            if tag in tags:
                list_of_notes.append(filename)

        if len(list_of_notes) == 0:
            return f"I can't find any note by this tag.\nPlease enter a valid note's tag for search."
        else:
            first_string = "I found the following notes by your tag:\n"
            note_names = "\n".join(str(record) for record in list(list_of_notes))
            return first_string + note_names

    @staticmethod
    def find_by_name(note):
        folder = os.path.join(Path().resolve(), "notes")
        list_of_notes = []

        for filename in os.listdir(folder):
            if note in filename.split('.')[0]:
                list_of_notes.append(filename)

        if len(list_of_notes) == 0:
            return f"I can't find any note that contain this name.\nPlease enter a valid note's name for search."
        else:
            first_string = "I found  the following notes by searching name:\n"
            note_names = "\n".join(str(record) for record in list(list_of_notes))
            return first_string + note_names


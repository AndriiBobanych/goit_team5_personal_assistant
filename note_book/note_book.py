import os
from pathlib import Path


class Note:

    def __init__(self, note=None, tag=None, text=None):
        self.note = note
        self.tag = [tag] if tag is not None else []
        self.text = [text] if text is not None else []

    def __repr__(self):
        return f"note: {self.note.value},\n" \
               f"tag: {' '.join(tag.value for tag in self.tag)},\n" \
               f"text: {' '.join(text.value for text in self.text)},"

    def add_tag(self, new_tag: str):
        self.tag.append(new_tag)

    def add_text(self, new_text: str):
        self.text.append(new_text)

    def change_tag(self, old_tag: str, new_tag: str):
        try:
            self.tag.remove(old_tag)
            self.tag.append(new_tag)
        except ValueError:
            return f"Your note does not contain such tag: {old_tag}"

    def change_text(self, old_text: str, new_text: str):
        try:
            self.text.remove(old_text)
            self.text.append(new_text)
        except ValueError:
            return f"Your note does not contain such text: {old_text}"

    def delete_tag(self, tag: str):
        try:
            self.tag.remove(tag)
        except ValueError:
            return f"Your note does not contain such tag: {tag}"

    def delete_text(self, text: str):
        try:
            self.text.remove(text)
        except ValueError:
            return f"Your note does not contain such text: {text}"


class NoteBook(Note):

    @staticmethod
    def add_note(note, tag, text):
        current_path = Path().resolve()
        file_name = note + ".txt"
        full_pass = os.path.join(current_path, "notes", file_name)
        text_for_note = {"note": note,
                         "tag": tag.split(" "),
                         "text": [text],
                         }
        if not os.path.isfile(full_pass):
            with open(full_pass, 'w', encoding='utf8') as file:
                for key, val in text_for_note.items():
                    file.writelines(f"{key}: {val},\n")
            return f"Your new note with name '{note}' is created in folder 'notes'"
        else:
            return f"Note with name '{note}' is already exist in folder 'notes'"

    @staticmethod
    def read_note(note):
        current_path = Path().resolve()
        file_name = note + ".txt"
        full_pass = os.path.join(current_path, "notes", file_name)
        one_note_text = {}

        if os.path.isfile(full_pass):
            with open(full_pass, 'r', encoding='utf8') as file:
                note_data = file.readlines()
                for line in note_data:
                    items = line.split(":")
                    one_note_text[items[0]] = items[1]
            return one_note_text
        else:
            return f"Note with name '{note}' was not found in folder 'notes'"

    @staticmethod
    def update_note(note, updated_dict):
        current_path = Path().resolve()
        file_name = note + ".txt"
        full_pass = os.path.join(current_path, "notes", file_name)

        if os.path.isfile(full_pass):
            with open(full_pass, "w+", encoding='utf8') as file:
                for key, val in updated_dict.items():
                    file.writelines(f"{key}: {val},\n")
            return f"Note '{note}' was updated successfully!"

        else:
            return f"Note with name '{note}' was not found in folder 'notes'"

    @staticmethod
    def delete_note(note):
        current_path = Path().resolve()
        file_name = note + ".txt"
        full_pass = os.path.join(current_path, "notes", file_name)

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
        pass
        # folder = os.path.join(Path().resolve(), "notes")
        # notes_list_for_tag = []
        #
        # for filename in os.listdir(folder):
        #     NoteBook.read_note(filename)
        #     tags_list
        #
        # if note in notes_list:
        #     return True
        # else:
        #     return False

    @staticmethod
    def find_by_name(note):
        pass
        # folder = os.path.join(Path().resolve(), "notes")
        # notes_name_list = []
        # matched_note = None
        #
        # for filename in os.listdir(folder):
        #     notes_name_list.append(filename.removesuffix(".txt"))
        #
        # if note in notes_name_list:
        #     matched_note = note
        #
        # return matched_note


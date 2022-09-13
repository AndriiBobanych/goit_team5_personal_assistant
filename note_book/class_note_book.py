import os
from pathlib import Path


# class Note:
#
#     def __init__(self, note=None, tag=None, text=None):
#         self.note = note
#         self.tag = [tag] if tag is not None else []
#         self.text = [text] if text is not None else []
#
#     def __repr__(self):
#         return f"note: {self.note.value},\n" \
#                f"tag: {' '.join(tag.value for tag in self.tag)},\n" \
#                f"text: {' '.join(text.value for text in self.text)},"
#
#     def add_tag(self, new_tag: str):
#         self.tag.append(new_tag)
#
#     def add_text(self, new_text: str):
#         self.text.append(new_text)
#
#     def change_tag(self, old_tag: str, new_tag: str):
#         try:
#             self.tag.remove(old_tag)
#             self.tag.append(new_tag)
#         except ValueError:
#             return f"Your note does not contain such tag: {old_tag}"
#
#     def change_text(self, old_text: str, new_text: str):
#         try:
#             self.text.remove(old_text)
#             self.text.append(new_text)
#         except ValueError:
#             return f"Your note does not contain such text: {old_text}"
#
#     def delete_tag(self, tag: str):
#         try:
#             self.tag.remove(tag)
#         except ValueError:
#             return f"Your note does not contain such tag: {tag}"
#
#     def delete_text(self, text: str):
#         try:
#             self.text.remove(text)
#         except ValueError:
#             return f"Your note does not contain such text: {text}"


class NoteBook:

    @staticmethod
    def add_note(note, tag, text):
        # folder = os.path.join(Path().resolve(), 'notes')
        # if not os.path.exists(folder):
        #     os.mkdir(folder)
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
        # shit = []
        # # if len(os.listdir(folder)) == 0:
        # #     with open(os.path.join(folder, file_name), 'w', encoding='utf8') as file:
        # #         for key, val in text_for_note.items():
        # #             file.writelines(f"{key}: {val},\n")
        # #     return f"Your new note with name '{file_name}' is created in folder 'notes'"
        # # else:
        # #
        # #     for el in Path(folder).iterdir():
        # #         if el.is_file() and el.name != file_name:
        # #             shit.append(True)
        # #         elif el.is_file() and el.name == file_name:
        # #             shit.append(False)
        # #     result = all(shit)
        # #     if result:
        # #         with open(os.path.join(folder, file_name), 'w', encoding='utf8') as file:
        # #             for key, val in text_for_note.items():
        # #                 file.writelines(f"{key}: {val}\n")
        # #         return f"Your new note with name '{file_name}' is created in folder 'notes'"
        # #
        # #
        # #     else:
        # #         return f"Note with name '{file_name}' is already exist in folder 'notes'"

    @staticmethod
    def read_note(note):
        # one_note_text = {}
        # folder = os.path.join(Path().resolve(), 'notes')
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

        # if os.path.isfile(full_pass):
        #     with open(full_pass, 'r', encoding='utf8') as file:
        #         note_data = file.readlines()
        #     for line in note_data:
        #         items = line.split(": ")
        #
        #         if items[0] == "note":
        #             one_note_text[items[0]] = items[1].replace('\n', '').replace(',', '')
        #         elif items[0] == "tag":
        #             normalized_tag = items[1].replace('\n', '').replace(',', '')
        #             one_note_text[items[0]] = normalized_tag.strip('][').split(', ')
        #         elif items[0] == "text":
        #             normalized_text = items[1].replace('\n', '').replace(',', '')
        #             one_note_text[items[0]] = normalized_text.strip('][').split(', ')
        #
        #     return one_note_text
        # else:
        #     return f"Note with name '{note}' was not found in folder 'notes'"
        #
        # for el in Path(folder).iterdir():
        #     if el.is_file() and el.name == file_name:
        #         with open(os.path.join(folder, file_name), 'r', encoding='utf8') as file:
        #             note_data = file.readlines()
        #             for line in note_data:
        #                 items = line.split(":")
        #                 one_note_text[items[0]] = items[1].strip().replace('\n', '')
        #         return one_note_text
        #
        # return f"Note with name '{note}' was not found in folder 'notes'"

    @staticmethod
    def update_note(note, tag, text):
        # folder = os.path.join(Path().resolve(), 'notes')
        file_name = note + ".txt"
        full_pass = os.path.join(Path().resolve(), "notes", file_name)

        if os.path.isfile(full_pass):
            with open(full_pass, "w", encoding='utf8') as file:
                file.writelines(f"note: {note}\n")
                file.writelines(f"{tag}\n")
                file.writelines(text)

                # for key, val in updated_dict.items():
                #     file.writelines(f"{key}: {val},\n")

            return f"Note '{note}' was updated successfully!"
        else:
            return f"Note with name '{note}' was not found in folder 'notes'"
        # open(os.path.join(folder, file_name), "w").close()
        # for el in Path(folder).iterdir():
        #     if el.is_file() and el.name == file_name:
        #         with open(os.path.join(folder, file_name), "w", encoding='utf8') as file:
        #             for key, val in updated_dict.items():
        #                 file.writelines(f"{key}: {val}\n")
        #         return f"Note '{note}' was updated successfully!"
        #     else:
        #         return f"Note with name '{note}' was not found in folder 'notes'"

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
        # return list_of_notes
        # for filename in os.listdir(folder):
        #     for key, val in NoteBook.read_note(filename.split('.')[0]).items():
        #         if key == 'tag':
        #             if tag in val:
        #                 list_of_notes.append(filename)
        #
        # if len(list_of_notes) == 0:
        #     return f"I can't find any note by this tag.\nPlease enter a valid note's tag for search."
        # else:
        #     first_string = "I found the following notes by your tag:\n"
        #     note_names = "\n".join(str(record) for record in list(list_of_notes))
        #     return first_string + note_names

    @staticmethod
    def find_by_name(note):
        folder = os.path.join(Path().resolve(), "notes")
        list_of_notes = []
        # for filename in os.listdir(folder):
        #     for key, val in NoteBook.read_note(filename.split('.')[0]).items():
        #         if key == 'note':
        #             if str(val).find(name) != -1:
        #                 list_of_notes.append(filename)
        for filename in os.listdir(folder):
            if note in filename.split('.')[0]:
                list_of_notes.append(filename)
        if len(list_of_notes) == 0:
            return f"I can't find any note that contain this name.\nPlease enter a valid note's name for search."
        else:
            first_string = "I found  the following notes by searching name:\n"
            note_names = "\n".join(str(record) for record in list(list_of_notes))
            return first_string + note_names


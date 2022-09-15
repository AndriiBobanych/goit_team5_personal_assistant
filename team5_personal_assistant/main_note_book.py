import functools
import os
from pathlib import Path

# try:
#     from class_note_book import *
# except:
#     from .class_note_book import *


# -------------------------- class NoteBook --------------------------


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


# -------------------------- class CLINoteBook --------------------------


NOTEBOOK = NoteBook()


def is_exist(note):
    file_name = note + ".txt"
    full_pass = os.path.join(Path().resolve(), "notes", file_name)
    if os.path.exists(full_pass):
        return True
    else:
        return False


def command_error_handler(func):
    @functools.wraps(func)
    def wrapper(*args):
        try:
            return func(*args)
        except ValueError as e:
            return str(e)
        except KeyError as e:
            return str(e)
        except Exception as e:
            return str(e)
    return wrapper


class CLINoteBook:

    @staticmethod
    def help_handler():
        return ("""
You can use the following commands for your NoteBook:
    - add note -> to create new note and save into folder 'notes';
    - read note -> to open indicated note and read text inside;
    - delete note -> to delete indicated note from the folder;

    - find by tag -> to find all notes that are matched with this tag;
    - find by name -> to find notes that are matched with this name;
    - show all notes -> to show list of notes that were saved in folder;

    - add tag -> to include additional tag to existing note;
    - add text -> to include additional text to existing note;
    - change tag -> to change existing tag in note (recommend to read note first);
    - change text -> to change existing text in note (recommend to read note first);
    - delete tag -> to delete existing tag in note (recommend to read note first);
    - delete text -> to delete existing text in note (recommend to read note first);
    """)

    @command_error_handler
    def add_note_handler(self=None):
        note = input("Please enter name for note: ")
        if note == "":
            return "Name of note is missed. Please try again"
        elif is_exist(note):
            return f"Note with name '{note}' is already exist in folder 'notes'"
        else:
            tag = input("Please enter tags (start with #, space to divide): ")
            text = input("Please enter text for note: ")
            return NOTEBOOK.add_note(note, tag, text)

    @command_error_handler
    def read_note_handler(self=None):
        note = input("Please enter name of note to read it (without '.txt'): ")
        if note != "":
            return NOTEBOOK.read_note(note)
        else:
            return "Name of note is missed. Please try again"

    @command_error_handler
    def delete_note_handler(self=None):
        note = input("Please enter name of note to delete it (without '.txt'): ")
        if note != "":
            return NOTEBOOK.delete_note(note)
        else:
            return "Name of note is missed. Please try again"

    @command_error_handler
    def find_tag_handler(self=None):
        tag = input("Please enter 1 tag to find notes (start with #): ")
        if tag != "":
            return NOTEBOOK.find_by_tag(tag)
        else:
            return "Tag for search is missed. Please try again"

    @command_error_handler
    def find_note_handler(self=None):
        note = input("Please enter name to find note (without '.txt'): ")
        if note != "":
            return NOTEBOOK.find_by_name(note)
        else:
            return "Name for search is missed. Please try again"

    @command_error_handler
    def show_all_handler(self=None):
        return NOTEBOOK.show_all_notes()

    @command_error_handler
    def add_tag_handler(self=None):
        note = input("Please enter name of note to update info (without '.txt'): ")
        if is_exist(note):
            tag = input("Please use 1 tag to add to this note (start with #): ")
            note_to_do = NOTEBOOK.read_note(note)
            old_tag = ''
            old_text = ''

            for i, item in enumerate(note_to_do.split('\n'), start=0):
                if i == 1:
                    old_tag = item + ' '

            for i, item in enumerate(note_to_do.split('\n')[2:], start=0):
                old_text += item + '\n'

            return NOTEBOOK.update_note(note, old_tag + tag, old_text)
        else:
            raise ValueError(f"Note with name '{note}' does not exist in NoteBook.")

    @command_error_handler
    def add_text_handler(self=None):
        note = input("Please enter name of note to update info (without '.txt'): ")
        if is_exist(note):
            text = input("Please write text to add to the current note: ")
            note_to_do = NOTEBOOK.read_note(note)
            old_tag = ''
            old_text = ''

            for i, item in enumerate(note_to_do.split('\n'), start=0):
                if i == 1:
                    old_tag = item

            for i, item in enumerate(note_to_do.split('\n')[2:], start=0):
                old_text += item + '\n'

            return NOTEBOOK.update_note(note, old_tag, old_text + text)
        else:
            raise ValueError(f"Note with name '{note}' does not exist in NoteBook.")

    @command_error_handler
    def change_tag_handler(self=None):
        note = input("Please enter name of note to update info (without '.txt'): ")
        if is_exist(note):
            note_to_do = NOTEBOOK.read_note(note)
            tag_list = note_to_do.split('\n')[1]
            new_tag = ''
            new_text = ''

            for i, item in enumerate(tag_list.split(), start=0):
                print(i, item)
            tag_index = int(input("Please enter index of tag that you want to change: "))
            tag = input("Please write new tag to add instead old to the current note: ")

            for i, item in enumerate(tag_list.split(), start=0):
                if i == tag_index:
                    item = tag
                new_tag += item + ' '

            for i, item in enumerate(note_to_do.split('\n')[2:], start=0):
                new_text += item + '\n'

            return NOTEBOOK.update_note(note, new_tag, new_text)
        else:
            raise ValueError(f"Note with name '{note}' does not exist in NoteBook.")

    @command_error_handler
    def change_text_handler(self=None):
        note = input("Please enter name of note to update info (without '.txt'): ")
        if is_exist(note):
            note_to_do = NOTEBOOK.read_note(note)
            new_tag = ''
            new_text = ''

            for i, item in enumerate(note_to_do.split('\n')[2:], start=0):
                print(i, item)
            text_index = int(input("Please enter index of text that you want to change: "))
            text = input("Please write new text to add instead old to the current note: ")

            for i, item in enumerate(note_to_do.split('\n'), start=0):
                if i == 1:
                    new_tag = item

            for i, item in enumerate(note_to_do.split('\n')[2:], start=0):
                if i == text_index:
                    item = text
                new_text += item + '\n'

            return NOTEBOOK.update_note(note, new_tag, new_text)
        else:
            raise ValueError(f"Note with name '{note}' does not exist in NoteBook.")

    @command_error_handler
    def delete_tag_handler(self=None):
        note = input("Please enter name of note to update info (without '.txt'): ")
        if is_exist(note):
            note_to_do = NOTEBOOK.read_note(note)
            tag_list = note_to_do.split('\n')[1]
            new_tag = ''
            new_text = ''

            for i, item in enumerate(tag_list.split(), start=0):
                print(i, item)
            tag_index = int(input("Please enter index of tag that you want to delete: "))

            for i, item in enumerate(tag_list.split(), start=0):
                if i == tag_index:
                    item = ""
                new_tag += item + ' '

            for i, item in enumerate(note_to_do.split('\n')[2:], start=0):
                new_text += item + '\n'

            return NOTEBOOK.update_note(note, new_tag.strip(), new_text)
        else:
            raise ValueError(f"Note with name '{note}' does not exist in NoteBook.")

    @command_error_handler
    def delete_text_handler(self=None):
        note = input("Please enter name of note to update info (without '.txt'): ")
        if is_exist(note):
            note_to_do = NOTEBOOK.read_note(note)
            tag_list = note_to_do.split('\n')[1]
            new_tag = ''
            new_text = ''

            for i, item in enumerate(note_to_do.split('\n')[2:], start=0):
                print(i, item)
            text_index = int(input("Please enter index of text that you want to delete: "))

            for i, item in enumerate(tag_list.split('\n'), start=0):
                if i == 0:
                    new_tag = item

            for i, item in enumerate(note_to_do.split('\n')[2:], start=0):
                if i == text_index:
                    item = ''
                new_text += item + '\n'

            return NOTEBOOK.update_note(note, new_tag, new_text.strip())
        else:
            raise ValueError(f"Note with name '{note}' does not exist in NoteBook.")

    notes_commands_dict = {
        "help": help_handler,

        "add note": add_note_handler,
        "read note": read_note_handler,
        "delete note": delete_note_handler,

        "find by tag": find_tag_handler,
        "find by name": find_note_handler,
        "show all": show_all_handler,

        "add tag": add_tag_handler,
        "add text": add_text_handler,
        "change tag": change_tag_handler,
        "change text": change_text_handler,
        "delete tag": delete_tag_handler,
        "delete text": delete_text_handler,
        }

    @staticmethod
    def run_notes_assistant():

        folder = os.path.join(Path().resolve(), 'notes')
        if not os.path.exists(folder):
            os.mkdir(folder)

        print("Hello! I'm here to assist you with your NoteBook.")
        print("You could enter exact commands if you already know them.\n"
              "Or please use:\n"
              "  help -> to see whole list of commands\n"
              "  close -> to finish work with NoteBook")

        while True:
            command = input("Please enter your command: ").lower().strip()

            if command == "close":
                # raise SystemExit("\nThank you for using NoteBook Bot.\nSee you later!\n")
                return "\nThank you for using NoteBook Bot.\nSee you later!\n"
                # break

            elif command in CLINoteBook.notes_commands_dict.keys():
                handler = CLINoteBook.notes_commands_dict[command]
                answer = handler()
                print(answer)

            else:
                list_comm = []
                for k in CLINoteBook.notes_commands_dict.keys():
                    for item in k.split():
                        if command in item:
                            list_comm.append(k)
                            break
                if list_comm:
                    print('You mean these commands: ')
                    print(*list_comm, sep=', ')
                else:
                    print("Incorrect input.\nPlease check and enter correct command (or 'help' or 'close').")


if __name__ == '__main__':
    CLINoteBook.run_notes_assistant()

import functools
import os
from pathlib import Path

try:
    from class_note_book import *
except:
    from .class_note_book import *


# NOTE = Note()
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
            # old_name = ""
            # for i, item in enumerate(note_to_do.split('\n'), start=0):
            #     if i == 0:
            #         old_name = item
            old_tag = ''
            for i, item in enumerate(note_to_do.split('\n'), start=0):
                if i == 1:
                    old_tag = item + ' '
            old_text = ''
            for i, item in enumerate(note_to_do.split('\n')[2:], start=0):
                old_text += item + '\n'

            return NOTEBOOK.update_note(note, old_tag + tag, old_text)
            # note_to_do = NOTEBOOK.read_note(note)
            # note_to_do["tag"].append(tag)
            # return NOTEBOOK.update_note(note, note_to_do)
        else:
            raise ValueError(f"Note with name '{note}' does not exist in NoteBook.")

    @command_error_handler
    def add_text_handler(self=None):
        note = input("Please enter name of note to update info (without '.txt'): ")
        if is_exist(note):
            text = input("Please write text to add to the current note: ")
            note_to_do = NOTEBOOK.read_note(note)
            # old_name = ""
            # for i, item in enumerate(note_to_do.split('\n'), start=0):
            #     if i == 0:
            #         old_name = item
            old_tag = ''
            for i, item in enumerate(note_to_do.split('\n'), start=0):
                if i == 1:
                    old_tag = item
            old_text = ''
            for i, item in enumerate(note_to_do.split('\n')[2:], start=0):
                old_text += item + '\n'

            return NOTEBOOK.update_note(note, old_tag, old_text + text)
            # note_to_do["text"].append(text)
            # return NOTEBOOK.update_note(note, note_to_do)
        else:
            raise ValueError(f"Note with name '{note}' does not exist in NoteBook.")

        # note = input("Please enter name of note to update info (without '.txt': ")
        # try:
        #     text = input("Please write text to add to the current note: ")
        #     note_to_do = NOTEBOOK.read_note(note)
        #     new_dict = {}
        #     new_lst = []
        #     new_lst.append(note_to_do["text"])
        #     new_lst.append(text)
        #
        #     new_dict['tag'] = note_to_do["tag"]
        #     new_dict['text'] = new_lst
        #     return NOTEBOOK.update_note(note, new_dict)
        #
        # except Exception:
        #     raise ValueError(f"Note with name '{note}' does not exist in NoteBook.")

    @command_error_handler
    def change_tag_handler(self=None):
        note = input("Please enter name of note to update info (without '.txt'): ")
        if is_exist(note):
            note_to_do = NOTEBOOK.read_note(note)
            tag_list = note_to_do.split('\n')[1]
            for i, item in enumerate(tag_list.split(), start=0):
                print(i, item)
            tag_index = int(input("Please enter index of tag that you want to change: "))
            tag = input("Please write new tag to add instead old to the current note: ")
            # note_to_do["tag"][tag_index] = new_tag
            # old_name = ""
            # for i, item in enumerate(note_to_do.split('\n'), start=0):
            #     if i == 0:
            #         old_name = item
            new_tag = ''
            for i, item in enumerate(tag_list.split(), start=0):
                if i == tag_index:
                    item = tag
                new_tag += item + ' '
            new_text = ''
            for i, item in enumerate(note_to_do.split('\n')[2:], start=0):
                new_text += item + '\n'

            return NOTEBOOK.update_note(note, new_tag, new_text)
            # return NOTEBOOK.update_note(note, note_to_do)
        else:
            raise ValueError(f"Note with name '{note}' does not exist in NoteBook.")

        # note = input("Please enter name of note to update info (without '.txt': ")
        # try:
        #     note_to_do = NOTEBOOK.read_note(note)
        #     tag_list = note_to_do["tag"].split()
        #     for i, item in enumerate(tag_list, start=0):
        #         print(i, item)
        #     tag_index = int(input("Please enter index of tag that you want to change: "))
        #     new_tag = input("Please write new tag to add instead old to the current note: ")
        #     tag_list[tag_index] = new_tag
        #     new_dict = {}
        #     new_dict['tag'] = tag_list
        #     new_dict['text'] = note_to_do["text"]
        #
        #     return NOTEBOOK.update_note(note, new_dict)
        # except Exception:
        #     raise ValueError(f"Note with name '{note}' does not exist in NoteBook.")

    @command_error_handler
    def change_text_handler(self=None):
        note = input("Please enter name of note to update info (without '.txt'): ")
        if is_exist(note):
            note_to_do = NOTEBOOK.read_note(note)
            # text_list = note_to_do["text"]
            # old_name = ""
            # for i, item in enumerate(note_to_do.split('\n'), start=0):
            #     if i == 0:
            #         old_name = item
            new_tag = ''
            for i, item in enumerate(note_to_do.split('\n'), start=0):
                if i == 1:
                    new_tag = item

            for i, item in enumerate(note_to_do.split('\n')[2:], start=0):
                print(i, item)
            new_text = ''

            # for i, item in enumerate(text_list, start=0):
            #     print(i, item)
            text_index = int(input("Please enter index of text that you want to change: "))
            text = input("Please write new text to add instead old to the current note: ")
            # note_to_do["text"][text_index] = new_text
            # return NOTEBOOK.update_note(note, note_to_do)
            for i, item in enumerate(note_to_do.split('\n')[2:], start=0):
                if i == text_index:
                    item = text
                new_text += item + '\n'

            return NOTEBOOK.update_note(note, new_tag, new_text)
        else:
            raise ValueError(f"Note with name '{note}' does not exist in NoteBook.")

        # note = input("Please enter name of note to update info (without '.txt'): ")
        # try:
        #     # if CLINoteBook.find_note_handler(note):
        #     note_to_do = NOTEBOOK.read_note(note)
        #     text_list = note_to_do["text"].split()
        #     for i, item in enumerate(text_list, start=0):
        #         print(i, item)
        #     text_index = int(input("Please enter index of text that you want to change: "))
        #     new_text = input("Please write new text to add instead old to the current note: ")
        #     text_list[text_index] = new_text
        #     new_dict = {}
        #     new_dict['tag'] = note_to_do["tag"]
        #     new_dict['text'] = text_list
        #     return NOTEBOOK.update_note(note, new_dict)
        #
        # except Exception:
        #     raise ValueError(f"Note with name '{note}' does not exist in NoteBook.")

    @command_error_handler
    def delete_tag_handler(self=None):
        note = input("Please enter name of note to update info (without '.txt'): ")
        if is_exist(note):
            note_to_do = NOTEBOOK.read_note(note)
            tag_list = note_to_do.split('\n')[1]
            # tag_list = note_to_do["tag"]
            for i, item in enumerate(tag_list.split(), start=0):
                print(i, item)
            tag_index = int(input("Please enter index of tag that you want to delete: "))
            # note_to_do["tag"].pop(tag_index)
            # return NOTEBOOK.update_note(note, note_to_do)
            # old_name = ""
            # for i, item in enumerate(note_to_do.split('\n'), start=0):
            #     if i == 0:
            #         old_name = item
            new_tag = ''
            for i, item in enumerate(tag_list.split(), start=0):
                if i == tag_index:
                    item = ""
                new_tag += item + ' '
            new_text = ''
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
            # text_list = note_to_do["text"]
            tag_list = note_to_do.split('\n')[1]
            # old_name = ""
            # for i, item in enumerate(note_to_do.split('\n'), start=0):
            #     if i == 0:
            #         old_name = item
            new_tag = ''
            for i, item in enumerate(tag_list.split('\n'), start=0):
                # print(i, item)
                if i == 0:
                    new_tag = item
            new_text = ''
            for i, item in enumerate(note_to_do.split('\n')[2:], start=0):
                print(i, item)
            text_index = int(input("Please enter index of text that you want to delete: "))
            # note_to_do["text"].pop(text_index)
            for i, item in enumerate(note_to_do.split('\n')[2:], start=0):
                if i == text_index:
                    item = ''
                new_text += item + '\n'

            return NOTEBOOK.update_note(note, new_tag, new_text.strip())
            # return NOTEBOOK.update_note(note, note_to_do)
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
                raise SystemExit("\nThank you for using NoteBook.\nSee you later!\n")

            elif command in CLINoteBook.notes_commands_dict.keys():
                handler = CLINoteBook.notes_commands_dict[command]
                answer = handler()
                print(answer)

            # else:
            #     list_comm = []
            #     for k in CLINoteBook.notes_commands_dict.keys():
            #         for item in k.split():
            #             if command in item:
            #                 list_comm.append(k)
            #     if list_comm:
            #         print('You mean commands: ')
            #         print(*list_comm,sep=',')
            #     else:
            #         print("Incorrect input.\nPlease check and enter correct command (or 'help' or 'close').")

            else:
                print("Incorrect input.\nPlease check and enter correct command (or 'help' or 'close').")


if __name__ == '__main__':
    CLINoteBook.run_notes_assistant()

# **Personal Assistant**
GoIT Python7 Group5 Project
## **Description**
Personal Assistant is a usefull programm with CLI-interface that contains Contact Book, Notes and can parse folder.
#### _With Personal Assistant you can:_
- add contacts with phone number, email, address and birthday date to your Contact Book;
- change and delete contacts;
- find contacts by name;
- add notes with tags, change and delete it;
- parse folder by categories.
## **Installation**
```bash
pip install -i https://test.pypi.org/simple/ goit-team5-personal-assistant==1.0.0
```
## **How to work with Personal Assistant**
After you opened Personal Assistant please select category: Contact Book, Notes or Folder Cleaner. After that you can use following commands.
### Commands for Contact Book:
| Command         | Arguments                  | Result                                                                               |
| --------------- | -------------------------- | ------------------------------------------------------------------------------------ |
| help            | -                          | show list of comands                                                                 |
| add contact     | -                          | to add new contact to your phonebook                                                 |
| add phone       | name, phone                | to add phone to existing contact or to create new contact with phone                 |
| add email       | name, email                | to add email to existing contact or to create new contact with email                 |
| add address     | name, address              | to add address to existing contact or to create new contact with address             |
| add birthday    | name, birthday             | to add or change birthday to existing contact or to create new contact with birthday |
| change phone    | name, old phone, new phone | to set up new number for contact with this name                                      |
| change email    | name, old email, new email | to set up new email for contact with this name                                       |
| change address  | name                       | to set up new address for contact with this name                                     |
| delete contact  | name                       | to delete the contact with this name from phonebook (if exist)                       |
| delete phone    | name, phone                | to delete phone from the contact with this name                                      |
| delete email    | name, email                | to delete email from the contact with this name                                      |
| delete address  | name, address              | to delete address from the contact with this name                                    |
| delete birthday | name, birthday             | to delete birthday from the contact with this name                                   |
| nearby birthday | days                       | to show who celebrate birthdays in next days                                         |
| show all        | -                          | to see all contacts in your phonebook                                                |
| find            | name                       | to find contacts that are matching to entered key-letters                            |
| close           | -                          | to finish work and return to main menu                                               |
### Commands for Notes:
| Command        | Result                                                         |
| -------------- | -------------------------------------------------------------- |
| help           | show list of comands                                           |
| add note       | to create new note and save into folder 'notes'                |
| read note      | to open indicated note and read text inside                    |
| delete note    | to delete indicated note from the folder                       |
| find by tag    | to find all notes that are matched with this tag               |
| find by name   | to find notes that are matched with this name                  |
| show all notes | to show list of notes that were saved in folder                |
| add tag        | to include additional tag to existing note                     |
| add text       | to include additional text to existing note                    |
| change tag     | to change existing tag in note (recommend to read note first)  |
| change text    | to change existing text in note (recommend to read note first) |
| delete tag     | to delete existing tag in note (recommend to read note first)  |
| delete text    | to delete existing text in note (recommend to read note first) |
| close          | to finish work and return to main menu                         |
### Commands for Parser Folder:
| Command        | Result                                 |
| -------------- | -------------------------------------- |
| sorting folder | to sort your folder                    |
| close          | to finish work and return to main menu |
---
## About our team
### User Friendly Team
- Team Lead: Andrii Bobanych
- Scrum Master: Valeriia Lytvynova
- Python Developers: Yasha Klymenko, Maryna Zipova
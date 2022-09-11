import sorting_files


def run_sorter():
    def show_command():
        print('Available commands:')
        print('Sorting folder', 'Close', sep='\n')

    while True:
        user_input = input('Enter your command:').lower()
        if user_input == 'Help'.lower():
            show_command()
        elif user_input == 'Sorting folder'.lower():
            out = input('Folder path:')
            sorting_files.main_func(out)
            print('Your folder was successfully sorted! Empty folders were deleted.')
        elif user_input == 'Close'.lower():
            break
        else:
            print('Enter correct command,pls!')
            show_command()
            print('Help')


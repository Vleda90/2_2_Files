def switch_option():
    """Function for switch option"""
    while True:
        option = input('What option of input you want to use:\n'
                '1 - for read information from file\n'
                '2 - for write information by yourself\n'
                'Choose: ').strip()
        if option in ('1', '2'):
            return option
        print("Error! Please enter '1' or '2'.")

def validate_extension(file_name):
    """Function to validate file extension"""
    if not file_name.endswith('.txt'):
        print('Error: Only .txt files are allowed')
        return False
    return True

def file_read(file_name):
    """Function for reading file"""
    if not validate_extension(file_name):
        return
    try:
        with open(file_name, 'r') as f:
            print("\n--- FILE CONTENT ---")
            print(f.read())
    except FileNotFoundError:
        print(f'Error: File {file_name} not found.')

def file_append(file_name, content):
    """Function for appending to the exist file"""
    with open(file_name, 'a') as f:
        f.write(f'Name: {content[0]}, Surname: {content[1]}, Age: {content[2]}\n')
    print(f'Information written to {file_name}')

def file_write(file_name, content):
    """Function for creation the new file or rewrite the existing one"""
    with open(file_name, 'w') as f:
        f.write(f'Name: {content[0]}, Surname: {content[1]}, Age: {content[2]}\n')
    print(f'Information written to {file_name}')

def get_info_from_user():
    """Function for getting information from user"""
    return [
        input('Input user name: '),
        input('Input user surname: '),
        input('Input user age: ')
    ]

def file_exists(file_name):
    """Check if file exists"""
    try:
        with open(file_name, 'r'):
            return True
    except FileNotFoundError:
        return False

"""The main function"""
opt = switch_option()

if opt == '1':
    user_input = input('Enter file name: ')
    file_read(user_input)

elif opt == '2':
    user_list = get_info_from_user()
    print(f'Name: {user_list[0]}, Surname: {user_list[1]}, Age: {user_list[2]}')

    choice = input('Would you like to write information? (y/n): ').strip().lower()
    if choice == 'y':
        user_input = input('Enter file name: ').strip()

        if not validate_extension(user_input):
            print('Error: Only .txt files are allowed')
        else:
            if file_exists(user_input):
                if input('Would you like to REWRITE the file? (y/n): ').strip().lower() == 'y':
                    file_write(user_input, user_list)
                else:
                    file_append(user_input, user_list)
            else:
                file_write(user_input, user_list)
    else:
        print('Thank you!')
else:
    print('Error! Invalid option selected.')

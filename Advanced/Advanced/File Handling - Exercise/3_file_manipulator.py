import os


def create_file(file_name):
    with open(file_name, 'w'):
        pass


def add_content_to_file(file_name, content):
    with open(file_name, 'a') as file:
        file.write(f'{content}\n')


def replace_string_in_file(file_name, old_string, new_string):
    try:

        with open(file_name, 'r') as file:
            content = file.read()
            content = content.replace(old_string, new_string)

        with open(file_name, 'w') as file:
            file.write(content)

    except FileNotFoundError:
        print('An error occurred')


def delete_file(file_name):
    try:
        os.remove(file_name)
    except FileNotFoundError:
        print('An error occurred')


def start_program():

    while True:
        command, *info = input().split('-')
        if command == 'End':
            break
        mapper[command](*info)


mapper = {
    'Create': create_file,
    'Add': add_content_to_file,
    'Replace': replace_string_in_file,
    'Delete': delete_file,
}


start_program()


#### Starting program function: implementation Nº2 ####

# def start_program():
#     while True:
#         command, *info = input().split('-')

#         if command == 'End':
#             break

#         file_name = info[0]

#         if command == 'Create':
#             create_file(file_name)

#         elif command == 'Add':
#             content = info[1]
#             add_content_to_file(file_name, content)

#         elif command == 'Replace':
#             old_string, new_string = info[1:]
#             replace_string_in_file(file_name, old_string, new_string)

#         elif command == 'Delete':
#             delete_file(file_name)

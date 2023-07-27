
#!py

import sys, os
import pyperclip3 as pyperclip
from datetime import datetime
from manage_functions import copy_template, create_class, create_file, rename_class, delete_class, copy_class, test_class


# # initializing variables
# now = datetime.now()
# date = now.strftime('%d-%B-%Y')

# class_name = ''
# template = ''


# def create_class():

#     global class_name
#     global template
#     global date
    
#     # ask user for filename
#     class_name = input('Enter the name of the java class without .java extension: ')
#     template = f'''/**********************************************************
# @Author: Fawaaz Kamali Siddiqui
# @Date: {date}
# @File: {class_name}.java
# @Teacher: A. Carreiro
# @Description: 
# **********************************************************/



# class {class_name} {{ 


#     public static void main(String[]args){{



#     }} // end of main() method
        
        
# }} // end of {class_name}.java
# '''


# def create_file():
    
#     create_class()

#     # copy all content into new file
#     file_write = f'{class_name}.java'
#     with open(file_write, 'w') as write_file:
#         for line in template:
#             write_file.write(line)


# def copy_template():

#     create_class()

#     # copy template to the clipboard
#     pyperclip.copy(template)
#     print('Template has been copied to clipboard.')


# def rename_class():

#     # asking user for file to change
#     old_file = input('Enter the name of the java class you want to rename (without .java): ')
#     new_file = input('Enter the new name of the java class (without .java): ')
#     old_filename = f'{old_file}.java'
#     new_filename = f'{new_file}.java'

#     try:
#         # replacing all instances of old_file and old_filename inside the file
#         with open(old_filename, 'r') as file_read:
#             replacements = file_read.read().replace(old_file, new_file).replace(old_filename, new_filename)
#             # since old_filename is reliant on old_file, we replace old_file first
#             # otherwise, it will remain glitchy

#         with open(old_filename, 'w') as file_write:
#             file_write.write(replacements)

#         # renaming the actual file
#         os.rename(old_filename, new_filename)

#         # removing previous .class files 
#         try:
#             os.remove(f'{old_file}.class')
#         except FileNotFoundError:
#             print('There is no .class file for this')
        
#     except FileNotFoundError:
#         print('This file does not exist in the directory.')
    


COMMANDS = {
    'template': create_file.create_file, 
    'copy-template': copy_template.copy_template, 
    'rename-class': rename_class.rename_class, 
    'delete-class': delete_class.delete_class, 
    'copy-class': copy_class.copy_class, 
    'test-class': test_class.test_class # can be improved
}


if len(sys.argv) < 2:
    print('Usage: py manage.py [command][*args]')
    print(f'Commands available: {COMMANDS.keys()}')
    sys.exit()


command = sys.argv[1] # first command in the terminal line

if command in COMMANDS:
    COMMANDS[command]()
else:
    print('There is no such command.')
    print(f'Commands available: {COMMANDS.keys()}')



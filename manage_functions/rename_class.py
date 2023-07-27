import os
import pyinputplus as pyip

def rename_class():

    # asking user for file to change
    old_file = pyip.inputStr('Enter the name of the java class you want to rename (without .java): ', blockRegexes=[r'\.java'])
    new_file = pyip.inputStr('Enter the new name of the java class (without .java): ', blockRegexes=[r'\.java'])
    old_filename = f'{old_file}.java'
    new_filename = f'{new_file}.java'

    try:
        # replacing all instances of old_file and old_filename inside the file
        with open(old_filename, 'r') as file_read:
            replacements = file_read.read().replace(old_file, new_file).replace(old_filename, new_filename)
            # since old_filename is reliant on old_file, we replace old_file first
            # otherwise, there will be glitches in the program

        with open(old_filename, 'w') as file_write:
            file_write.write(replacements)

        # renaming the actual file
        os.rename(old_filename, new_filename)

        # removing previous .class files 
        try:
            os.remove(f'{old_file}.class')
        except FileNotFoundError:
            print('There is no .class file for this')
        
    except FileNotFoundError:
        print('This file does not exist inside the directory.')
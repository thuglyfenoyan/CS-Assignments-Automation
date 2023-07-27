import pyperclip3 as pyperclip
import pyinputplus as pyip

def copy_class():

    # input section
    filename = pyip.inputStr('Enter the name of the class without the .java extension: ', blockRegexes=[r'\.java'])

    # copy the class content to clipboard
    try: 
        class_content = ''
        with open(f'{filename}.java', 'r') as file_read:
            for line in file_read:
                class_content += line

        pyperclip.copy(class_content)
        print('Class has been copied to clipboard.')

    except FileNotFoundError:
        print(f'There is no {filename}.java file.')

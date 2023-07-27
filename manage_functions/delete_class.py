import os 
import pyinputplus as pyip


def delete_class(): 

    # input section
    class_name = pyip.inputStr('Enter the name of the class you want to delete without the .java extension: ', blockRegexes=[r'\.java'])

    # deleting .java file
    try:
        os.remove(f'{class_name}.java')
    except FileNotFoundError:
        print(f'There is no {class_name}.java file')

    # deleting .class file if it exists
    try: 
        os.remove(f'{class_name}.class')
    except FileNotFoundError:
        print(f'There is no {class_name}.class file')

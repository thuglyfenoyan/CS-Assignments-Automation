from . import create_class
import pyperclip3 as pyperclip

def copy_template():

    create_class.create_class()

    # copy template to the clipboard
    pyperclip.copy(create_class.template)
    print('Template has been copied to clipboard.')

from . import create_class


def create_file():
    
    create_class.create_class()

    # copy all content into new file
    file_write = f'{create_class.class_name}.java'
    with open(file_write, 'w') as write_file:
        for line in create_class.template:
            write_file.write(line)
import os 


def test_class() :

    num_test = 0 # listing how many files in directory are test java files
    for file in os.listdir():
        if (file.startswith("Test") or file.startswith("test")) and file.endswith(".java"):
            num_test+=1


    template = f'''class Test{num_test+1} {{

    public static void main(String[]args) {{



    }}

}}'''


    # writing template to new test file
    with open(f'Test{num_test+1}.java', 'w') as file_write:
        for line in template:
            file_write.write(line)


import os


def rename_files(path):
    files = os.listdir(path)
    table = str.maketrans(dict.fromkeys('0123456789'))
    saved_path = os.getcwd()

    os.chdir(path)
    for file in files:
        new_file = file.translate(table)
        print("Old name file: {}".format(file))
        print("New name file: {}".format(new_file))
        os.rename(file, new_file)

    os.chdir(saved_path)

if __name__ == '__main__':
    rename_files("helloworld")

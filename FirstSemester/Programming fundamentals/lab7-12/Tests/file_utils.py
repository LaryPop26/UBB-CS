import shutil

def clear_file(file):
    with open(file, 'w') as f:
        pass

def copy_content(source, destination):
    shutil.copy(source, destination)

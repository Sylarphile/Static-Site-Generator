import shutil, os

def copy_to_public(source, destination, files):
    if len(files) < 1:
        return
    first_file = files[0]
    file_path = os.path.join(source, first_file)
    if os.path.isfile(file_path):
        #Debug Logging
        #print(f"Copying file: {file_path} to {destination}")
        shutil.copy(file_path, destination)
    elif os.path.isdir(file_path):
        dir_list = os.listdir(file_path)
        new_dir = os.path.join(destination, first_file)
        #Debug Logging
        #print(f"Creating directory: {new_dir}")
        os.mkdir(new_dir)
        copy_to_public(file_path, new_dir, dir_list)

    copy_to_public(source,destination, files[1:])
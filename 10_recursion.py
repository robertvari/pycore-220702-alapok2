import os


def get_all_files(root_folder, file_list):
    folder_content = os.listdir(root_folder)

    # collect files and subfolders
    subfolders = []
    for i in folder_content:
        full_path = os.path.join(root_folder, i)

        if os.path.isfile(full_path):
            file_list.append(full_path)
        else:
            if os.path.isdir(full_path):
                subfolders.append(full_path)

    if subfolders:
        for folder in subfolders:
            get_all_files(folder, file_list)


root_folder = r"C:\Work\_PythonSuli\pycore-220702\Alapok2"
file_list = []
get_all_files(root_folder, file_list)

for i in file_list:
    print(i)
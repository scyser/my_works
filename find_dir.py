# show all dirs recusively or not

import os

def get_elements(path, flag_recursive=False):
    files_list = []
    for dirpath, dirnames, filenames in os.walk(path):
        for filename in filenames:
            files_list.append({"name": filename, "type": "file"})
        for dirname in dirnames:
            if flag_recursive:
                new_path = os.path.join(dirpath, dirname)
                files_list.append({"name": dirname, "type": "folder", "subelements": get_elements(new_path, True)})
            else:
                files_list.append({"name": dirname, "type": "folder"})
        break
    return files_list

print(get_elements("E:/Test", True))


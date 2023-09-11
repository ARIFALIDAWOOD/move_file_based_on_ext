import os
import shutil
import glob
from datetime import datetime

cur_path = os.path.dirname(os.path.abspath(__file__))
down_path = os.path.join("C:\\", "Users", os.getlogin(), "Downloads") if input("DOWNLOAD? (else Documents) ['Y', ' '] :") in ['Y', ' '] else os.path.join("C:\\", "Users", os.getlogin(), "Documents")

def getExtensions():
    ext_list = []
    list_of_files = glob.glob(os.path.join(down_path, '*.*'))
    for lt in list_of_files:
        if os.path.isdir(lt):
            continue
        ext = os.path.splitext(lt)[1].lower()[1:]
        if ext not in ext_list:
            ext_list.append(ext)
    return ext_list

def makeParent(ext):
    list_of_files_parent = glob.glob(os.path.join(down_path, ext.upper()+"*"))
    path_of_parent = os.path.join(down_path, ext.upper())
    if not os.path.exists(path_of_parent):
        os.makedirs(path_of_parent)
    print("PARENT NAME: ", path_of_parent)  
    for file_name_p in list_of_files_parent:
        if "~$" not in file_name_p:
            print(file_name_p)
            # breakpoint()
            shutil.move(os.path.join(down_path, file_name_p), path_of_parent)

for ext in getExtensions():
    if ext.upper() == "EXE":
        continue
    list_of_files = glob.glob(os.path.join(down_path, '*.' + ext))
    path_of = os.path.join(down_path, ext.upper() + " " + str(datetime.now())[:10].replace(":", "_"))

    if not os.path.exists(path_of):
        try:
            os.makedirs(path_of)
        except:
            pass
    
    for file_name in list_of_files:
        if "~$" not in file_name:
            print(file_name)
            try:
                # breakpoint()
                shutil.move(os.path.join(down_path, file_name), path_of)
            except Exception as e:
                print("Error:", str(e))

    makeParent(ext)

getExtensions()

# Changes to make: if subdirectory exists, move to that subdirectory
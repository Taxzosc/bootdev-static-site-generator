import os
import shutil


def copy_static(src_path: str | os.PathLike, destination: str | os.PathLike):
    if os.path.exists(src_path) != True:
        raise ValueError("src_path not valid path")
    
    if os.path.exists(destination): #checks if destination exists, if it does, delete. destination should only be a directory
        shutil.rmtree(destination)
    os.mkdir(destination)

    for item in os.listdir(src_path): #returns a list of the files/directories in src_path. just names
        item_path = os.path.join(src_path, item)
        
        if os.path.isdir(item_path) == True:
            new_destination = os.path.join(destination,item)
            copy_static(item_path, new_destination) #goes into that directory
        
        if os.path.isfile(item_path) == True:
            shutil.copy(item_path, destination)
    return


#the solution separates the logic, where copy_static only ever copies and recurses,
# while the deletion of the destination happends in main, before ever calling copy_static.
# both work, but having a deletion section in the function makes it fragile?(according to boots)
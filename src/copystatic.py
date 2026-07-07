import os
import shutil
from block_markdown import markdown_to_blocks, markdown_to_html_node


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
#also, my naming is not that clear. item path. solution uses from path, dest path. makes it more clear. could also name destination path as generated content path maybe?


def extract_title(markdown: str) -> str:
    blocks = markdown_to_blocks(markdown)
    for text in blocks:
        if text.startswith("# "):
            return text[2:].strip()
    raise ValueError("markdown contains no h1 header")


def generate_page(from_path: str | os.PathLike, template_path: str | os.PathLike, dest_path: str | os.PathLike):
    print(f"Generating page from {from_path} to {dest_path}, using {template_path}")

    markdown = ""
    template = ""
    html = markdown_to_html_node(markdown)
    title = extract_title(markdown)

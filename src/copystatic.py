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
    # what is from_path going to be? is it the directory or is it supposed to be the md file itself? "read the md file at frompath"
    print(f"Generating page from {from_path} to {dest_path}, using {template_path}")
    md_file = from_path
    markdown = ""
    # if os.path.isdir(md_file): #this is not needed as from_path should be pointing directly at the markdown file itself.
    #     content_files = os.listdir(md_file)
    #     for file in content_files: #doing this because i assume content can contain other things than the md file
    #         if file[-3:] == ".md":
    #             md_file = os.path.join(md_file,file)
    #             break
    open_md = open(md_file)
    markdown = open_md.read()
    open_md.close()

    html_node = markdown_to_html_node(markdown)
    html = html_node.to_html()
    title = extract_title(markdown)

    open_template = open(template_path)
    template = open_template.read() #copies template content to variable
    open_template.close()
    swapped_title_content = template.replace("{{ Title }}", title).replace("{{ Content }}", html)

    destination_dir_path = os.path.dirname(dest_path) #this snippet is copied from the solution after talking to boots to understand it.
    if destination_dir_path != "":
        os.makedirs(destination_dir_path, exist_ok=True)
    
    new_file_name = dest_path
    new_file = open(new_file_name, mode='w') #creates and opens for writing
    new_file.write(swapped_title_content)
    new_file.close()



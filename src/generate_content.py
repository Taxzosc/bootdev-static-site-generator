import os
from block_markdown import markdown_to_blocks, markdown_to_html_node
from pathlib import Path

def extract_title(markdown: str) -> str:
    blocks = markdown_to_blocks(markdown)
    for text in blocks:
        if text.startswith("# "):
            return text[2:].strip()
    raise ValueError("markdown contains no h1 header")

def generate_page(from_path: str | os.PathLike, template_path: str | os.PathLike, dest_path: str | os.PathLike): 
    # what is from_path going to be? is it the directory or is it supposed to be the md file itself? "read the md file at frompath"
    print(f"Generating page from {from_path} to {dest_path}, using {template_path}")
    # if os.path.isdir(md_file): #this is not needed as from_path should be pointing directly at the markdown file itself.
    #     content_files = os.listdir(md_file)
    #     for file in content_files: #doing this because i assume content can contain other things than the md file
    #         if file[-3:] == ".md":
    #             md_file = os.path.join(md_file,file)
    #             break
    open_md = open(from_path)
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



def generate_pages_recursive(dir_path_content: str | os.PathLike, template_path: str | os.PathLike, dest_dir_path: str | os.PathLike):
    if len(os.listdir(dir_path_content)) == 0: #redundant as if a loop is fed an empty list, it does not execute and the function returns none
        return
        # raise ValueError("directory empty")
    for item in os.listdir(dir_path_content):
        item_path = os.path.join(dir_path_content,item)
        destination_item_path = os.path.join(dest_dir_path, item)
        
        if os.path.isfile(item_path) and item[-3:] == ".md":
            # md_destination = os.path.join(dest_dir_path, "index.html")  #solution uses Path(dest_path).with_suffix(".html") to avoid every file be named "index.html".
            #aka it creates a path object of the path to the html file.
            #what if there is a md file that is not supposed to be named index
            md_destination = Path(destination_item_path).with_suffix(".html") #copied after seeing solution and chatting with boots. the above solution works for this project, assuming every md is index.
            print(f"inside recursive : using generating page using {item_path}, {template_path}, {md_destination}")
            generate_page(item_path, template_path, md_destination)
        if os.path.isdir(item_path):
            print(f"recursing down to {item_path}")
            generate_pages_recursive(item_path, template_path, destination_item_path)
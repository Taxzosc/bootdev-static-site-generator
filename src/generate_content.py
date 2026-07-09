import os
from block_markdown import markdown_to_blocks, markdown_to_html_node

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
import os
from textnode import TextNode, TextType
from copystatic import copy_static
from generate_content import generate_page

static_path = "./static"
destination_path = "./public"
content_path = "./content"
template_path = "./template.html"

def main() -> None:
    copy_static(static_path, destination_path)
    # generate_page("./content","./template.html","./public") #changed it to reflect what i am learning from the solution.
    generate_page(
        os.path.join(content_path, "index.md"),
        template_path,
        os.path.join(destination_path, "index.html")
    )
main()
import os
from textnode import TextNode, TextType
from copystatic import copy_static
from generate_content import generate_pages_recursive
import sys

# basepath = sys.argv #after checking with boots, i got a better solution
# if len(basepath) < 2:
#     basepath.append("/")
if len(sys.argv) > 1:
    basepath = sys.argv[1]
else:
    basepath = "/"
static_path = "./static"
destination_path = "./docs"
content_path = "./content"
template_path = "./template.html"
print(basepath)
def main() -> None:
    print(f"copying from static : {static_path} to destination : {destination_path}")
    copy_static(static_path, destination_path)
    # generate_page("./content","./template.html","./public") #changed it to reflect what i am learning from the solution.

    print("in main using generate_pages_recursive")
    generate_pages_recursive(content_path, template_path, destination_path, basepath)
    
main()
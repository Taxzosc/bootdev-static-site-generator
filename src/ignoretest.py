import re
from inline_markdown import extract_markdown_images, extract_markdown_links,split_nodes_delimiter,split_nodes_image,split_nodes_link
from textnode import *
from block_markdown import *
from htmlnode import *
# testhis = {
# "href": "https://www.google.com",
# "target": "_blank",
# }
# newstring = ""
# for key, value in testhis.items():
# newstring=newstring + f'{key}="{value}"'
# print(newstring)

# This is a test
# string  = "This is text with a `code block` word"
# print(string.split("`"))
# print(0%2)


# text = "This is text with a link [to boot dev](https://www.boot.dev)"# and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
# result = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
# print(result)
# print(text)
# print(type(result))
# for i in result:
#     print(type(i))

# text = "this is some text [to boot dev](https://www.boot.dev) with this following"
# split_text = text.split("(")
# split_again = split_text.split(")")
# print(split_again)

# text = "this is text ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg) more text"
# split_text = re.split(r"!\[([^\[\]]*\]\([^\(\)]*)\)", text)
# print(split_text)  #output: ['this is text ', 'obi wan](https://i.imgur.com/fJRm4Vk.jpeg', ' more text']

# text = "This is text with a link [to boot dev](https://www.boot.dev) text, with more This is text with a link [to boot dev](https://www.boot.dev)[to boot dev](https://www.boot.dev) text"
# split_text = re.split(r"(?<!!)\[([^\[\]]*\]\([^\(\)]*)\)", text)
# print(split_text) #output ['This is text with a link ', 'to boot dev](https://www.boot.dev', ' text']

# textimage = "![obi wan](https://i.imgur.com/fJRm4Vk.jpeg) test this ![mobi](https://i.pimgur.com/fJRm4Vk.jpeg) meme ![mobi](htips://i.pimgur.com/fJRm4Vk.jpeg) test"
# images = extract_markdown_images(textimage)
# print(textimage)
# new_list = []
# for image in images:
#     split_text = textimage.split(f"![{image[0]}]({image[1]})",1)
#     textimage = split_text[1]
#     if split_text[0] != "":
#         new_list.append(f"{split_text[0]}")
#     new_list.append(f"{image[0]}, {image[1]}")
#     print(split_text)
# if textimage != "":
#     new_list.append(textimage)
# print(f"new list is {new_list}")

# text = [TextNode("![bobi wan image](htrtps://i.imgur.com/fJRm4Vk.jpeg) This is _text_ with an **bold** word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)", TextType.TEXT)]
# newlist = []
# text = split_nodes_delimiter(text, "**",TextType.BOLD)
# print(len(text))
# text = split_nodes_delimiter(text, "_", TextType.ITALIC)
# print(len(text))
# text = split_nodes_delimiter(text, "`", TextType.CODE)
# print(len(text))
# text = split_nodes_image(text)
# print(len(text))
# text = split_nodes_link(text)
# print(len(text))
# print(text)

# text = """
#   This is **bolded** paragraph


  

#  This is another paragraph with _italic_ text and `code` here
# This is the same paragraph on a new line  

 
# - This is a list
# - with items
# """

# markdowntext = text.split("\n\n")
# print(markdowntext)
# newlist = []
# for i in markdowntext:
#     if i == "":
#         continue
#     newlist.append(i.strip())

# # print(newlist)

# block = """
# 1. first
# 2. second
# 3. third
# 4. fourth
# 5. fifth
# 6. sixth
# 7. seventh
# 8. eighth
# 9. nineth
# 10. tenth
# """
# def check_valid_ordered_list(text):
#     newblock = block.strip()
#     splitblock = newblock.split("\n")
#     count = 1
#     for slab in splitblock:
#         if not slab.startswith(f"{count}. "):
#             return False
#         count += 1
#     return True
# is_valid = check_valid_ordered_list(block)
# if is_valid:
#     print("ordered list")
# else:
#     print("do nothing, let the next if statement check")
# count = "#"
# for i in range(0,10):
#     print(count)
#     count += "#"
# markdown = """```
# this is a code block
# ```"""
# newlist = markdown_to_blocks(markdown)
# print(newlist)
# text = "#### "
# print(text[0:2])

# text = "###### headers are we###ird ###"
# text = """```
# this is code
# and more code
# ```"""
# stripped = text.lstrip("# ")
# print(stripped)
# print(text)
# count = len(text) - len(stripped) - 1
# this_typ = (stripped, count)
# print(type(this_typ))
# print(this_typ[0])

markdown = """
- this is unordered
- list
- yeah this is one
"""
nodes = []
# print(repr(html))
# newtxt = text.strip("```\n")
# print(newtxt)
# block = "### third header"
nodes = []
# header_string_and_hash_count = helper_strip_and_count_header(block)  #tuple with string and # count.
# html_node = helper_text_to_htmlnode_children(header_string_and_hash_count[0])
# nodes.append(ParentNode(f"h{header_string_and_hash_count[1]}", html_node))
blocks = markdown_to_blocks(markdown)
for block in blocks:
    nodes.append(ParentNode("ul", helper_unordered_list(markdown)))
parent = ParentNode("div", nodes)
# print(nodes)
html = parent.to_html()
print(repr(html))
import re
from inline_markdown import extract_markdown_images, extract_markdown_links,split_nodes_delimiter,split_nodes_image,split_nodes_link
from textnode import TextNode,TextType
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

text = "``` headingstuffs```"
print(text[0:2])
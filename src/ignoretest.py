import re
from inline_markdown import extract_markdown_images, extract_markdown_links
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

textimage = "![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
split_text = re.split(r"!\[([^\[\]]*\]\([^\(\)]*)\)", textimage)
images_urls = extract_markdown_images(textimage)
print(images_urls)
print(split_text)
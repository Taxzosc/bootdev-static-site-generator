import re

# testhis = {
# "href": "https://www.google.com",
# "target": "_blank",
# }
# newstring = ""
# for key, value in testhis.items():
# newstring=newstring + f'{key}="{value}"'
# print(newstring)

#This is a test
# string  = "This is text with a `code block` word"
# print(string.split("`"))
# print(0%2)


text = "This is text with a link [to boot dev](https://www.boot.dev)"# and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
result = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
print(result)
print(type(result))
for i in result:
    print(type(i))
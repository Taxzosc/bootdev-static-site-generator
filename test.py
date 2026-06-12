# testhis = {
# "href": "https://www.google.com",
# "target": "_blank",
# }
# newstring = ""
# for key, value in testhis.items():
# newstring=newstring + f'{key}="{value}"'
# print(newstring)

#This is a test
string  = "This is text with a `code block` word, and more `code text` to check, `codeblock``anotherblock`"
print(string.split("`"))
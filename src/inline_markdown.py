import re
from textnode import TextNode, TextType

def split_nodes_delimiter(
        old_nodes: list[TextNode],
        delimiter: str,
        text_type: TextType) -> list[TextNode]:
    new_text = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            #this assumes the node text only contains a markdown string, aka **boldtext** or something like it.
            new_text.append(node)
        # if delimiter not in node.text: #assumes node is a TEXT node, but did not find given delimiter.
        #     raise ValueError(f"{delimiter} not found in text")
        #i read the task wrong here, its supposed to be MATCHING delimiter, not if theres no delimiter/unknown delimiter
        #which i got to test when i added the test for both bold and italic in 1 test.
        
        if node.text_type == TextType.TEXT:
            split_text = node.text.split(delimiter)
            if len(split_text) % 2 == 0: #added after i added test bold_and_italic, and seen the solution
                raise ValueError("Matching Delimiter not found")
            index = 0
            for i in split_text:
                if i == "": #added after copy multiword test.
                    index += 1
                    continue
                if index % 2 != 0: #if index is odd, it is not text, it must be the delimited text, extend to list as new node, loop back to top
                    new_text.append(TextNode(i,text_type))
                if index % 2 == 0: #if index is even, it must be text, extend text tot list as new node, loop back to top
                    new_text.append(TextNode(i,TextType.TEXT))
                index += 1
                #note the solution has a bit shorter code solution for this. this still works
    return new_text




def extract_markdown_images(text: str) -> list[tuple[str,str]]:
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)",text) #old \[(.*?)\]\((.*?)\)
#i was confused on why the solution regex was so different from mine, since mine works, but mine "finds markdown-style things" while solution finds images and links spesifically.
#im not going to copy the solution, and rather find the correct regex myself.
#update didnt figure it out myself, but went through the given in tips to learn how it works.
#the current regex finds the section that has a !followed by whatever is inside [] and () except the []() themselves in 2 capture groups
def extract_markdown_links(text: str) -> list[tuple[str,str]]:
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)",text)#old \[(.*?)\]\((.*?)\)
#this does the same as above, except it uses (?<!!) to exclude any markdown []() with a ! infront of it, making that a link

# def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:  #i have decided to depreciate this, write it anew.keeping for record keeping as this is study not final/real world product
#     new_text = []
#     for node in old_nodes:
#         if node.text_type != TextType.TEXT:
#             new_text.append(node)
#             continue
#         list_index = 0
#         split_text = re.split(r"!\[([^\[\]]*\]\([^\(\)]*)\)", node.text) #splits the text at the image, we dont care about the image itself just index
#         images_urls = extract_markdown_images(node.text) #does not alter original
#         for i in range(len(split_text)):
#             if split_text[i] == "":
#                 continue
#             if i % 2 != 0: #this means image
#                 new_text.append(TextNode(images_urls[list_index][0], TextType.IMAGE, images_urls[list_index][1]))
#                 list_index +=1
#             if i % 2 == 0:
#                 new_text.append(TextNode(split_text[i], TextType.TEXT))
#     return new_text




# def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
#     new_text = []
#     for node in old_nodes:
#         if node.text_type != TextType.TEXT:
#             new_text.append(node)
#             continue
#         list_index = 0
#         split_text = re.split(r"(?<!!)\[([^\[\]]*\]\([^\(\)]*)\)", node.text) #splits the text at the link, we dont care about the link itself just index
#         alt_text_urls = extract_markdown_links(node.text) #does not alter original
#         for i in range(len(split_text)):
#             if split_text[i] == "":
#                 continue
#             if i % 2 != 0: #this means link
#                 new_text.append(TextNode(alt_text_urls[list_index][0], TextType.LINK, alt_text_urls[list_index][1]))
#                 list_index +=1
#             if i % 2 == 0:
#                 new_text.append(TextNode(split_text[i], TextType.TEXT))
#     return new_text
#after chatting with boots and seeing the solution reference, and the tips given in the solution,
# i now understand a bit more of why my re.split solution has some very likely edge cases in real use.
#  its: what happends if the link/imagelink contains elements that interfer with the lookup. like an early ) or somethign else
# i will now rewrite my solutions while knowing of the split given in the tips.
# 
#  sections = original_text.split(f"![{image_alt}]({image_link})", 1)
def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    node_list = []
    for node in old_nodes:
        original_text = node.text
        if node.text_type != TextType.TEXT:
            node_list.append(node)
            continue
        
        images = extract_markdown_images(original_text)
        if len(images) == 0:
            node_list.append(node)
            continue
        for image in images:
            sections = original_text.split(f"![{image[0]}]({image[1]})", 1)
            if len(sections) != 2:
                raise ValueError("not valid markdown, something wrong the closing on images.")
            original_text = sections[1]
            if sections[0] != "":
                node_list.append(TextNode(sections[0], TextType.TEXT))
            node_list.append(TextNode(image[0], TextType.IMAGE, image[1]))
        if original_text != "":
            node_list.append(TextNode(original_text, TextType.TEXT))
    return node_list
            


def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    node_list = []
    for node in old_nodes:
        original_text = node.text
        if node.text_type != TextType.TEXT:
            node_list.append(node)
            continue
        
        links = extract_markdown_links(original_text)
        if len(links) == 0:
            node_list.append(node)
            continue
        for link in links:
            sections = original_text.split(f"[{link[0]}]({link[1]})", 1)
            if len(sections) != 2:
                raise ValueError("not valid markdown, something wrong the closing on links.")
            original_text = sections[1]
            if sections[0] != "":
                node_list.append(TextNode(sections[0], TextType.TEXT))
            node_list.append(TextNode(link[0], TextType.LINK, link[1]))
        if original_text != "":
            node_list.append(TextNode(original_text, TextType.TEXT))
    return node_list

def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.TEXT)]
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes
#CRITICAL ERROR, i made my tests where whats given to the function is a textnode, instead of text. in the solution 
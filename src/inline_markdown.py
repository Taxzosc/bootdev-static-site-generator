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
def extract_markdown_links(text: str) -> list[tuple[str,str]]:
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)",text)#old \[(.*?)\]\((.*?)\)
from enum import Enum
from htmlnode import LeafNode

class TextType(Enum):
    TEXT = "text"  #swapped from plain to text, to be more in line with the assignments notes
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode():
    def __init__(self, text: str, text_type: TextType, url: str | None = None) -> None:
        self.text = text
        self.text_type = text_type
        self.url = url
    
    def __eq__(self, other: "TextNode") ->  bool:
        if isinstance(other, TextNode):
            if (other.text == self.text) and (other.text_type == self.text_type) and (other.url == self.url):
                return True
                    
    def __repr__(self) -> str:
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"

def text_node_to_html_node(text_node: TextNode) -> LeafNode:
    # if text_node.text_type not in TextType:  #changing this to match the solution. while this will work, it can cause errors.
    #     raise Exception("This is not a valid Text Type") #its better and cleaner to just have it at the end, because if none of the if statements gets hit, it must be a wrong input.
    if text_node.text_type.value == "text":  #all of the If statements here can be written as "if text_node.text_type == TextType.Type(TEXT,BOLD etc)"
        return LeafNode(None, text_node.text)  #removing the f-strings as this can cause an error if text_node.url is none, also redundant and not needed
    if text_node.text_type.value == "bold":
        return LeafNode("b", text_node.text)    #removing the f-strings as this can cause an error if text_node.url is none, also redundant and not needed
    if text_node.text_type.value == "italic":
        return LeafNode("i", text_node.text)    #removing the f-strings as this can cause an error if text_node.url is none, also redundant and not needed
    if text_node.text_type.value == "code":
        return LeafNode("code", text_node.text) #removing the f-strings as this can cause an error if text_node.url is none, also redundant and not needed
    if text_node.text_type.value == "link":
        return LeafNode("a", f"{text_node.text}", {"href":text_node.url})
    if text_node.text_type.value == "image":
        return LeafNode("img", "", {"src":text_node.url, "alt": text_node.text})
    raise ValueError(f"invalid text type: {text_node.text_type}") #copied from solution, see reasoning above.
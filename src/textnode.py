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
    if text_node.text_type not in TextType:
        raise Exception("This is not a valid Text Type")
    if text_node.text_type.value == "text":
        return LeafNode(None, f"{text_node.text}")
    if text_node.text_type.value == "bold":
        return LeafNode("b", f"{text_node.text}")
    if text_node.text_type.value == "italic":
        return LeafNode("i", f"{text_node.text}")
    if text_node.text_type.value == "code":
        return LeafNode("code", f"{text_node.text}")
    if text_node.text_type.value == "link":
        return LeafNode("a", f"{text_node.text}", {"href":f"{text_node.url}"})
    if text_node.text_type.value == "image":
        return LeafNode("img", "", {"src":f"{text_node.url}", "alt": text_node.text})
from enum import Enum
from htmlnode import HTMLNode, ParentNode, LeafNode
from inline_markdown import text_to_textnodes
from textnode import text_node_to_html_node,TextNode, TextType

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list" #spelling error "unDorned_list"
    ORDERED_LIST = "ordered_list"

def helper_check_valid_headings(text: str) -> bool: 
    block = text.strip()
    # split_block = block.split("\n") #this check is wrong. there should never be a multiline heading.
    # count = "#"
    # for line in split_block:
    #     if not line.startswith(f"{count} "):
    #         return False
    #     count += "#"
    # return True
    if block.startswith(("# ","## ","### ","#### ","##### ","##### ","###### ")):
        return True

def helper_check_valid_quote(text: str) -> bool:
    block = text.strip()
    split_block = block.split("\n")
    for line in split_block:
        if not line.startswith(">"):
            return False
    return True

def helper_check_valid_unordered_list(text: str) -> bool:
    block = text.strip()
    split_block = block.split("\n")
    for line in split_block:
        if not line.startswith("- "):
            return False
    return True

def helper_check_valid_ordered_list(text: str) -> bool:
    block = text.strip()
    split_block = block.split("\n")
    count = 1
    for line in split_block:
        if not line.startswith(f"{count}. "):
            return False
        count += 1
    return True

def helper_text_to_htmlnode_children(text: str) -> list[HTMLNode]: #takes a block, takes whatever is inside it, and turns it into htmlnodes
    text_nodes = text_to_textnodes(text)
    new_nodes = []
    for node in text_nodes:
        current = text_node_to_html_node(node)
        new_nodes.append(current)
    return new_nodes

def helper_strip_and_count_header(text: str) -> tuple[str, int]:
    stripped_text = text.lstrip("# ")
    hashes_count = len(text) - len(stripped_text) -1
    return (stripped_text, hashes_count)

def helper_strip_code_backtips(text:str) -> str:
    stripped_code = text[len("```\n"):-len("```")] #saves all text except the first 4 characters and the last 3. keeping the newline at the end is important according to boots
    return stripped_code

def helper_strip_quote(text: str) -> str:
    stripped_quote = text.lstrip("> ")
    return stripped_quote

def helper_strip_paragraph(text: str) -> str:
    paragraph_no_newlines = text.replace("\n", " ")
    return paragraph_no_newlines

def helper_unordered_list(text: str) -> list["HTMLNode"]:
    split_text = text.split("- ")
    nodes = []
    for item in split_text:
        if item == "\n":
            continue
        print("meme")
        nodes.append(ParentNode("li", helper_text_to_htmlnode_children(item[:-len("\n")])))
    return nodes

def markdown_to_blocks(markdown):
    split_markdown = markdown.split("\n\n")
    block_list = []
    for text in split_markdown:
        if text == "":
            continue
        block_list.append(text.strip())
    return block_list

def block_to_block_type(block: str) -> BlockType:
    if helper_check_valid_headings(block):
        return BlockType.HEADING
    if len(block) > 1 and block[0:4] == "```\n" and block[-3:] == "```":  #this does not check if its a multiline code, as in, has mutliple lines, adding a len check like in the solution. 
        return BlockType.CODE
    if helper_check_valid_quote(block):
        return BlockType.QUOTE
    if helper_check_valid_unordered_list(block):
        return BlockType.UNORDERED_LIST
    if helper_check_valid_ordered_list(block):
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH


def markdown_to_html_node(markdown: str) -> HTMLNode:
    nodes = []
    blocks = markdown_to_blocks(markdown)

    for block in blocks:
        block_type = block_to_block_type(block)
        if block_type == BlockType.HEADING:
            header_string_and_hash_count = helper_strip_and_count_header(block)  #tuple with string and # count.
            html_node = helper_text_to_htmlnode_children(header_string_and_hash_count[0])
            nodes.append(ParentNode(f"h{header_string_and_hash_count[1]}", html_node))
        
        if block_type == BlockType.CODE:
            text_node = TextNode(helper_strip_code_backtips(block), TextType.CODE)
            html_node = [text_node_to_html_node(text_node)]
            nodes.append(ParentNode("pre", html_node))
        
        if block_type == BlockType.QUOTE:
            text = helper_strip_quote(block)
            html_node = helper_text_to_htmlnode_children(text)
            nodes.append(ParentNode("blockquote",html_node))
        if block_type == BlockType.UNORDERED_LIST:
            nodes.append(ParentNode("ul", helper_unordered_list(block)))
        if block_type == BlockType.ORDERED_LIST:
            pass
        if block_type == BlockType.PARAGRAPH:
            text = helper_strip_paragraph(block)
            html_node = helper_text_to_htmlnode_children(text)
            nodes.append(ParentNode("p", html_node))
    return ParentNode("div", nodes)
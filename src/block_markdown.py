from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list" #spelling error "unDorned_list"
    ORDERED_LIST = "ordered_list"

def check_valid_headings(text: str) -> bool: 
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

def check_valid_quote(text: str) -> bool:
    block = text.strip()
    split_block = block.split("\n")
    for line in split_block:
        if not line.startswith(">"):
            return False
    return True

def check_valid_unordered_list(text: str) -> bool:
    block = text.strip()
    split_block = block.split("\n")
    for line in split_block:
        if not line.startswith("- "):
            return False
    return True


def check_valid_ordered_list(text: str) -> bool:
    block = text.strip()
    split_block = block.split("\n")
    count = 1
    for line in split_block:
        if not line.startswith(f"{count}. "):
            return False
        count += 1
    return True


def markdown_to_blocks(markdown):
    split_markdown = markdown.split("\n\n")
    block_list = []
    for text in split_markdown:
        if text == "":
            continue
        block_list.append(text.strip())
    return block_list

def block_to_block_type(block: str) -> BlockType:
    if check_valid_headings(block):
        return BlockType.HEADING
    if len(block) > 1 and block[0:4] == "```\n" and block[-3:] == "```":  #this does not check if its a multiline code, as in, has mutliple lines, adding a len check like in the solution. 
        return BlockType.CODE
    if check_valid_quote(block):
        return BlockType.QUOTE
    if check_valid_unordered_list(block):
        return BlockType.UNORDERED_LIST
    if check_valid_ordered_list(block):
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH
from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "undordered_list"
    ORDERED_LIST = "ordered_list"

def check_valid_headings(text: str) -> bool:
    block = text.strip()
    split_block = block.split("\n")
    count = "#"
    for line in split_block:
        if not line.startswith(f"{count} "):
            return False
        count += "#"
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
    if block[0:4] == "```\n" and block[-3:] == "```":
        return BlockType.CODE
    if block[0] == ">":
        return BlockType.QUOTE
    if block[0:2] == "- ":
        return BlockType.UNORDERED_LIST
    if check_valid_ordered_list(block):
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH
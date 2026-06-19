from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "undordered_list"
    ORDERED_LIST = "ordered_list"

def markdown_to_blocks(markdown):
    split_markdown = markdown.split("\n\n")
    block_list = []
    for text in split_markdown:
        if text == "":
            continue
        block_list.append(text.strip())
    return block_list

def block_to_block_type(block: str) -> BlockType:
    if "# " in block[0:7]:
        return BlockType.HEADING
    if block[0:4] == "``` " and block[-3:] == "```":
        return BlockType.CODE
    if block[0:2] == "> ":
        return BlockType.QUOTE
    if block[0:2] == "- ":
        return BlockType.UNORDERED_LIST
    pass
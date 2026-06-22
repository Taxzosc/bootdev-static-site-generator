import unittest
from block_markdown import BlockType, markdown_to_blocks, block_to_block_type

class test_markdown_to_blocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_markdown_to_blocks_leading_trailing_whitespace(self):
        md = """
   This is **bolded** paragraph   

  This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line  

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_markdown_to_blocks_extra_newlines(self):
        md = """
This is **bolded** paragraph


This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line


- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

class test_block_to_blocktype(unittest.TestCase):
    def test_headings_valid(self):
        heading = "# heading"
        typeblock = block_to_block_type(heading)
        self.assertEqual(typeblock, BlockType.HEADING)

    def test_headings_not_valid(self):
        heading = "#heading"
        typeblock = block_to_block_type(heading)
        self.assertEqual(typeblock, BlockType.PARAGRAPH)

    def test_multiline_code_valid(self):
        code = """```
        this is a code block
        with lots of code
        total haxor
        ```"""

        typeblock = block_to_block_type(code)
        self.assertEqual(typeblock, BlockType.CODE)
    
    def test_multiline_code_not_valid(self):
        code = """```this is a code block
        with lots of code
        total haxor
        ```"""

        typeblock = block_to_block_type(code)
        self.assertEqual(typeblock, BlockType.PARAGRAPH)
    
    def test_quote_block_valid(self):
        quote = """
> this is a quote
>this is also a quote
"""
        typeblock = block_to_block_type(quote)
        self.assertEqual(typeblock, BlockType.QUOTE)

    def test_quote_block_not_valid(self):
        quote = """
> this is a quote
>this is also a quote
<>this is not a valid quote
"""
        typeblock = block_to_block_type(quote)
        self.assertEqual(typeblock, BlockType.PARAGRAPH)

    def test_unordered_list_valid(self):
        unordered_list = """
- line 1
- line 2
- line 3
"""
        typeblock = block_to_block_type(unordered_list)
        self.assertEqual(typeblock, BlockType.UNORDERED_LIST)

    def test_unordered_list_not_valid(self):
        unordered_list = """
- line 1
- line 2
-line 3 not valid
"""
        typeblock = block_to_block_type(unordered_list)
        self.assertEqual(typeblock, BlockType.PARAGRAPH)
    
    def test_ordered_list_valid(self):
        ordered_list = """
1. line 1
2. line 2
3. line 3
4. l4
5. l5
6. l6
7. l7
8. l8
9. l9
10. l10
"""
        typeblock = block_to_block_type(ordered_list)
        self.assertEqual(typeblock, BlockType.ORDERED_LIST)

    def test_ordered_list_not_valid(self):
        ordered_list = """
1. line 1
2. line 2
3. line 3
4. l4
5. l5
6. l6
8. l8
9. l9
10. l10
"""
        typeblock = block_to_block_type(ordered_list)
        self.assertEqual(typeblock, BlockType.PARAGRAPH)

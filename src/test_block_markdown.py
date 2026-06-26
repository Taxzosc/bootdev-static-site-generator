import unittest
from block_markdown import BlockType, markdown_to_blocks, block_to_block_type, markdown_to_html_node

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


class test_markdown_to_html(unittest.TestCase):
    def test_header(self):
        md = "### third header"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            "<div><h3>third header</h3></div>",
            html
        )
    def test_two_headers(self):
        md = """
### third header

##### fifth header
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            "<div><h3>third header</h3><h5>fifth header</h5></div>",
            html
        )
    
    def test_quote_block(self):
        md = "> this is a quote block"
        node = markdown_to_html_node(md)
        html = node.to_html()
        # print(repr(html))
        self.assertEqual(
            "<div><blockquote>this is a quote block</blockquote></div>",
            html
        )
    
    def test_more_lines_quote_block(self):
        md = """
> this is a quote block
> with **two** lines
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        # print(repr(html))
        self.assertEqual(
            "<div><blockquote>this is a quote block with <b>two</b> lines</blockquote></div>",
            html
        )

    def test_multiline_code(self):
        md = """
```
this is multiline
code
```
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            "<div><pre><code>this is multiline\ncode\n</code></pre></div>",
            html
        )

    def test_paragraph(self):
        md = """
this is a paragraph
with some text in it
thats all
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        # print(repr(html))
        self.assertEqual(
            "<div><p>this is a paragraph with some text in it thats all</p></div>",
            html
        )

    def test_unordered_list(self):
        md = """
- this is
- an unordered
- list of sentences
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        # print(repr(html))
        self.assertEqual(
            "<div><ul><li>this is</li><li>an unordered</li><li>list of sentences</li></ul></div>",
            html
        )

    def test_ordered_list(self):
        md="""
1. this is
2. an ordered
3. list of sentences
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        # print(repr(html))
        self.assertEqual(
            "<div><ol><li>this is</li><li>an ordered</li><li>list of sentences</li></ol></div>",
            html
        )


    def test_full_markdown(self):
        md = """
1. this is an ordered
2. list of sentences
3. with some **bold** text

- this is an
- unordered list
- of sentences with some _italic_ text

### third header

##### fifth header

> this is a quote block

> this is another quote block
> that contains some _italic_ text

```
this is a multiline
code block with some **bold** text
```

this is just a straight paragraph that contains some `code text` some **bold** text,
and some _italic_ text,
there is also a [link](https://boot.dev) and,
a picture to ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) this guy
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        # print(repr(html))
        self.maxDiff = None
        self.assertEqual(
            """<div><ol><li>this is an ordered</li><li>list of sentences</li><li>with some <b>bold</b> text</li></ol><ul><li>this is an</li><li>unordered list</li><li>of sentences with some <i>italic</i> text</li></ul><h3>third header</h3><h5>fifth header</h5><blockquote>this is a quote block</blockquote><blockquote>this is another quote block that contains some <i>italic</i> text</blockquote><pre><code>this is a multiline\ncode block with some **bold** text\n</code></pre><p>this is just a straight paragraph that contains some <code>code text</code> some <b>bold</b> text, and some <i>italic</i> text, there is also a <a href="https://boot.dev">link</a> and, a picture to <img src="https://i.imgur.com/fJRm4Vk.jpeg" alt="obi wan image"></img> this guy</p></div>""",
            html
        )
import unittest
from split_nodes_delimiter import split_nodes_delimiter
from textnode import TextNode, TextType

class TestSplitNodeDelimiter(unittest.TestCase):
    def test_split_node_delimiter_code(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes,[
    TextNode("This is text with a ", TextType.TEXT),
    TextNode("code block", TextType.CODE),
    TextNode(" word", TextType.TEXT),
] )
    def test_split_node_delimiter_bold(self):
        node = TextNode("This is text with a **code block** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(new_nodes,[
    TextNode("This is text with a ", TextType.TEXT),
    TextNode("code block", TextType.BOLD),
    TextNode(" word", TextType.TEXT),
] )
        
    def test_split_node_delimiter_italic(self):
        node = TextNode("This is text with a _code block_ word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertEqual(new_nodes,[
    TextNode("This is text with a ", TextType.TEXT),
    TextNode("code block", TextType.ITALIC),
    TextNode(" word", TextType.TEXT),
] )
    def test_split_node_delimiter_full_bold(self):
        node = TextNode("**This is text with a code block word**", TextType.BOLD)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(new_nodes,[TextNode("**This is text with a code block word**",TextType.BOLD)])
    
    def test_split_node_delimiter_italic_no_word_after_italic(self):
        node = TextNode("This is text with a _code block_", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertEqual(new_nodes,[
    TextNode("This is text with a ", TextType.TEXT),
    TextNode("code block", TextType.ITALIC),
    ] )

    
    # The following tests is copied from the solution, as i see they are missing from mine.
    def test_delim_bold_multiword(self): #adding this test made me realize i was missing a statement to take care of empty strings.
        node = TextNode(
            "This is text with a **bolded word** and **another**", TextType.TEXT
        )
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bolded word", TextType.BOLD),
                TextNode(" and ", TextType.TEXT),
                TextNode("another", TextType.BOLD),
            ],
            new_nodes,
        )
    def test_delim_bold_and_italic(self):  #adding this test has made me see that my valueerror is wrong. and why the task said "MATCHING DELIMITER"
        node = TextNode("**bold** and _italic_", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        new_nodes = split_nodes_delimiter(new_nodes, "_", TextType.ITALIC)
        self.assertListEqual(
            [
                TextNode("bold", TextType.BOLD),
                TextNode(" and ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
            ],
            new_nodes,
        )
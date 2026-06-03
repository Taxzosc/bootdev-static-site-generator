import unittest
from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_text_noteq(self):
        node = TextNode("This is an italic text node", TextType.ITALIC)
        node2 = TextNode("This is a bold text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)
    
    def test_url_noteq(self):
        node = TextNode("bootdevs website", TextType.LINK, "https://www.boot.dev")
        node2 = TextNode("bootdevs website", TextType.LINK, "https://www.boots.dev")
        self.assertNotEqual(node, node2)
    
    def test_url_eq(self):
        node = TextNode("bootdevs website", TextType.LINK, "https://www.boot.dev")
        node2 = TextNode("bootdevs website", TextType.LINK, "https://www.boot.dev")
        self.assertEqual(node, node2)
    
    def test_type_not_eq(self):
        node = TextNode("This is a type test", TextType.BOLD)
        node2 = TextNode("This is a type test", TextType.ITALIC)
        self.assertNotEqual(node, node2)
    
    def test_url_none_eq(self):
        node = TextNode("some text", TextType.BOLD)
        node2 = TextNode("some text", TextType.BOLD, None)
        self.assertEqual(node, node2)
     #copied from boots ai learning tool after asking about missing tests.
     #"a nice to have rather than a genuine gap", since the init is default to None
if __name__ == "__main__":
    unittest.main()
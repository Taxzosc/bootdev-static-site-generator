import unittest
from textnode import TextNode, TextType, text_node_to_html_node

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

    def test_textnode_to_htmlnode_function_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
    
    def test_textnode_to_htmlnode_func_bold(self):
        node = TextNode("This is a bold text node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a bold text node")
    
    def test_textnode_to_htmlnode_func_italic(self):
        node = TextNode("This is an italic text node", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This is an italic text node")
    
    def test_textnode_to_htmlnode_func_code(self):
        node = TextNode("This is a code text node", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "This is a code text node")
    
    def test_textnode_to_htmlnode_func_link(self):
        node = TextNode("This is a link to bootdev node", TextType.LINK, "https://www.boot.dev")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "This is a link to bootdev node")
        self.assertEqual(html_node.props, {"href":"https://www.boot.dev"})
    
    def test_textnode_to_htmlnode_func_image(self):
        node = TextNode("This is a link to bootdev image node", TextType.IMAGE, "https://www.boot.dev")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props, {"src":"https://www.boot.dev", "alt": "This is a link to bootdev image node"})

if __name__ == "__main__":
    unittest.main()
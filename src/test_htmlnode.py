import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    prop_dict = {
    "href": "https://www.google.com",
    "target": "_blank",
}
    def test_tag_eq(self):
        node = HTMLNode("a", "hello", None, self.prop_dict)
        node2 = HTMLNode("a", "hello", None, self.prop_dict)
        self.assertEqual(node.tag,node2.tag)
    
    def test_tag_not_eq(self):
        node = HTMLNode("b", "hello", None, self.prop_dict)
        node2 = HTMLNode("a", "hello", None, self.prop_dict)
        self.assertNotEqual(node.tag,node2.tag)
    
    def test_props_to_html(self):
        node = HTMLNode("b", "hello", None, self.prop_dict)
        # node2 = HTMLNode("a", "hello", None, self.prop_dict)
        # self.assertEqual(node.props_to_html(),node2.props_to_html())
        #  this does the job of checking if each outcome is the same
        # but does not check if the outcome is what we want.
        self.assertEqual(node.props_to_html(),  ' href="https://www.google.com" target="_blank"')
    
    def test_values(self): #copied straight from the solution after completing the assignment. this creates a node and checks if each individual element is equal to the expected result
        node = HTMLNode(
            "div",
            "I wish I could read",
        )
        self.assertEqual(
            node.tag,
            "div",
        )
        self.assertEqual(
            node.value,
            "I wish I could read",
        )
        self.assertEqual(
            node.children,
            None,
        )
        self.assertEqual(
            node.props,
            None,
        )
    
    def test_repr(self): #added after seeing solution to see what i am missing. i understand the unittest better now
        node = HTMLNode("a","hello world", None, {"memes": "dreams"})
        self.assertEqual(node.__repr__(), "HTMLNode(a, hello world, children: None, {'memes': 'dreams'})")
import unittest
from generate_content import extract_title

class test_extract_title(unittest.TestCase):
    def test_first_line_h1(self):
        md = """
# this is a valid h1

this is just some text
"""
        title = extract_title(md)
        self.assertEqual(
            "this is a valid h1",
            title
        )

    def test_not_first_line(self):
        md = """
this is some text

# this is a valid h1
"""
        title = extract_title(md)
        self.assertEqual(
            "this is a valid h1",
            title
        )

    def test_not_only_h1(self):
        md = """
# this is also a valid h1

# this is a valid h1
"""
        title = extract_title(md)
        self.assertEqual(
            "this is also a valid h1",
            title
        )
    
    def test_hash_in_sentence(self):
        md = """
this is # not a h1 tag

# but this is
"""
        title = extract_title(md)
        self.assertEqual(
            "but this is",
            title
        )

    def test_error(self):
        md = """
## there is no valid h1 here

get pranked
"""

        with self.assertRaises(ValueError):
            extract_title(md)
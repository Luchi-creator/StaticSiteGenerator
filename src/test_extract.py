import unittest

from textnode import extract_markdown_images, extract_markdown_links


class TestExtractFunctions(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is a link [to google](https://www.google.com)"
        )
        self.assertListEqual([("to google", "https://www.google.com")], matches)
    
    def test_extract_markdown_images_empty_anchor(self):
        matches = extract_markdown_images(
            "This is text with an ![](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_links_empty_anchor(self):
        matches = extract_markdown_links(
            "This is a link [](https://www.google.com)"
        )
        self.assertListEqual([("", "https://www.google.com")], matches)

    def test_extract_markdown_images_multiple_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and a second ![image](rickroll.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png"),("image", "rickroll.png")], matches)

    def test_extract_markdown_links_multiple_links(self):
        matches = extract_markdown_links(
            "This is a link [to google](https://www.google.com) and [to maybe netflix](https://www.netflix.com)"
        )
        self.assertListEqual([("to google", "https://www.google.com"),("to maybe netflix","https://www.netflix.com")], matches)

    def test_extract_markdown_images_complete_empty(self):
        matches = extract_markdown_images(
            "This is text with an ![]()"
        )
        self.assertListEqual([("", "")], matches)

    def test_extract_markdown_links_complete_empty(self):
        matches = extract_markdown_links(
            "This is a link []()"
        )
        self.assertListEqual([("", "")], matches)


if __name__ == "__main__":
    unittest.main()
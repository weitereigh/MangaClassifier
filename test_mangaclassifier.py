# test_mangaclassifier.py
"""
Tests for MangaClassifier module.
"""

import unittest
from mangaclassifier import MangaClassifier

class TestMangaClassifier(unittest.TestCase):
    """Test cases for MangaClassifier class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = MangaClassifier()
        self.assertIsInstance(instance, MangaClassifier)
        
    def test_run_method(self):
        """Test the run method."""
        instance = MangaClassifier()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()

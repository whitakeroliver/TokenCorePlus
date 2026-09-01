# test_tokencoreplus.py
"""
Tests for TokenCorePlus module.
"""

import unittest
from tokencoreplus import TokenCorePlus

class TestTokenCorePlus(unittest.TestCase):
    """Test cases for TokenCorePlus class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = TokenCorePlus()
        self.assertIsInstance(instance, TokenCorePlus)
        
    def test_run_method(self):
        """Test the run method."""
        instance = TokenCorePlus()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()

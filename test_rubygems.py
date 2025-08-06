# test_rubygems.py
"""
Tests for RubyGems module.
"""

import unittest
from rubygems import RubyGems

class TestRubyGems(unittest.TestCase):
    """Test cases for RubyGems class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = RubyGems()
        self.assertIsInstance(instance, RubyGems)
        
    def test_run_method(self):
        """Test the run method."""
        instance = RubyGems()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()

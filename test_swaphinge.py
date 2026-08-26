# test_swaphinge.py
"""
Tests for SwapHinge module.
"""

import unittest
from swaphinge import SwapHinge

class TestSwapHinge(unittest.TestCase):
    """Test cases for SwapHinge class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = SwapHinge()
        self.assertIsInstance(instance, SwapHinge)
        
    def test_run_method(self):
        """Test the run method."""
        instance = SwapHinge()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()

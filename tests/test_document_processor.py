"""
Tests for the DocumentProcessor class.
"""

import os
import unittest
from pathlib import Path
from unittest.mock import patch, MagicMock

from finanalysis import DocumentProcessor


class TestDocumentProcessor(unittest.TestCase):
    """Test cases for the DocumentProcessor class."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.processor = DocumentProcessor()
    
    def test_initialization(self):
        """Test that the DocumentProcessor initializes correctly."""
        self.assertIsInstance(self.processor, DocumentProcessor)
        self.assertEqual(self.processor.elements, [])
        self.assertEqual(self.processor.config, {})
    
    def test_initialization_with_config(self):
        """Test initialization with custom config."""
        config = {"option": "value"}
        processor = DocumentProcessor(config=config)
        self.assertEqual(processor.config, config)
    
    @patch('finanalysis.processors.document_processor.partition')
    def test_process_file(self, mock_partition):
        """Test processing a file."""
        # Mock the partition function to return some elements
        mock_elements = [MagicMock(), MagicMock()]
        mock_partition.return_value = mock_elements
        
        # Create a temporary file path that exists
        with patch('pathlib.Path.exists', return_value=True):
            result = self.processor.process("dummy_file.pdf")
        
        # Check the partition function was called with the right arguments
        mock_partition.assert_called_once_with(filename="dummy_file.pdf")
        
        # Check the elements were stored and the method returned self
        self.assertEqual(self.processor.elements, mock_elements)
        self.assertEqual(result, self.processor)
    
    def test_process_nonexistent_file(self):
        """Test processing a file that doesn't exist."""
        # Create a temporary file path that doesn't exist
        with patch('pathlib.Path.exists', return_value=False):
            with self.assertRaises(FileNotFoundError):
                self.processor.process("nonexistent_file.pdf")
    
    def test_get_elements(self):
        """Test getting the elements."""
        # Set some elements directly
        mock_elements = [MagicMock(), MagicMock()]
        self.processor.elements = mock_elements
        
        # Check the get_elements method returns the correct elements
        self.assertEqual(self.processor.get_elements(), mock_elements)
    
    def test_get_full_text(self):
        """Test getting the full text."""
        # Create some mock elements with string representations
        element1 = MagicMock()
        element1.__str__.return_value = "Text 1"
        element2 = MagicMock()
        element2.__str__.return_value = "Text 2"
        
        # Set the elements directly
        self.processor.elements = [element1, element2]
        
        # Check the get_full_text method returns the correct text
        self.assertEqual(self.processor.get_full_text(), "Text 1\n\nText 2")


if __name__ == '__main__':
    unittest.main()
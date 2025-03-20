#!/usr/bin/env python
"""
Example script demonstrating how to use FinAnalysis to process a financial document.
"""

import sys
import os
from pathlib import Path

# Add the parent directory to the path to import the package
sys.path.insert(0, str(Path(__file__).parent.parent))

from finanalysis import DocumentProcessor


def main():
    """Process a sample financial document and display the results."""
    
    # Check if a file path is provided as an argument
    if len(sys.argv) < 2:
        print("Usage: python process_document.py <path_to_document>")
        print("Example: python process_document.py ../data/sample_10k.pdf")
        return
    
    file_path = sys.argv[1]
    
    # Create a document processor
    processor = DocumentProcessor()
    
    try:
        # Process the document
        processor.process(file_path)
        
        # Get and display the full text
        full_text = processor.get_full_text()
        print("=" * 80)
        print("DOCUMENT TEXT SAMPLE:")
        print("=" * 80)
        # Print only the first 500 characters for brevity
        print(full_text[:500] + "..." if len(full_text) > 500 else full_text)
        print("\n")
        
        # Get and display the number of elements
        elements = processor.get_elements()
        print(f"Total elements extracted: {len(elements)}")
        print("\n")
        
        # Get the metrics (placeholder for now)
        metrics = processor.extract_metrics()
        print("=" * 80)
        print("EXTRACTED METRICS:")
        print("=" * 80)
        print(metrics)
        print("\n")
        
        # Get the summary (placeholder for now)
        summary = processor.generate_summary()
        print("=" * 80)
        print("DOCUMENT SUMMARY:")
        print("=" * 80)
        print(summary)
        
    except Exception as e:
        print(f"Error processing document: {e}")


if __name__ == "__main__":
    main()
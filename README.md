# FinAnalysis

A financial analysis project leveraging unstructured.io for processing financial documents and extracting valuable insights.

## Overview

FinAnalysis is a tool designed to help financial analysts and researchers extract, process, and analyze information from various financial documents such as:

- Annual reports (10-K)
- Quarterly reports (10-Q)
- Earnings call transcripts
- Financial news articles
- SEC filings
- Bank statements
- Financial PDFs

The project uses [unstructured.io](https://unstructured.io), a powerful library for extracting and preprocessing unstructured data from documents for use with Large Language Models (LLMs).

## Features

- Document ingestion and parsing from multiple sources
- Extraction of key financial metrics and data points
- Natural language processing of financial text
- Data visualization and reporting
- Custom processing pipelines for financial document analysis

## Installation

### Prerequisites

- Python 3.8+
- pip package manager

### Dependencies

Install system dependencies for unstructured.io:

```bash
# For Debian/Ubuntu
sudo apt-get install libmagic-dev poppler-utils tesseract-ocr libreoffice pandoc

# For macOS
brew install libmagic poppler tesseract libreoffice pandoc
```

### Python Installation

```bash
# Clone the repository
git clone https://github.com/mgalore/FinAnalysis.git
cd FinAnalysis

# Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install the required packages
pip install -r requirements.txt
```

## Usage

```python
from finanalysis import DocumentProcessor

# Process a financial document
processor = DocumentProcessor()
results = processor.process("path/to/financial_document.pdf")

# Extract financial metrics
metrics = results.extract_metrics()
print(metrics)

# Generate a summary
summary = results.generate_summary()
print(summary)
```

## Project Structure

```
FinAnalysis/
├── finanalysis/           # Main package
│   ├── __init__.py
│   ├── processors/        # Document processing modules
│   ├── extractors/        # Financial data extraction
│   ├── analyzers/         # Financial analysis tools
│   └── visualizers/       # Data visualization tools
├── examples/              # Example usage scripts
├── tests/                 # Unit and integration tests
├── data/                  # Sample data files
├── notebooks/             # Jupyter notebooks for exploration
├── requirements.txt       # Project dependencies
└── README.md              # Project documentation
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- [unstructured.io](https://unstructured.io) - For providing the core document processing capabilities
- The open-source community for various financial analysis tools and libraries
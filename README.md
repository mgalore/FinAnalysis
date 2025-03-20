# NKAccountant - Automated Accounting System

An AI-powered system that processes raw, unstructured financial data into structured accounting records.

## 1. Overview

NKAccountant is designed to automate the accounting workflow by extracting, processing, classifying, and analyzing financial data from various sources. The system leverages AI technologies to ensure accuracy, compliance, and efficiency while providing insights into financial trends and generating comprehensive financial reports.

## 2. Objectives

- Extract financial data from documents (invoices, receipts, bank statements, etc.)
- Convert unstructured data into structured formats
- Apply accounting rules (double-entry bookkeeping, classification, reconciliation)
- Detect anomalies for auditing and fraud prevention
- Store structured financial data in a database
- Provide a user-friendly dashboard for review and reporting
- Export data in CSV and PDF formats

## 3. System Architecture

### Step 1: Data Ingestion
- **Unstructured.io**: Primary tool for extracting text from various document formats
- Alternatives: AWS Textract, Google Document AI, Tesseract OCR

### Step 2: NLP Processing & Accounting Rule Application
- **GPT-4 + LangChain**: LLM to understand and process text
- Alternative: Spacy + Custom Python Rules

### Step 3: Accounting API Integration
- **QuickBooks API**: For integration with standard accounting systems
- Alternatives: Xero API, Ledger.js

### Step 4: Anomaly Detection & Auditing
- **Scikit-Learn + Custom Models**: For machine learning-based anomaly detection
- Alternatives: MindBridge AI, Pandas + Rule-Based Detection

### Step 5: Data Storage
- **PostgreSQL**: For structured financial data storage
- Alternatives: MongoDB, Google Firestore

### Step 6: User Dashboard & Reporting
- **Streamlit**: For creating an interactive user dashboard
- Alternatives: Retool, Dash

### Step 7: Data Export
- **Pandas + ReportLab**: For CSV and PDF exports
- Alternative: WeasyPrint

## 4. Installation

### Prerequisites

- Python 3.8+
- pip package manager

### System Dependencies

```bash
# For Debian/Ubuntu
sudo apt-get install libmagic-dev poppler-utils tesseract-ocr libreoffice pandoc postgresql

# For macOS
brew install libmagic poppler tesseract libreoffice pandoc postgresql
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

## 5. Usage

```python
from nkaccountant import AccountingSystem

# Initialize the system
system = AccountingSystem()

# Process a financial document
result = system.process_document("path/to/invoice.pdf")

# Review extracted data
print(result.extracted_data)

# Generate accounting entries
entries = result.generate_accounting_entries()
print(entries)

# Export as CSV
result.export_to_csv("accounting_data.csv")

# Generate a financial report
report = system.generate_report(start_date="2023-01-01", end_date="2023-12-31")
report.save_as_pdf("financial_report_2023.pdf")
```

## 6. Project Structure

```
NKAccountant/
├── nkaccountant/           # Main package
│   ├── __init__.py
│   ├── ingestion/          # Data extraction modules
│   ├── processing/         # NLP and accounting rule processing
│   ├── integration/        # Accounting API integrations
│   ├── anomaly/            # Anomaly detection and auditing
│   ├── storage/            # Database storage modules
│   ├── dashboard/          # Streamlit dashboard
│   └── export/             # Data export utilities
├── examples/               # Example usage scripts
├── tests/                  # Unit and integration tests
├── data/                   # Sample data files
├── notebooks/              # Jupyter notebooks for exploration
├── requirements.txt        # Project dependencies
└── README.md               # Project documentation
```

## 7. Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 8. License

This project is licensed under the MIT License - see the LICENSE file for details.

## 9. Acknowledgments

- [unstructured.io](https://unstructured.io) - For providing document processing capabilities
- [LangChain](https://langchain.com) - For NLP processing framework
- Open-source community for various accounting and financial analysis tools
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="finanalysis",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A financial analysis project leveraging unstructured.io",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mgalore/FinAnalysis",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=[
        "unstructured[all-docs]>=0.17.0",
        "pandas>=2.0.0",
        "numpy>=1.24.0",
        "matplotlib>=3.7.0",
        "seaborn>=0.12.0",
        "scikit-learn>=1.2.0",
        "nltk>=3.8.0",
        "beautifulsoup4>=4.12.0",
        "requests>=2.30.0",
        "python-dotenv>=1.0.0",
        "pdfplumber>=0.10.0",
    ],
)
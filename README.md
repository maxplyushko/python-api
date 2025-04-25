# Fake Store API Testing Script

This project contains a Python script to test and validate the product data from the Fake Store API (https://fakestoreapi.com/products).

## Features

- Validates HTTP status code (must be 200 OK)
- Checks each product for:
  - Non-empty title
  - Non-negative price
  - Rating not exceeding 5
- Reports any products that fail validation with detailed defect information

## Prerequisites

- Python 3.x
- pip (Python package installer)
- python3-venv package (for Ubuntu/Debian systems)

## Setup

1. Install the required system package (if on Ubuntu/Debian):
   ```bash
   sudo apt install python3-venv
   ```

2. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Tests

1. Make sure you're in the virtual environment (you should see `(venv)` in your terminal prompt)

2. Run the test script:
   ```bash
   python api_test.py
   ```

## Output

The script will:
- Print any products that violate the validation rules
- For each invalid product, show:
  - Product ID
  - Specific defects found
  - Complete product details for debugging

If no output is shown, it means all products passed the validation checks.

## Dependencies

- requests==2.31.0

## Deactivating the Virtual Environment

When you're done working, you can deactivate the virtual environment:
```bash
deactivate
```

## Project Structure

```
.
├── README.md
├── api_test.py
└── requirements.txt
```

- `api_test.py`: Main testing script
- `requirements.txt`: Python package dependencies
- `README.md`: This documentation file 
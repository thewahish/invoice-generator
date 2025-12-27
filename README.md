# Invoice Generator

**Domain:** Business-Tools
**Status:** Active
**Priority:** Medium

Professional invoice generation system for creating, managing, and exporting invoices with HTML and PDF output support.

## Overview

A comprehensive invoice generation system designed for freelancers and small businesses to create professional invoices quickly and efficiently. Features a web-based interface with Python-powered PDF generation.

## Features

- Create professional invoices via web interface
- Multiple currency support
- Client management
- Customizable invoice templates
- PDF export via Python scripts
- Batch invoice generation
- JSON data storage for invoices

## Project Structure

```
invoice-generator/
├── index.html                    # Main web interface (20KB)
│
├── generated/                    # Generated invoices
│   ├── example-invoice-data.html # Example invoice HTML
│   ├── example-invoice-data.json # Example invoice data
│   ├── invoice-motif-agency-voiceover.html
│   ├── invoice-motif-agency-voiceover.json
│   ├── invoice-motif-agency-voiceover-LOCAL.html
│   ├── Invoice — Motif.pdf       # Generated PDF invoice
│   └── *.pdf                     # Other generated PDFs
│
├── scripts/                      # Python automation
│   ├── generate_pdf.py           # Single PDF generation
│   └── batch_generate.py         # Batch PDF generation
│
├── templates/                    # Invoice templates
│
├── assets/                       # Static assets
│
├── requirements.txt              # Python dependencies
├── CLAUDE.md                     # AI instructions
├── quest-status.json             # Progress tracking
└── README.md                     # This file
```

## Tech Stack

| Technology | Purpose |
|------------|---------|
| **HTML5/CSS3** | Invoice web interface |
| **JavaScript** | Form handling and generation |
| **Python** | PDF generation scripts |
| **JSON** | Invoice data storage |

## Getting Started

### Prerequisites
- Modern web browser
- Python 3.8+ (for PDF generation)

### Installation

```bash
# Clone repository
git clone https://github.com/thewahish/invoice-generator.git
cd invoice-generator

# Install Python dependencies (for PDF generation)
pip install -r requirements.txt
```

### Usage

1. **Open Interface:** Launch `index.html` in a browser
2. **Fill Invoice Data:** Enter client and invoice details
3. **Generate Invoice:** Click generate to create HTML invoice
4. **Export PDF:** Use Python scripts for PDF export

### Generating PDFs

```bash
# Generate single PDF
python scripts/generate_pdf.py

# Batch generate multiple PDFs
python scripts/batch_generate.py
```

## Generated Invoices

The `generated/` folder contains example invoices:

| File | Description |
|------|-------------|
| `example-invoice-data.html` | Sample invoice HTML |
| `example-invoice-data.json` | Sample invoice data |
| `invoice-motif-agency-voiceover.*` | Motif Agency voiceover invoice |
| `Invoice — Motif.pdf` | Generated PDF example |

## Invoice Data Format

Invoices are stored as JSON:

```json
{
  "invoiceNumber": "INV-001",
  "client": "Client Name",
  "items": [...],
  "total": 1000,
  "currency": "USD"
}
```

## Python Scripts

| Script | Purpose |
|--------|---------|
| `generate_pdf.py` | Convert single invoice HTML to PDF |
| `batch_generate.py` | Process multiple invoices at once |

## Templates

The `templates/` folder contains customizable invoice templates. Modify these to match your branding and layout preferences.

## Related Projects

| Project | Relationship |
|---------|-------------|
| `business-tools` | Business utilities collection |
| `personal-finance-management` | Financial management |

## GitHub Repository

[https://github.com/thewahish/invoice-generator](https://github.com/thewahish/invoice-generator)

---

**Developer:** Obai Sukar
**Last Updated:** December 27, 2025

# Invoice Generator

A professional invoice generation system based on your custom invoice template design. Generate beautiful, print-ready invoices with a web interface or command-line tools.

## Features

- **Web-based invoice creator** with live preview
- **Beautiful gradient design** (blue #00AEEF to pink #EC008C)
- **Print-optimized** PDF generation
- **Export to HTML and PDF**
- **Save/load invoice data** as JSON
- **Batch processing** from JSON files
- **Mobile responsive** design

## Quick Start

### Method 1: Web Interface (Easiest)

1. Open `index.html` in your web browser
2. Fill in the invoice details
3. Click "Generate Invoice Preview" to see it
4. Click "Download HTML" to save the invoice
5. Use the Python script to convert to PDF (optional)

### Method 2: Command Line (Advanced)

1. Create a JSON file with invoice data
2. Generate HTML and PDF using Python scripts

## File Structure

```
invoice-generator/
├── index.html              # Web-based invoice creator
├── README.md              # This file
├── templates/             # Invoice templates
├── generated/             # Generated invoices (HTML/PDF)
├── assets/               # Logos and images
└── scripts/              # Python utilities
    ├── generate_pdf.py   # Convert HTML to PDF
    └── batch_generate.py # Generate from JSON data
```

## Usage Examples

### Using the Web Interface

1. **Open the generator:**
   ```bash
   open index.html
   # or just double-click index.html
   ```

2. **Fill in your details:**
   - Your business information
   - Client information
   - Invoice number and date
   - Add line items with dates, descriptions, hours, rates

3. **Generate invoice:**
   - Click "Generate Invoice Preview" to view
   - Click "Download HTML" to save
   - Click "Save Data (JSON)" to save for later

### Converting HTML to PDF

Install Python dependencies first:

```bash
# Install weasyprint for PDF generation
pip install weasyprint

# On macOS, you may need:
brew install cairo pango gdk-pixbuf libffi

# On Ubuntu/Debian:
sudo apt-get install libcairo2 libpango-1.0-0 libpangocairo-1.0-0 libgdk-pixbuf2.0-0 libffi-dev
```

Then convert:

```bash
cd scripts
python generate_pdf.py ../generated/invoice-123.html
# Creates: invoice-123.pdf
```

### Batch Generate from JSON

```bash
cd scripts
python batch_generate.py ../generated/invoice-data.json
# Creates: invoice-data.html and invoice-data.pdf
```

## JSON Data Format

Save invoice data in this format:

```json
{
  "businessName": "Your Business Name",
  "businessAddress": "1134 S Linden Rd, Ste 8\nFlint, MI 48532\nwww.yourbusiness.com",
  "logoUrl": "",
  "clientName": "Client Name",
  "clientAddress": "123 Main St\nCity, ST 12345",
  "invoiceNumber": "001",
  "invoiceDate": "2025-01-15",
  "footerText": "Thank you for your business. Payment due upon receipt.",
  "lineItems": [
    {
      "date": "January 15, 2025",
      "description": "Web Development Services",
      "hours": "10.00",
      "rate": "100.00",
      "amount": "1000.00"
    }
  ]
}
```

## Customization

### Adding Your Logo

1. **Option 1:** Place your logo in the `assets/` folder
2. **Option 2:** Use a URL to your logo
3. In the web form, enter the path: `assets/logo.svg` or `https://example.com/logo.png`

### Changing Colors

Edit the CSS in `index.html` or generated invoices:

- Primary blue: `#00AEEF`
- Primary pink: `#EC008C`
- Purple accent: `#92278F`
- Dark text: `#292663`

### Custom Template

To create a custom template:

1. Generate an invoice using the web interface
2. Download the HTML
3. Edit the HTML/CSS as needed
4. Save as a new template in `templates/`

## Tips

- **Invoice numbering:** Use sequential numbers like 001, 002, etc.
- **Date formats:** Dates display as "January 15, 2025" automatically
- **Currency:** All amounts formatted with $ and commas
- **Hours:** Can use decimals (e.g., 2.5 hours)
- **Print:** Use Cmd+P (Mac) or Ctrl+P (Windows) to print directly from browser

## Troubleshooting

### PDF generation fails

Make sure you've installed weasyprint and its dependencies:
```bash
pip install weasyprint
```

### Logo doesn't show

- Check the file path is correct
- Use absolute paths or relative to the HTML file
- Supported formats: SVG, PNG, JPG

### Invoice doesn't fit on one page

The template is optimized for Letter size with compact styling. If you have many line items:
- Reduce font sizes in the CSS
- Adjust margins in `@page` rule
- Split into multiple invoices

## License

This is your custom invoice system. Use it for your business needs.

## Support

For issues or questions, refer to the original invoice template or modify the code as needed.

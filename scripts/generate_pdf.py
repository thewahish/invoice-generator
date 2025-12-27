#!/usr/bin/env python3
"""
Invoice PDF Generator
Converts HTML invoices to PDF format using weasyprint
"""

import sys
import os
from pathlib import Path

try:
    from weasyprint import HTML, CSS
except ImportError:
    print("ERROR: weasyprint is not installed.")
    print("Please install it with: pip install weasyprint")
    print("\nNote: weasyprint requires additional dependencies:")
    print("  - On macOS: brew install cairo pango gdk-pixbuf libffi")
    print("  - On Ubuntu/Debian: apt-get install libcairo2 libpango-1.0-0 libpangocairo-1.0-0 libgdk-pixbuf2.0-0 libffi-dev")
    sys.exit(1)


def generate_pdf(html_path, output_path=None):
    """
    Generate PDF from HTML invoice

    Args:
        html_path: Path to HTML invoice file
        output_path: Optional path for PDF output (defaults to same name with .pdf extension)

    Returns:
        Path to generated PDF
    """
    html_path = Path(html_path)

    if not html_path.exists():
        raise FileNotFoundError(f"HTML file not found: {html_path}")

    # Set default output path if not provided
    if output_path is None:
        output_path = html_path.with_suffix('.pdf')
    else:
        output_path = Path(output_path)

    # Create output directory if it doesn't exist
    output_path.parent.mkdir(parents=True, exist_ok=True)

    # Generate PDF
    print(f"Generating PDF from {html_path}...")
    HTML(filename=str(html_path)).write_pdf(str(output_path))
    print(f"PDF generated successfully: {output_path}")

    return output_path


def main():
    """Main entry point for command-line usage"""
    if len(sys.argv) < 2:
        print("Usage: python generate_pdf.py <html_file> [output_pdf]")
        print("\nExample:")
        print("  python generate_pdf.py invoice-123.html")
        print("  python generate_pdf.py invoice-123.html ../generated/invoice-123.pdf")
        sys.exit(1)

    html_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else None

    try:
        pdf_path = generate_pdf(html_file, output_file)
        print(f"\n✓ Success! PDF created at: {pdf_path}")
    except Exception as e:
        print(f"\n✗ Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()

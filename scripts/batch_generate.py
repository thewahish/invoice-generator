#!/usr/bin/env python3
"""
Batch Invoice Generator
Generates invoices from JSON data files
"""

import json
import sys
from pathlib import Path
from datetime import datetime


def load_invoice_data(json_path):
    """Load invoice data from JSON file"""
    with open(json_path, 'r') as f:
        return json.load(f)


def format_currency(amount):
    """Format number as currency"""
    return f"${float(amount):,.2f}"


def format_date(date_string):
    """Format date string"""
    date_obj = datetime.strptime(date_string, '%Y-%m-%d')
    return date_obj.strftime('%B %d, %Y')


def create_invoice_html(data):
    """Create invoice HTML from data dictionary"""

    # Generate line items HTML
    line_items_html = []
    for item in data['lineItems']:
        line_items_html.append(f"""
          <tr>
            <td>
              <div class="service-date">{item['date']}</div>
            </td>
            <td>{item['description']}</td>
            <td class="num">{float(item['hours']):.2f}</td>
            <td class="num">{format_currency(item['rate'])}</td>
            <td class="num">{format_currency(item['amount'])}</td>
          </tr>""")

    line_items_html = '\n'.join(line_items_html)

    # Calculate subtotal
    subtotal = sum(float(item['amount']) for item in data['lineItems'])

    # Logo or business name
    if data.get('logoUrl'):
        logo_html = f'<img src="{data["logoUrl"]}" alt="{data["businessName"]} Logo" style="display:block;width:240px;height:auto;margin:0 auto;">'
    else:
        logo_html = f'<h2 style="font-size:28px;margin:0;color:#292663;">{data["businessName"]}</h2>'

    # Format addresses
    business_address = data['businessAddress'].replace('\n', '<br>')
    client_address = data['clientAddress'].replace('\n', '<br>')

    # Create full HTML
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>Invoice — {data['businessName']}</title>
<style>
  /* Page */
  @page {{ size: Letter; margin: 0.75in; }}
  * {{ box-sizing: border-box; }}
  body {{
    font: 14px/1.5 system-ui, -apple-system, Segoe UI, Roboto, Arial, sans-serif;
    color: #1f2330;
    background: #fff;
    -webkit-print-color-adjust: exact;
    print-color-adjust: exact;
    margin: 0;
  }}
  .wrap {{ max-width: 8.5in; margin: 0 auto; }}

  /* Header */
  .header {{
    display: grid;
    grid-template-columns: 200px 1fr 200px;
    gap: 24px;
    align-items: center;
    border-bottom: 1px solid #e5e7eb;
    padding-bottom: 16px;
    margin-bottom: 24px;
  }}

  /* Table */
  .services-table {{
    width: 100%;
    margin-bottom: 30px;
    border-collapse: separate;
    border-spacing: 0;
    overflow: hidden;
    border-radius: 10px;
    box-shadow: 0 2px 10px rgba(41,38,99,0.1);
  }}
  .services-table thead {{
    background: linear-gradient(135deg, #00AEEF, #EC008C);
    color: white;
  }}
  .services-table th {{
    padding: 15px;
    text-align: left;
    font-weight: 600;
    font-size: 14px;
    text-transform: uppercase;
    letter-spacing: 0.5px;
  }}
  .services-table th:last-child {{
    text-align: right;
  }}
  .services-table tbody tr {{
    border-bottom: 1px solid rgba(41,38,99,0.1);
  }}
  .services-table tbody tr:nth-child(even) {{
    background-color: rgba(0,174,239,0.03);
  }}
  .services-table td {{
    padding: 12px 15px;
    font-size: 14px;
    color: #292663;
  }}
  .services-table td:last-child {{
    text-align: right;
    font-weight: 500;
  }}
  .service-date {{
    font-weight: 600;
    color: #00AEEF;
  }}
  .num {{ text-align: right; white-space: nowrap; }}

  /* Totals */
  .totals {{
    display: grid;
    grid-template-columns: 1fr 320px;
    gap: 24px;
    margin-top: 16px;
    align-items: start;
  }}
  .totals .box {{
    background: linear-gradient(135deg, rgba(251,176,76,0.1) 0%, rgba(236,0,140,0.1) 100%);
    border-radius: 10px;
    padding: 20px;
  }}
  .row {{
    display: flex; justify-content: space-between; align-items: center;
    font-size: 14px; padding: 6px 0;
  }}
  .row.total {{
    border-top: 2px solid #EC008C;
    margin-top: 8px; padding-top: 10px;
    font-weight: 700; font-size: 16px;
    color: #292663;
  }}

  /* Footer */
  .footer {{
    margin-top: 28px;
    padding-top: 16px;
    border-top: 1px solid #e5e7eb;
    text-align: center;
    font-size: 12px;
    color: #6b7280;
  }}

  /* Fit-on-one-page overrides */
  @page {{ size: Letter; margin: 0.50in; }}
  body {{ font-size: 12.5px; line-height: 1.35; }}
  .header {{ margin-bottom: 8px; padding-bottom: 6px; gap: 12px; }}
  .header img {{ width: 150px; height: auto; }}
  .services-table {{ margin-bottom: 10px; }}
  .services-table thead th {{ padding: 8px 10px; font-size: 11.5px; }}
  .services-table td {{ padding: 7px 10px; font-size: 12.5px; }}
  table, thead, tbody, tr, td, th {{ page-break-inside: avoid; break-inside: avoid; }}
  .services-table {{ page-break-after: avoid; break-after: avoid; }}
  .totals, .totals * {{ page-break-inside: avoid; break-inside: avoid; }}
  .totals {{ grid-template-columns: 1fr 240px; gap: 12px; margin-top: 6px; }}
  .totals .box {{ padding: 10px 12px; }}
  .row {{ padding: 3px 0; font-size: 12.5px; }}
  .row.total {{ font-size: 14px; padding-top: 6px; }}
  .footer {{ margin-top: 12px; padding-top: 8px; font-size: 10.5px; }}
</style>
</head>
<body>
  <div class="wrap">
    <!-- Header -->
    <div class="header" style="display:grid;grid-template-columns:200px 1fr 200px;gap:24px;align-items:center;">
      <div style="text-align:left;">
        <h3 style="font-size:12px;color:#6b7280;text-transform:uppercase;letter-spacing:.08em;margin:0 0 8px;">Bill To</h3>
        <div style="font-size:13px;line-height:1.4;color:#292663;">
          {client_address}
        </div>
      </div>

      <div style="text-align:center;">
        {logo_html}
        <div style="font-size:12px;margin-top:8px;line-height:1.4;color:#292663;">
          {business_address}
        </div>
      </div>

      <div class="invoice-details" style="text-align:right;">
        <h2 style="font-size:26px;margin:0;color:#EC008C;">INVOICE</h2>
        <p style="font-size:13px;margin:5px 0;"><strong>Invoice #:</strong> {data['invoiceNumber']}</p>
        <p style="font-size:13px;margin:5px 0;"><strong>Date:</strong> {format_date(data['invoiceDate'])}</p>
      </div>
    </div>

    <!-- Table -->
    <section class="block" style="margin-top: 20px;">
      <table class="services-table">
        <thead>
          <tr>
            <th style="width:18%">Date</th>
            <th style="width:57%">Service Description</th>
            <th style="width:8%">Hours</th>
            <th style="width:8%">Rate</th>
            <th style="width:9%" class="num">Amount</th>
          </tr>
        </thead>
        <tbody>
          {line_items_html}
        </tbody>
      </table>
    </section>

    <!-- Totals -->
    <section class="totals">
      <div></div>
      <div class="box">
        <div class="row"><span>Subtotal</span><span>{format_currency(subtotal)}</span></div>
        <div class="row total"><span>Total Due</span><span>{format_currency(subtotal)}</span></div>
      </div>
    </section>

    <!-- Footer -->
    <footer class="footer">
      {data['footerText']}
    </footer>
  </div>
</body>
</html>"""

    return html


def main():
    """Main entry point"""
    if len(sys.argv) < 2:
        print("Usage: python batch_generate.py <json_file>")
        print("\nExample:")
        print("  python batch_generate.py invoice-data.json")
        sys.exit(1)

    json_path = Path(sys.argv[1])

    if not json_path.exists():
        print(f"Error: File not found: {json_path}")
        sys.exit(1)

    # Load data
    print(f"Loading invoice data from {json_path}...")
    data = load_invoice_data(json_path)

    # Generate HTML
    html = create_invoice_html(data)

    # Save HTML
    output_path = json_path.with_suffix('.html')
    with open(output_path, 'w') as f:
        f.write(html)

    print(f"✓ Invoice HTML generated: {output_path}")

    # Try to generate PDF if weasyprint is available
    try:
        from generate_pdf import generate_pdf
        pdf_path = generate_pdf(output_path)
        print(f"✓ Invoice PDF generated: {pdf_path}")
    except ImportError:
        print("\nNote: Install weasyprint to generate PDFs automatically")
        print("  pip install weasyprint")


if __name__ == "__main__":
    main()

from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from datetime import datetime

def generate_pdf(query: str, sources: list, summary: str, filename: str):
    c = canvas.Canvas(filename, pagesize=A4)
    width, height = A4

    x_margin = 1 * inch
    y = height - 1 * inch

    # Title
    c.setFont("Helvetica-Bold", 16)
    c.drawString(x_margin, y, f"Research Report: {query}")
    y -= 30

    # Metadata
    c.setFont("Helvetica", 10)
    c.drawString(x_margin, y, f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    y -= 40

    # Sources
    c.setFont("Helvetica-Bold", 12)
    c.drawString(x_margin, y, "Sources")
    y -= 20

    c.setFont("Helvetica", 10)
    for s in sources:
        text = f"- {s['title']} ({s['url']})"
        c.drawString(x_margin, y, text[:110])
        y -= 15
        if y < 1 * inch:
            c.showPage()
            y = height - 1 * inch

    # Summary
    c.showPage()
    y = height - 1 * inch

    c.setFont("Helvetica-Bold", 12)
    c.drawString(x_margin, y, "Summary")
    y -= 20

    c.setFont("Helvetica", 11)
    for line in summary.split("\n"):
        c.drawString(x_margin, y, line[:110])
        y -= 15
        if y < 1 * inch:
            c.showPage()
            y = height - 1 * inch

    c.save()

from fpdf import FPDF
import pandas as pd

df = pd.read_csv('topics.csv')

pdf = FPDF(orientation="P", unit='mm', format='A4')
pdf.auto_page_break = False
for item, row in df.iterrows():
    pdf.add_page()
    pdf.set_font(family="times", style='B', size=20)
    pdf.cell(w=0, h=20, align="L", ln=1, border=0, txt=row['Topic'])

    for i in range(24, 290, 13):
        pdf.line(10, i, 200, i)
        print(i)

    pdf.ln(275)
    pdf.set_font(family="times", style='B', size=10)
    pdf.cell(w=0, h=10, align="R", ln=0, border=0, txt=row['Topic'])

    for i in range(row['Pages'] - 1):
        pdf.add_page()
        pdf.ln(275)
        pdf.set_font(family="times", style='B', size=10)
        pdf.cell(w=0, h=10, align="R", ln=0, border=0, txt=row['Topic'])

        for y in range(10, 290, 13):
            pdf.line(10, y, 200, y)

pdf.output("output.pdf")

import pandas as pd
from fpdf import FPDF
from pathlib import Path
import glob

filepaths = glob.glob('invoice/*.xlsx')

for paths in filepaths:
    filename = Path(paths).stem

    invoice_no, date = filename.split('-')
    df = pd.read_excel(paths, sheet_name="Sheet 1")

    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()

    pdf.set_font(family='Times', style="B", size=25)
    pdf.cell(w=0, h=25, txt=f"Invoice_No {invoice_no}", ln=1)

    pdf.set_font(family='Times', style="I", size=15)
    pdf.cell(w=0, h=15, txt=f"Date {date}", ln=1)

    columns = list(df.columns)
    columns = [item.replace("_", " ").title() for item in columns]
    pdf.set_font(family='Times', style="B", size=9)
    pdf.cell(w=20, h=9, txt=columns[0], border=1, align="C")
    pdf.cell(w=38, h=9, txt=columns[1], border=1, align="C")
    pdf.cell(w=30, h=9, txt=columns[2], border=1, align="C")
    pdf.cell(w=25, h=9, txt=columns[3], border=1, align="C")
    pdf.cell(w=20, h=9, txt=columns[4], border=1, align="C", ln=1)

    print(df.columns)
    for i, row in df.iterrows():
        pdf.set_font(family='Times', style="I", size=9)
        pdf.cell(w=20, h=7, txt=str(row['product_id']), border=1, align="C")
        pdf.cell(w=38, h=7, txt=str(row['product_name']), border=1, align="C")
        pdf.cell(w=30, h=7, txt=str(row['amount_purchased']), border=1, align="C")
        pdf.cell(w=25, h=7, txt=str(row['price_per_unit']), border=1, align="C")
        pdf.cell(w=20, h=7, txt=str(row['total_price']), border=1, align="C", ln=1)

    add = df['total_price'].sum()
    pdf.set_font(family='Times', style="I", size=9)
    pdf.cell(w=20, h=7, txt="", border=1, align="C")
    pdf.cell(w=38, h=7, txt="", border=1, align="C")
    pdf.cell(w=30, h=7, txt="", border=1, align="C")
    pdf.cell(w=25, h=7, txt="", border=1, align="C")
    pdf.cell(w=20, h=7, txt=str(add), border=1, align="C", ln=1)

    pdf.set_font(family='Times', style="B", size=15)
    pdf.cell(w=0, h=15, txt=f"The total of price is {add}", ln=1)

    pdf.set_font(family='Times', style="B", size=12)
    pdf.cell(w=0, h=12, txt="Spider_Kingdom")


    pdf.output(f"PDFs/{filename}.pdf")










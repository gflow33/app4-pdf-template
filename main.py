from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

df = pd.read_csv('topics.csv')
for index, row in df.iterrows():
    pdf.add_page()
    # print()
    pdf.set_font(family="Times", style="B", size=12)
    pdf.set_text_color(100, 254, 10)
    pdf.cell(w=0, h=12, txt=row['Topic'], align="L", ln=1)
    pdf.line(10, 20, 200, 20)
    
    # Set the footer
    pdf.ln(265)
    pdf.set_font(family="Times", style="I", size=8)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=10, txt=row['Topic'], align="R")


    

    for i in range(row['Pages'] - 1):
        pdf.add_page()
        # Set the footer
        pdf.ln(275)
        pdf.set_font(family="Times", style="I", size=8)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=10, txt=row['Topic'], align="R")



pdf.output("output.pdf")

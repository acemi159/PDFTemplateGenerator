from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

df = pd.read_csv("topics.csv")

page_width = pdf.w
page_height = pdf.h
lines_start = 35
lines_thickness = 10

for index, row in df.iterrows():
    for page in range(row["Pages"]):
        pdf.add_page()
        
        
        if page == 0:
            pdf.set_font(family="Times", style="B", size=24)
            pdf.set_text_color(100, 100, 100)
            pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1)
            pdf.line(x1=10, y1=25, x2=200, y2=25)
            pdf.ln(265)
            pdf.set_font(family="Times", style="I", size=8)
            pdf.set_text_color(180, 180, 180)
            pdf.cell(w=0, h=10, txt=row['Topic'], align="R")
        else:
            # Footer
            pdf.ln(277)
            pdf.set_font(family="Times", style="I", size=8)
            pdf.set_text_color(180, 180, 180)
            pdf.cell(w=0, h=10, txt=row['Topic'], align="R")
        
        lines_count = int((page_height-lines_start) // lines_thickness)
        
        for i in range(lines_count):
            pdf.line(x1=5, y1=(lines_start + i*lines_thickness), x2=page_width - 5, y2=(lines_start + i*lines_thickness))
            

pdf.output("output.pdf")
from fpdf import FPDF

def main():
    line = input("Name for shirt: ")
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("helvetica", "B", 50)
    pdf.cell(text="CS50 Shirtificate", align="C", center=True, new_x="LMARGIN", new_y="NEXT")
    pdf.image("D:\Dad programs\week8\shirtificate.png", w=pdf.epw)
    pdf.set_font_size(30)
    pdf.set_text_color(255, 255, 255)
    pdf.cell(h=-250, text=f"{line} took CS50", align="C", center=True)
    pdf.output("shirtificate.pdf")

if __name__ == "__main__":
    main()
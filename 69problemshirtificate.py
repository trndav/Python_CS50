from fpdf import FPDF

user_input = input("Name: ")
shirt_img_path = "shirtificate.png"
string = " took CS50"

pdf = FPDF(orientation="portrait", unit="mm", format="A4")
pdf.add_page()
pdf.set_font('Arial', 'B', 26)
pdf.cell(0, 10, "CS50 Shirtificate", border=0, ln=True, align="C")
pdf.cell(0, 10, text="", border=0, ln=True, align="C")

pdf.image(shirt_img_path, x=10, w=190)

pdf.set_y(pdf.get_y() - 140)
pdf.set_text_color(255, 255, 255)
pdf.set_font('Arial', 'B', 26)
pdf.cell(0, 10, user_input+string, border=0, ln=True, align="C")
pdf.output("shirtificate.pdf")

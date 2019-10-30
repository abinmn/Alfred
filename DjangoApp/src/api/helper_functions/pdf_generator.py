from reportlab.graphics.barcode import qr
from reportlab.graphics.shapes import Drawing 
from reportlab.lib.pagesizes import B6
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas
from reportlab.graphics import renderPDF

from django.core.files import File
from django.core.mail import EmailMessage
from io import BytesIO

 
def createBarCodes(excel_id):
    """
    Create barcode examples and embed in a PDF
    """
    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=B6,)
 
    x = 1 * mm
    y = 285 * mm
    x1 = 6.4 * mm
 
 
  
    # draw a QR code
    qr_code = qr.QrCodeWidget(excel_id.id)
    d = Drawing(300, 300)
    d.add(qr_code)
    renderPDF.draw(d, c, 120, 400)

    c.drawString(130, 390, excel_id.id)
    c.drawString(130, 375, excel_id.name)
    c.drawString(130, 360, excel_id.college.name)
    c.drawString(130, 345, excel_id.email)
    c.drawString(130, 330, str(excel_id.phone_number))
    c.save()

    pdf = buffer.getvalue()

    print(excel_id.email)
    email_message = EmailMessage(
        "ExcelId", "Hello World!", "excelmec2019@gmail.com", (excel_id.email,)
    )
    # try:
    #     email_message.attach(pdf)
    # except:
    #     print('attachement exception')
    email_message.attach('excel_id.pdf', pdf, 'application/pdf')
    email_message.send()

if __name__ == "__main__":
    createBarCodes("EX1")

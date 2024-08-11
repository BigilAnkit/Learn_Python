import qrcode

# Generate QR code
qr = qrcode.QRCode(version=1, box_size=10, border=5)
qr.add_data("https://www.linkedin.com/in/aankitgehlot/")
qr.make(fit=True)

# Save the QR code as an image
img = qr.make_image(fill_color="black", back_color="white")
img.save("my_qrcode.png")

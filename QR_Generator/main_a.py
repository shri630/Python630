from PIL import Image
import qrcode
qr = qrcode.QRCode(version=1,box_size=10,border=10,error_correction=qrcode.ERROR_CORRECT_H,)
qr.add_data("www.google.com")
qr.make(fit=True)
img = qr.make_image(fill_color="red",back_color="white")
img.save("google.png")
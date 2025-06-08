import qrcode

img = qrcode.make("www.google.com")

img.save("google.png")


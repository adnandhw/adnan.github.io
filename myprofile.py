import qrcode

link = "https://adnandhw.github.io/adnan.github.io/"
img = qrcode.make(link)
img.save("QR_WebProfilAdnan.png")

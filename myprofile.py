import qrcode

link = "http://localhost/myprofile.php"
img = qrcode.make(link)
img.save("QR_WebProfilAdnan.png")

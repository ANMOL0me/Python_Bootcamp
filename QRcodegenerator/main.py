import qrcode
from PIL import Image, ImageDraw
url = "HAppy Buitrhfsa"
filename = input("File name you want to save:\t")
if not(filename.endswith(".png")):
    filename += ".png"

    
img = qrcode.make(url)
img.save(filename)

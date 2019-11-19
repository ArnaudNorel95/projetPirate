
from PIL import Image
import statistics

im = Image.open("pictures/letsHack.jpg")

imgF = Image.new("RGB", [278, 131])
imgVerte = Image.new("RGB", [278, 131])

width = im.size[0]
height = im.size[1]

print("widht : ", width, "height : ", height)

iDefault = 1227
iFilter = 1228

for i in range(0, 278):
    for j in range(0, 131):
        #px = im.getpixel((iDefault, j+844))
        #imgVerte.putpixel((0,j), px)  

        pxF = im.getpixel((iFilter-i, j+844))
        imgVerte.putpixel((278-i-1, j), pxF)

imgVerte.save("resultats/GROSTEST.jpg")


#imgF.save("resultats/GrandeFiltree.jpg")

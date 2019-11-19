
from PIL import Image
import statistics

im = Image.open("resultats/imgVerteEtGrise.jpg")
width = im.size[0]
height = im.size[1]

imgF = Image.new("RGB", [2, 9])

Filtre = [[15, 0, 0], [-14,0, 0], [0, 0 ,0]]

def Convolution2D(Filtre,TPix,x,y):
  p0 = p1 = p2 = 0
  for i in range(-1,1):
   for j in range(-1,1):
    p0 += Filtre[i+1][j+1]*TPix.getpixel((y+i,x+j))[0]
    p1 += Filtre[i+1][j+1]*TPix.getpixel((y+i,x+j))[1]
    p2 += Filtre[i+1][j+1]*TPix.getpixel((y+i,x+j))[2]
    # normalisation des composantes
    p0 = int(p0/9.0)
    p1 = int(p1/9.0)
    p2 = int(p2/9.0)
  # retourne le pixel convolué
  return (p0,p1,p2)

for x in range(1,height-1):
    #for y in range(1,width-1):
    pDefault = im.getpixel((0,x))
    p = Convolution2D(Filtre,im,x,1)
    imgF.putpixel((1,x),p)
    imgF.putpixel((0,x), pDefault)

imgF.save("resultats/GROSTESTFILTREE.jpg")
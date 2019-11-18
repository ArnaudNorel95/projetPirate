
from PIL import Image
import statistics

im = Image.open("resultats/imgVerteEtGrise.jpg")

#imGris = im.convert("L")
imgF = Image.new("RGB", [2, 9])
imgVerte = Image.new("RGB", [2,131])


iDefault = 1227
iFilter = 1228

#for j in range(0, 131):
#    px = im.getpixel((iDefault, j+844))
#    imgVerte.putpixel((0,j), px)

#    pxF = im.getpixel((iFilter, j+844))
#    imgVerte.putpixel((1,j), pxF)

#imgVerte.save("resultats/imgVerteEtGrise.jpg")

Filtre = [[0,-2,0],[0,16,0],[0,-2,0]]
#Filtre = [[1,1,1],[1,1,1],[1,1,1]]
#Filtre = [[4,2,1,0,0], [4,2,1,0,0], [4,2,1,0,0], [4,2,1,0,0], [4,2,1,0,0]]

width = im.size[0]
height = im.size[1]

def Convolution2D(Filtre,TPix,x,y):
  p0 = p1 = p2 = 0
  for i in range(-1,1):
   for j in range(-1,1):
    p0 += Filtre[i+1][j+1]*TPix.getpixel((0,x+j))[0]
    p1 += Filtre[i+1][j+1]*TPix.getpixel((0,x+j))[1]
    p2 += Filtre[i+1][j+1]*TPix.getpixel((0,x+j))[2]
    # normalisation des composantes
    p0 = int(p0/9.0)
    p1 = int(p1/9.0)
    p2 = int(p2/9.0)
  # retourne le pixel convolué
  return (p0,p1,p2)


for x in range(0,height):
  #for y in range(1,width-1):
   p = Convolution2D(Filtre,im,x,1)
   pDefault = im.getpixel((1, x-1))

   imgF.putpixel((0,x),p)
   imgF.putpixel((1,x),pDefault)
   print(x, " ", 1, " : success")


imgF.save("resultats/imgVerteEtGriseFiltree.jpg")

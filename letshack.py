
from PIL import Image
import statistics

im = Image.open("resultats/imgGriseACP.jpg")

#imGris = im.convert("L")
imgF = Image.new("RGB", [1, 9])
imgVerte = Image.new("RGB", [1,131])


iDefault = 1227
iFilter = 1228

#for j in range(0, 131):
#    px = im.getpixel((iDefault, j+844))
#    imgVerte.putpixel((0,j), px)

#    pxF = im.getpixel((iFilter, j+844))
#    imgF.putpixel((0,j), pxF)

#imgVerte.save("resultats/imgVerte.jpg")

Filtre = [[-1,-2,-1],[-2,16,-2],[-1,-2,-1]]
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


for x in range(1,height-1):
  #for y in range(1,width-1):
   p = Convolution2D(Filtre,im,x,1)
   imgF.putpixel((0,x),p)
   print(x, " ", 1, " : success")


imgF.save("resultats/imgGriseFiltreeACP.jpg")

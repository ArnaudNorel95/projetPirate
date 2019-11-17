
from PIL import Image
import statistics

im = Image.open("pictures/letsHack.jpg")

imGris = im.convert("L")
imgF = Image.new("RGB", im.size)
imgVerte = Image.new("RGB", [1,131])


iDefault = 1227
iFilter = 1228

#tabDefault  = []
#tabFilter = []

for j in range(1, 131):
    px = im.getpixel((iDefault, j+844))
    imgVerte.putpixel((0,j), px)
    #tabDefault.append(imGris.getpixel((iDefault, j)))
    #tabFilter.append(imGris.getpixel((iFilter, j)))

imgVerte.save("resultats/imgVerte.jpg")

#for j in range(0, 977-845):
#    print(tabDefault[j], "  =>  ", tabFilter[j])


#Filtre = [[-1,-2,-1],[-2,16,-2],[-1,-2,-1]]
Filtre = [[0,-4,0],[-4,18,-4],[0,-4,-0]]

width = im.size[0]
height = im.size[1]

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


#for x in range(1,height-1):
#  for y in range(1,width-1):
#   p = Convolution2D(Filtre,im,x,y)
#   imgF.putpixel((y,x),p)
#   print(x, " ", y, " : success")


imgF.save("resultats/hackedResult2.jpg")

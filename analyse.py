from PIL import Image

im = Image.open("resultats/imgVerteEtGrise.jpg")
#imCheat = Image.open("resultats/cheat.jpg")
data = list(im.getdata())

#print(data)

width = im.size[0]
height = im.size[1]
imNew = Image.new("L", (width, height))

###################################################################################"
#DISPLAY PIXEL VALUES OF IMAGE
###################################################################################"

for i in range(0, height):
    for j in range(0, width):
        numPixel = width*i + j
        val = (data[numPixel][0] + data[numPixel][1] + data[numPixel][2])/3
        
        if(round(val) == 192):
            print("   ", end=" ")
        else:
            print(round(val), end=" ")
    print(" ")

###################################################################################"
#INVERSE COLORS
###################################################################################"

#for i in range(0, height):
#    for j in range(0, width):

#        pixel = im.getpixel((j,i))
#        val = (pixel[0] + pixel[1] + pixel[2])/3

#        pixelNEW = 255-round(val)
#        imNew.putpixel((j,i), pixelNEW)

#imNew.save("resultats/negativeColors.jpg")

###################################################################################"
#CHANGE THE IMAGE : SET THE DIAGONAL WITH BLACK PIXELS
###################################################################################"

#for i in range(0, height):
#    for j in range(0, width):

#        pixelBLACK = 0
#        if(i==j):
#            im.putpixel((j,i), pixelBLACK)


#im.save("resultats/diagonaleBlackos.jpg")

###################################################################################"
#BLACK & WHITE
###################################################################################"

#imNew = im.convert("L")
#imNew.save("resultats/cheat.jpg")

#for i in range(0, height):
#    for j in range(0, width):

#        pixel = im.getpixel((j,i))
#        pixelGrey = imCheat.getpixel((j,i))

#        print(pixel, " VS " , pixelGrey)
        #pixelGrey = (pixel[0] + pixel[1] + pixel[2])/3
        #print(pixel, " : ", pixelGrey)
        #imNew.putpixel((j,i), pixelGrey)

#imNew.save("resultats/noirEtBlanc.jpg")
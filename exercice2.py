from PIL import Image

im = Image.open("pictures/imageTRESPETITE.jpg")
width = im.size[0]
height = im.size[1]
imNew = Image.new("L", ((width+1, height+1)))

im = im.convert("L")

for i in range (0, height+1):
    for j in range (0, width+1):
        if(i==0):
            imNew.putpixel((j,i), 0)
        elif(j==0):
            imNew.putpixel((j,i), 0)
        elif(i==width):
            imNew.putpixel((j,i), 0)
        elif(j==height):
            imNew.putpixel((j,i), 0)
        else :
            imNew.putpixel((j,i), im.getpixel((j,i)))

imNew.save("resultats/imageTRESPETITEcadre.jpg")

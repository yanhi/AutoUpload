import os
import os.path
from PIL import Image, ImageDraw, ImageFont
import math

rootdir = '/Users/yan/Downloads/cct'
imagenamelist=[]
for parent,dirnames,filenames in os.walk(rootdir):
    for filename in filenames:
        if(filename.rsplit('.')[1]!="txt" and filename.rsplit('.')[1]!="DS_Store"):
            imagenamelist.append(os.path.join(parent,filename))
            imagenamen = tuple(imagenamelist)
            print(imagenamen)
imagename = imagenamen[:]
print(imagename)
for i in imagename:
    image = Image.open(i)
    print(image.size, image.format,image.filename)
    width,height = image.size
    text = "HBIS HBIS HBIS HBIS HBIS"
    textImageW = int(width*5)
    textImageH = int(height*5)
    font = ImageFont.truetype('Arial.ttf', 500)
    if image.mode == 'RGBA':
        blank = Image.new("RGBA", (textImageW, textImageH), "white")
    elif image.mode == 'RGB':
        blank = Image.new("RGB", (textImageW, textImageH), "white")
    elif image.mode == "L":
        blank = Image.new("L", (textImageW, textImageH), "white")

    d = ImageDraw.Draw(blank)
    textW,textH = font.getsize(text)
    d.ink = 0 + 112 * 256 + 199 * 256 * 256
    d.text([(textImageW-textW)/2,(textImageH-textH)/2],text,font = font)
    textRotate = blank.rotate(30)
    rLen = math.sqrt((textW/2)**2+(textH/2)**2)
    oriAngle = math.atan(textH/textW)
    cropW = rLen*math.cos(oriAngle + math.pi/6) *2
    cropH = rLen*math.sin(oriAngle + math.pi/6) *2
    box = [int((textImageW-cropW)/2-1),int((textImageH-cropH)/2-1)-50,int((textImageW+cropW)/2+1),int((textImageH+cropH)/2+1)]
    textIm = textRotate.crop(box)

    pasteW,pasteH = textIm.size
    if image.mode == 'RGBA':
        textBlank = Image.new("RGBA",(width,height),"white")
    elif image.mode == 'RGB':
        textBlank = Image.new("RGB", (width, height), "white")
    elif image.mode == "L":
        textBlank = Image.new("L", (width, height), "white")

    pasteBox = (int((width-pasteW)/2-1), int((height-pasteH)/2-1))
    textBlank.paste(textIm, pasteBox)

    waterImage = Image.blend(image, textBlank, 0.2)
    waterImage.save(i)
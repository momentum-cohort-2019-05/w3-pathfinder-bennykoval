from PIL import Image

catIm = Image.open("zophie.png")
catCopyIm = catIm.copy()

catIm.size

print(catIm.size)

width, height = catIm.size 

print(width, height)

print(catIm.filename)

print(catIm.format)

croppedIm = catIm.crop((335, 345, 565, 560))
croppedIm.save("cropped_zophie.png")

faceIm = catIm.crop((335, 345, 565, 560))
faceIm.size

catCopyIm.paste(faceIm, (0, 0))
catCopyIm.paste(faceIm, (400, 500))
catCopyIm.save("pasted_zophie.png")

catImWidth, catImHeight = catIm.size
faceImWidth, faceImHeight = faceIm.size
catCopyTwo = catIm.copy()
for left in range(0, catImHeight, faceImHeight):
    for top in range(0, catImHeight, faceImHeight):
        print(left, top)
        catCopyTwo.paste(faceIm (left, top))

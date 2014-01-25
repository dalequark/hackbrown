from PIL import Image
import numpy
import random

learnPic = "grass.jpg"
markovL = 1
roundMod = 254
RGBcols = 255

palette = []
for x in range(1,roundMod+1):
	palette.append(RGBcols/x)

def simple(inValue):
	return palette[inValue%roundMod]

print simple(300)
inPic = Image.open(learnPic).convert("RGB")

width = inPic.size[0]
length = inPic.size[1]

outPic = Image.new("RGB", (min(length, width), min(length, width)))

# Convert to simpler color profile
count = 0
for x in range(0, width):
	for y in range(0, length):
		tup = inPic.getpixel((x,y))
		simplePix = (simple(tup[0]), simple(tup[1]), simple(tup[2]))
		inPic.putpixel((x,y), simplePix)
'''
for x in range(0, width):
	for y in range(0, length):
		inPic.putpixel((x,y), (1,1,1))
'''	

model = dict()
'''
# Creating the model
for x in range(markovL, width):
	for y in range(markovL, length):
		# The keys in the model are string concatinations of left, up, left, up (markovL times)
		thisList = []
		for pic in range(1, markovL+1):
			thisList.append(str(inPic.getpixel((x-pic, y))))
			thisList.append(str(inPic.getpixel((x, y-pic))))
		key = "".join(thisList)
		thisPicColor = str(inPic.getpixel((x,y)))

		# If key in model, increment count, else add it
		if key in model:
			if thisPicColor in model[key]:
				model[key][thisPicColor] += 1
			else:
				model[key][thisPicColor] = 1
		else:
			model[key] = dict()
			model[key][thisPicColor] = 1


# now generate!
width = outPic.size[0]
length = outPic.size[1]

# Create the resulting image. Just use the frame from the previous image for now
for x in range(0, width):
	for y in range(0, markovL+1):
		outPic.putpixel((x,y), inPic.getpixel((x,y)))
		outPic.putpixel((y,x), inPic.getpixel((y,x)))


for x in range(markovL, width):
	for y in range(markovL, length):
		# The keys in the model are string concatinations of left, up, left, up (markovL times)
		thisList = []
		for pic in range(1, markovL+1):
			thisList.append(str(inPic.getpixel((x-pic, y))))
			thisList.append(str(inPic.getpixel((x, y-pic))))
		key = "".join(thisList)
		possibleColorArray = model[key]
		totalCounts = 0

		# This is slow, need to go through counts twice, fix later
		count = 0 
		chosenColor = ""
		for color in possibleColorArray: 
			thisCount = possibleColorArray[color]
			randIndex = random.randint(1, totalCounts+thisCount)
			randNthWeight = random.randint(0, count)
			if randIndex > totalCounts and randNthWeight == count:
				chosenColor = color
			count += 1
			totalCounts += thisCount

		# go from key back to pixel
		tempAr = chosenColor[1:len(chosenColor)-1].split(",")
		rgbVal = (int(tempAr[0]), int(tempAr[1]), int(tempAr[2]))
		outPic.putpixel((x,y), rgbVal)
'''


'''

(r, g, b) = inPic.getpixel((1,1))

avgr = 0
avgb = 0
avgg = 0


for y in range(0, inPic.size[0]):
	for x in range(0, inPic.size[1]):
		(r, g, b) = inPic.getpixel((y,x))
		avgr += r
		avgb += b
		avgg += g

size = inPic.size[0] * inPic.size[1]
(resr, resg, resb) = (avgr/size, avgg/size, avgb/size)

for y in range(0,512):
	for x in range(0,512):
		outPic.putpixel((x,y), (resr, resg, resb))

'''
inPic.show()

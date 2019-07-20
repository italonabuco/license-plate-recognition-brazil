import cv2
import math
import re
from PIL import Image
import numpy as np

class possibleChar:
	def __init__(self, contour):
		self.contour = contour
		self.near = False
		self.boundingRect = cv2.boundingRect(self.contour)

		[x, y, w, h] = self.boundingRect

		self.boundingRectX = x
		self.boundingRectY = y
		self.boundingRectW = w
		self.boundingRectH = h
		self.centerX = x + int(w*0.5)
		self.centerY = y + int(h*0.5)
		self.aspectRatio = float(self.boundingRectW) / float(self.boundingRectH)

class group:
	def __init__(self, top, left, right, bottom):
		self.top = top
		self.left = left
		self.right = right
		self.bottom = bottom
		self.w = right - left
		self.h = bottom -top
		self.aspectRatio = float(self.h) / float(self.w)

def checkPossiblePlate(group):
	if(group.h < group.w
		and group.aspectRatio < 0.6
		):
		return True
	else:
		return False

def inGroups(group1, group2):
	if((group2.bottom >= group1.top >= group2.top or group2.bottom >= group1.bottom >= group2.top)
		and (group2.right >= group1.left >= group2.left or group2.right >= group1.right >= group2.left)):
		return True
	else:
		return False

def checkIfChar(possibleChar):
	if(possibleChar.boundingRectH > possibleChar.boundingRectW
		and possibleChar.aspectRatio < 0.8
		and 70 > possibleChar.boundingRectH > 10
		and possibleChar.boundingRectW > 5
		):
		return True
	else:
		return False

def distanceBetween(possible1, possible2):
	xb = abs(possible1.boundingRectX - possible2.boundingRectX)
	yb = abs(possible1.boundingRectY - possible2.boundingRectY)

	return math.sqrt((xb ** 2) + (yb ** 2));

def filterByGreater(arrChars, percentage):
	greaterHeight = 0
	for char in arrChars:
		if(char.boundingRectH > greaterHeight):
			greaterHeight = char.boundingRectH

	newArr = []

	for char in arrChars:
		if(char.boundingRectH > greaterHeight * percentage):
			newArr.append(char)

	return newArr;

def formatPlate(plate_string):
	plate = re.sub("[^0-9a-zA-Z]", "", plate_string)
	return plate

def sortX(char):
	return char.boundingRectX;

def orderByX(arrChars):
	arrChars.sort(key = sortX)
	return arrChars

def applyBitwise_not(char, w, h, percentage):
	# quantity_pixel = h*2 + w*2
	quantity_pixel = w
	quantity_black = 0

	counter = 0;
	# count horizontal top
	while (counter < w):
		if( char[0,counter] == 255):
			quantity_black += 1 
		counter += 1

	if(quantity_black > quantity_pixel * 0.8):
		return cv2.bitwise_not(char)
	else:
		return char

def resizeChar(char, expectedHeight):
	
    image = char

    w = image.size[0]
    h = image.size[1]
    h_aspectRatio = float(expectedHeight) / float(h)
    expectedWidth = int((w * h_aspectRatio))

    return image.resize((expectedWidth, expectedHeight), Image.ANTIALIAS)


def checkPlateText(text):
	text = re.sub("\s", "", text);
	if(len(text) >= 7):
		return True;
	else:
		return False;
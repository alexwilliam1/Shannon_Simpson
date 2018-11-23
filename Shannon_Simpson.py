import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
from array import array
from math import log as ln

def main():
	img = cv.imread('/home/alex/Documentos/TCC2/melanoma2.jpg',0)
	percorre(img) 
	print(img.size) #Total de Pixels
	print(img.shape) #Dimensoes X,Y
	cv.imshow('Imagem1',img)
	cv.waitKey(0)

def percorre(img):
	vetor = []
	for x in range(256):
		vetor.append(0)

	for i in range(0,img.shape[0]):
		for j in range(0,img.shape[1]):
			pixel = img.item(i, j)
			#print(pixel)
			vetor[pixel] += 1

	for a in range(0,256):
		print("Nível {0} ===> {1}p" .format(a, vetor[a]))

	X = shannon(vetor,img)
	D = simpson(vetor,img)

	print("\nShannon index:: ",round(X, ndigits=6))
	print("Simpson index: ",round(D, ndigits=6))

def shannon(data,img):
	def p(n,N):
		if n is 0:
			return 0
		else:
			return (float(n)/N)*ln(float(n/N),10)

	return -sum(p(data[i],img.size) for i in range(256) if data[i] is not 0)

def simpson(data,img):
	def p(n, N):
		if n is 0:
			return 0
		else:
			return (float(n/N) ** 2)

	return 1-(sum(p(data[n],img.size) for n in range(len(data)) if data[n] is not 0))

main()
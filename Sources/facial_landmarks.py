# USAGE
# python facial_landmarks.py --shape-predictor shape_predictor_68_face_landmarks.dat --image images/example_01.jpg 

# import the necessary packages
from imutils import face_utils
from math import *
import numpy as np
import argparse
import imutils
import dlib
import cv2
import glob
from PIL import Image

# construct the argument parser and parse the arguments
#ap = argparse.ArgumentParser()
#ap.add_argument("-p", "--shape-predictor", required=True,
#	help="path to facial landmark predictor")
#ap.add_argument("-i", "--image", required=True,
#	help="path to input image")
#args = vars(ap.parse_args())

#déclaration des fonctions qui seront utilisées

#cette fonction retourne un tableau contenant les distances entre chaque points du visage
def distances(shape):
	#i=0
	tab_new_shape = []
	tab_differences = []
	for (i) in (shape):
		tab_new_shape.append(i)
	tab_differences.append(sqrt(pow((tab_new_shape[17][0]-tab_new_shape[21][0]),2)+pow((tab_new_shape[17][1]-tab_new_shape[21][1]),2)))
	tab_differences.append(sqrt(pow((tab_new_shape[21][0]-tab_new_shape[22][0]),2)+pow((tab_new_shape[21][1]-tab_new_shape[22][1]),2)))
	tab_differences.append(sqrt(pow((tab_new_shape[22][0]-tab_new_shape[26][0]),2)+pow((tab_new_shape[22][1]-tab_new_shape[26][1]),2)))
	tab_differences.append(sqrt(pow((tab_new_shape[26][0]-tab_new_shape[16][0]),2)+pow((tab_new_shape[26][1]-tab_new_shape[16][1]),2)))
	tab_differences.append(sqrt(pow((tab_new_shape[0][0]-tab_new_shape[36][0]),2)+pow((tab_new_shape[0][1]-tab_new_shape[36][1]),2)))
	tab_differences.append(sqrt(pow((tab_new_shape[36][0]-tab_new_shape[39][0]),2)+pow((tab_new_shape[36][1]-tab_new_shape[39][1]),2)))
	tab_differences.append(sqrt(pow((tab_new_shape[39][0]-tab_new_shape[42][0]),2)+pow((tab_new_shape[39][1]-tab_new_shape[42][1]),2)))
	tab_differences.append(sqrt(pow((tab_new_shape[42][0]-tab_new_shape[45][0]),2)+pow((tab_new_shape[42][1]-tab_new_shape[45][1]),2)))
	tab_differences.append(sqrt(pow((tab_new_shape[45][0]-tab_new_shape[16][0]),2)+pow((tab_new_shape[45][1]-tab_new_shape[16][1]),2)))
	tab_differences.append(sqrt(pow((tab_new_shape[27][0]-tab_new_shape[31][0]),2)+pow((tab_new_shape[27][1]-tab_new_shape[31][1]),2)))
	tab_differences.append(sqrt(pow((tab_new_shape[32][0]-tab_new_shape[36][0]),2)+pow((tab_new_shape[32][1]-tab_new_shape[36][1]),2)))
	tab_differences.append(sqrt(pow((tab_new_shape[33][0]-tab_new_shape[51][0]),2)+pow((tab_new_shape[33][1]-tab_new_shape[51][1]),2)))
	tab_differences.append(sqrt(pow((tab_new_shape[57][0]-tab_new_shape[8][0]),2)+pow((tab_new_shape[57][1]-tab_new_shape[8][1]),2)))
	tab_differences.append(sqrt(pow((tab_new_shape[0][0]-tab_new_shape[16][0]),2)+pow((tab_new_shape[0][1]-tab_new_shape[16][1]),2)))
	tab_differences.append(sqrt(pow((tab_new_shape[5][0]-tab_new_shape[11][0]),2)+pow((tab_new_shape[5][1]-tab_new_shape[11][1]),2)))
	tab_differences.append(sqrt(pow((tab_new_shape[51][0]-tab_new_shape[62][0]),2)+pow((tab_new_shape[51][1]-tab_new_shape[62][1]),2)))
	tab_differences.append(sqrt(pow((tab_new_shape[66][0]-tab_new_shape[57][0]),2)+pow((tab_new_shape[66][1]-tab_new_shape[57][1]),2)))
	

				
	return tab_differences
	
#cette fonction prend deux tableaux et compare leurs valeurs
def differences(tabt, tabe, ratio_visage, ratio_reference):
	
	moy=0
	for (i) in range(len(tabt)) :
		if (tabt[i]==0 or tabe[i] ==0):
			moy = moy + max(tabt[i]/ratio_visage,tabe[i]/ratio_reference)
		else :
			moy=moy+fabs(max((tabt[i]/ratio_visage),(tabe[i]/ratio_reference))/min((tabt[i]/ratio_visage),(tabe[i]/ratio_reference)))
		
	i=i+1
	moy=moy/i
	
	return moy

def start(apprendre, test_fiabilité):

	# initialize dlib's face detector (HOG-based) and then create
	# the facial landmark predictor
	detector = dlib.get_frontal_face_detector()
	#on donne le shape-predictor par défaut car il n'y en a qu'un
	predictor = dlib.shape_predictor("Shape_Predictors/shape_predictor_68_face_landmarks.dat")

	reconnaissance = True
	fiabilité = 1
	stats = 1
	Last_Visage = "???"
	
	#on récupère l'ensemble des longueurs de tous les visages
	tab_all_shapes = []
	tab_names = []
	tab_ratio = []
	for (itest) in (glob.glob("images\*")) : 
				
				imagetest = cv2.imread(itest)
				imagetest = imutils.resize(imagetest, width=500)
				graytest = cv2.cvtColor(imagetest, cv2.COLOR_BGR2GRAY)
				rectstest = detector(graytest, 1)
				for (i2, rect) in enumerate(rectstest):
					ratio = rect.width()/100
					# determine the facial landmarks for the face region, then
					# convert the facial landmark (x, y)-coordinates to a NumPy
					# array
					shapetest = predictor(graytest, rect)
					shapetest = face_utils.shape_to_np(shapetest)
					"""
					# convert dlib's rectangle to a OpenCV-style bounding box
					# [i.e., (x, y, w, h)], then draw the face bounding box
					(x, y, w, h) = face_utils.rect_to_bb(rect)
					cv2.rectangle(imagetest, (x, y), (x + w, y + h), (0, 255, 0), 2)

					# show the face number
					cv2.putText(imagetest, "Face #{}".format(i + 1), (x - 10, y - 10),
						cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

					# loop over the (x, y)-coordinates for the facial landmarks
					# and draw them on the image
					for (x, y) in shapetest:
						cv2.circle(imagetest, (x, y), 1, (0, 0, 255), -1)
					"""	
				
					#on récupère les points du visage auquel on le compare
					
					tab_all_shapes.append(distances(shapetest))
					
					name=itest.split("#")[0][7:]
					
					tab_names.append(name)
					
					tab_ratio.append(ratio)
		
	cam = cv2.VideoCapture(0);
	
	while (reconnaissance == True) :
		
		ret_val, image = cam.read()
		
		
		

		# load the input image, resize it, and convert it to grayscale
		#on donne pour l'instant une image choisie arbitrairement, il faudra par la suite réucpérer ici l'image reçu par la caméra
		#image = cv2.imread("images\example_04.jpg")
		#image = imutils.resize(image, width=500)
		image = imutils.resize(image, width=500)
		
		gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

		visage = "???"
		

		# detect faces in the grayscale image
		rects = detector(gray, 1)

		# loop over the face detections
		for (i, rect) in enumerate(rects):
			ratio = rect.width()/100
			# determine the facial landmarks for the face region, then
			# convert the facial landmark (x, y)-coordinates to a NumPy
			# array
			shape = predictor(gray, rect)
			shape = face_utils.shape_to_np(shape)
			
			
			"""
			# loop over the (x, y)-coordinates for the facial landmarks
			# and draw them on the image
			for (x, y) in shape:
				cv2.circle(image, (x, y), 1, (0, 0, 255), -1)
			"""
			#on récupère les distances entre les points du visage à étudier
			tabt = distances(shape)
			
			visage = "????"
			
			temp = -1;
			face=0;
			res=False
			for i in range (len(tab_all_shapes)):
				#on récupère la comparaison entre tous ces points
				moy = differences(tabt, tab_all_shapes[i], ratio, tab_ratio[i])
				if (moy <= 1.4):
					
					if(temp == -1 or moy<temp):
						temp=moy
						res = True
						
						

						visage = tab_names[face]
							
					
				face+=1
				
			if (apprendre != 0):
				if (visage!=apprendre and visage != "????" ):
					print(visage)
					id=1
					
					for i in (glob.glob("images\*")):
						name=i.split("#")[0][7:]
						if (name==apprendre):
							id+=1
					
					im = Image.fromarray(image)
					im.save("images/"+apprendre+"#"+str(id)+".PNG")
					reconnaissance = False

						
				
				
			

				

			

			
		
		# convert dlib's rectangle to a OpenCV-style bounding box
		# [i.e., (x, y, w, h)], then draw the face bounding box
		image = imutils.resize(image, width=800)
		(x, y, w, h) = face_utils.rect_to_bb(rect)
		image = imutils.resize(image, width=500)
		
		cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

		# show the face number
		if test_fiabilité != 0 :
			if (visage == test_fiabilité and visage != "???") :
				fiabilité = fiabilité+1
			if stats != 0:
				cv2.putText(image, visage+"    fiabilite ="+str(int((fiabilité/stats)*100))+"%", (x - 10, y - 10),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
			if visage !="???" :
				stats+=1
		else :
			cv2.putText(image, visage, (x - 10, y - 10),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
		# show the output image with the face detections
		image = imutils.resize(image, width=800)
		cv2.imshow('Reconnaissance Faciale',image)
		
		if cv2.waitKey(1) == 27:
			break
	cv2.destroyAllWindows()

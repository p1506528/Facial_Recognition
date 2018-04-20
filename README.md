# Facial_Recognition

This project takes images from a camera, searches for faces in them then tries to recognize those faces.
You can start it by running the launch.sh file.
When you run the launch.sh file, a Tkinter window opens. It contains three menus, each one standing for one functionnality of the project.

"Lancer la Reconnaissance" is a the project itself.
The program tries to recognize whoever is in front of the camera and can recognize several faces at the same time.

"Faire des Statistiques" is used when we want to compare differents methods to recognize faces.
It runs the project exept that you have to give the name of the person standing in front of the camera, the program will then tell you how many times he got the expected results.

"Enregistrer un visage" allows you to save another face. You need to give the name of the person standing in front of the camera then, if the program doesn't know this person yet,
it will save it. It will be able to recognize this face in the future.

The code is organized in several directories : 
	- Shape_Predictors contains the pre-trained shape predictors that place the 68 landmarks on the faces.
	- Sources contains the file facial_landmarks.py in which are coded the functions used in the project.
	- images contains the differents faces currently saved in the project.
The file Tkinter.py is the file in which we coded the graphical interface.
The file launch.sh just run the Tkinter.py file.

To run this project, you need to have python 3, opencv, imutils and dlib installed on your machine.
To install Python 3, an easy way is to install Anaconda 3 : https://www.anaconda.com/download/
To install dlib, you can download the latest Python Wheel (.whl) file at https://pypi.org/simple/dlib/ and pip install it (cmd : pip install dlib-file.whl)
Opencv and Imutils can be pip installed (cmd : pip install imutils opencv-contrib-python)

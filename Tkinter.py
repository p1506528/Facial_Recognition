from Sources.facial_landmarks import *
from tkinter import *



def Statistiques():
	fenTemp = Tk()
	fenTemp['bg']='white'
	
	mainFrame = Frame(fenTemp, bg="white")
	btFrame = Frame(mainFrame, bg="white")
	entryFrame = Frame(mainFrame, bg = "white")
	prenomFrame = Frame(entryFrame, bg = "white")
	nomFrame = Frame(entryFrame, bg = "white")
	
	
	titremainFrame = Label(mainFrame, text="Indiquez la personne à reconnaître", font="Arial 15", bg="white")
	prenom = Label(prenomFrame, text="Prénom", font="Arial 12", bg ="white")
	prenomEntry = Entry(prenomFrame, justify=CENTER, font ="Arial 12", bg="LavenderBlush2", width = 10)
	nom = Label(nomFrame, text="Nom", font = "Arial 12", bg="white")
	nomEntry = Entry(nomFrame, justify=CENTER, font ="Arial 12", bg="LavenderBlush2", width = 10)
	
	validateBt = Button(btFrame, text="Valider", bg='violet', activebackground='medium orchid', highlightbackground='orange', highlightcolor='orange', font="Arial 15", command = lambda: start(0,prenomEntry.get()+"_"+nomEntry.get()))
	quitBtmainFrame = Button(btFrame, text = "Quitter",bg='orange red', font="Arial 15", activebackground='red',  command=fenTemp.destroy)
	
	
	titremainFrame.pack(pady=10, side = TOP)
	
	prenom.pack(pady = 20, padx = 20, side = LEFT)
	prenomEntry.pack(pady = 20,  side = LEFT)
	
	nomEntry.pack(pady = 20, padx = 20, side = RIGHT)
	nom.pack(pady = 20, side = RIGHT)
	
	
	quitBtmainFrame.pack(pady = 15, padx=30, side=RIGHT)
	validateBt.pack(padx=100, side=LEFT)
	
	
	prenomFrame.pack(side = LEFT, padx = 50)
	nomFrame.pack(side = RIGHT, padx = 50)
	entryFrame.pack(side = TOP)
	btFrame.pack(side = BOTTOM)
	mainFrame.pack()
	
	fenTemp.mainloop()

def Apprendre():
	fenTemp = Tk()
	fenTemp['bg']='white'
	
	mainFrame = Frame(fenTemp, bg="white")
	btFrame = Frame(mainFrame, bg="white")
	entryFrame = Frame(mainFrame, bg = "white")
	prenomFrame = Frame(entryFrame, bg = "white")
	nomFrame = Frame(entryFrame, bg = "white")
	
	
	titremainFrame = Label(mainFrame, text="Indiquez la personne à enregistrer", font="Arial 15", bg="white")
	prenom = Label(prenomFrame, text="Prénom", font="Arial 12", bg ="white")
	prenomEntry = Entry(prenomFrame, justify=CENTER, font ="Arial 12", bg="LavenderBlush2", width = 10)
	nom = Label(nomFrame, text="Nom", font = "Arial 12", bg="white")
	nomEntry = Entry(nomFrame, justify=CENTER, font ="Arial 12", bg="LavenderBlush2", width = 10)
	
	validateBt = Button(btFrame, text="Valider", bg='deep sky blue', activebackground='DeepSkyBlue2', highlightbackground='orange', highlightcolor='orange', font="Arial 15", command = lambda: start(prenomEntry.get()+"_"+nomEntry.get(),0))
	quitBtmainFrame = Button(btFrame, text = "Quitter",bg='orange red', font="Arial 15", activebackground='red',  command=fenTemp.destroy)
	
	
	titremainFrame.pack(pady=10, side = TOP)
	
	prenom.pack(pady = 20, padx = 20, side = LEFT)
	prenomEntry.pack(pady = 20,  side = LEFT)
	
	nomEntry.pack(pady = 20, padx = 20, side = RIGHT)
	nom.pack(pady = 20, side = RIGHT)
	
	
	quitBtmainFrame.pack(pady = 15, padx=30, side=RIGHT)
	validateBt.pack(padx=100, side=LEFT)
	
	
	prenomFrame.pack(side = LEFT, padx = 50)
	nomFrame.pack(side = RIGHT, padx = 50)
	entryFrame.pack(side = TOP)
	btFrame.pack(side = BOTTOM)
	mainFrame.pack()
	
	fenTemp.mainloop()



fenetre = Tk()
fenetre['bg']='white'


mainFrame = Frame(fenetre, bg="white")


titremainFrame = Label(mainFrame, text="Reconnaissance Faciale", font="Arial 30", bg="white")
standartBt = Button(mainFrame, text = "Lancer Reconnaissance",bg='chartreuse2', activebackground='chartreuse3', highlightbackground='orange', highlightcolor='orange', borderwidth=6, height=5, width=30, font="Arial 22", command=lambda: start(0,0))
statistiquesBt = Button(mainFrame, text = "Faire des statistiques",bg='violet', activebackground='medium orchid', highlightbackground='orange', highlightcolor='orange', borderwidth=6, height=5, width=30, font="Arial 22", command= Statistiques)
apprendreBt = Button(mainFrame, text = "Enregistrer un visage",bg='deep sky blue', activebackground='DeepSkyBlue2', highlightbackground='orange', highlightcolor='orange', borderwidth=6, height=5, width=30, font="Arial 22", command=Apprendre)
quitBtmainFrame = Button(mainFrame, text = "Quitter",bg='orange red', font="Arial 12", activebackground='red',  command=fenetre.destroy)

titremainFrame.pack(pady=10, side=TOP)
standartBt.pack(pady=30, side = TOP)
statistiquesBt.pack(pady=10, side = TOP)
apprendreBt.pack(padx = 100, pady=30, side = TOP)

quitBtmainFrame.pack(pady=10, side=BOTTOM)

mainFrame.pack()
fenetre.mainloop()    



import os, sys, time, fcntl, serial
from tkinter import *
# Here come the IHM or UI

def unPetitLog():
	print("COUCOU MON CHOU")
	pass

class IHM:
	"""docstring for IHM"""
	def __init__(self, frame):
		self.frame = frame
		frame.title("Projet S.A.S. Dashboard")

		self.label = Label(frame, text="Projet S.A.S. Dashboard", fg="white", bg="black")
		self.label.pack(side=TOP)

		paneTop = Frame(frame)
		paneTop.pack(side=LEFT)

		paneMiddle = Frame(frame)
		paneMiddle.pack(side=LEFT)

		paneLeft = Frame(frame)
		paneLeft.pack(side=LEFT)

		value = IntVar()
		self.sliderTemp = Checkbutton(paneLeft, text="Checked?", variable=value)
		self.sliderTemp.pack()

		self.sliderLum = Scale(paneMiddle, from_=100, to_=0)
		self.sliderLum.pack()

		self.sliderPre = Scale(paneTop, from_=100, to_=0)
		self.sliderPre.pack()

		self.printBu = Button(frame, text="PRINT DAT SHIT", command=unPetitLog)
		self.printBu.pack()


frame = Tk()

IHM = IHM(frame)

frame.mainloop()
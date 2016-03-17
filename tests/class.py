class Temp:
	
	"""docstring for Temp"""

	def __init__(self, interieur = 0.0, exterieur = 0.0):
		super(Temp, self).__init__()
		self.interieur = interieur
		self.exterieur = exterieur
	
	def diff(self):
			print("il fait : " + (str(round(self.interieur - self.exterieur, 2))) + " degres de plus à l'interieur que dehors.")
			pass

Temp = Temp(22.3, 14.7)
Temp.diff() # print "il fait : 7.6 degres de plus à l'interieur que dehors."
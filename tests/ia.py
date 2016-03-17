class sasIa:
	"""docstring for sasIa"""
	def __init__(self):
		super(sasIa, self).__init__()



# joke.
class coffee:
	"""docstring for coffee"""
	def __init__(self, cafeine = 100, sugar=0, withLove=True, name="buddy"):
		super(coffee, self).__init__()
		self.cafeine = cafeine
		self.sugar = sugar
		self.withLove = withLove
		self.name = name

	def drink(self):
		print("Here come your coffee " + str(self.name) + ", with " + str(self.sugar) + " sugar, " + str(self.cafeine) + "% cafeine.")
		if self.withLove:
			print("made with <3 by keikyoku !")
			pass
		pass
		

coffee = coffee(100, 0, True, "M.benjamin")
coffee.drink()
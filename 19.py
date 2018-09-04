name = None

class Test:
	def __init__(self, newName):
		self.name = newName
		global name
		name = "Global " + newName

	def print_names(self):
		print(name)
		print(self.name)
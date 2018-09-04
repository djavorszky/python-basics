class Car(object):
	def __init__(self, horsePower):
		self.horsePower = horsePower

	def printHorsePower(self):
		pass


class BMW(object):
	def __init__(self, horsePower):
		super().__init__(horsePower)

	def printHorsePower(self):
		print(self.horsePower)


car = BMW(300)
car.printHorsePower()
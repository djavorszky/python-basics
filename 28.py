class Car():
	def __init__(self, horsePower):
		self.horsePower = horsePower

	def print_horsepower(self):
		pass


class BMW(Car):
	def __init__(self, horsePower):
		super().__init__(horsePower)

	def print_horsepower(self):
		print(self.horsePower)


car = BMW(300)
car.print_horsepower()
def do_something(something):
	print("Doing " + str(something))

class Test:
	def do_something(self, something):
		self.__do_it(something)

	def __do_it(self, something):
		print("Doing " + str(something))
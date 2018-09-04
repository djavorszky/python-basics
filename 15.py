def doSomething(something):
	print("Doing " + str(something))

class Test:
	def doSomething(self, something):
		self.__doIt(something)

	def __doIt(self, something):
		print("Doing " + str(something))
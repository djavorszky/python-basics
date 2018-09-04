import sys

something = False

if(something is True):
	pass
elif(something is False):
	raise Exception
elif(something is None):
	sys.exit(0)
else:
	sys.exit(1)
try:
	username = sys.argv[1]
	chip 	 = sys.argv[2]
	region	 = sys.argv[3]

except Exception:
	print("The argument list is invalid!")
	sys.exit(0)
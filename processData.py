def processData(Input):
	print("[process] input : " + str(Input))
	dataIn = Input.split('_')
	global temp
	temp = float(dataIn[0])
	global lum
	lum = float(dataIn[1])
	pass
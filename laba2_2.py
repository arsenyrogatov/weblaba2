def isDiv(d, args):
	result = []
	for i in args:
		if i % d == 0:
			result.append(i)
	return result

def getNum(*args):
	result = []
	result.append(isDiv(2,args))
	result.append(isDiv(3,args))
	result.append(isDiv(5,args))
	return result

a = getNum(1,2,3,4,5,6,7,8,9,10)
for i in a:
	for j in i:
		print(j)
	print ("\n")
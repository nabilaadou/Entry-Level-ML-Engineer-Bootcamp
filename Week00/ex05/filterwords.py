import sys

punctuationMarks = ['!', "," ,"\'" ,";" ,"\"", ".", "-" ,"?"]

def ft_filter(arg:str, n):
	arg = arg.translate({ord(i): None for i in punctuationMarks})
	list = arg.split()
	ans_list = []

	for i in list:
		if  len(i) >= n:
			ans_list.append(i)
	print(ans_list)


if __name__ == "__main__":
	try:
		assert len(sys.argv) == 3, "ERROR: wrong number of args"
		# assert sys.argv[1] is str, "ERROR: first arg is not a string" 
		# assert sys.argv[2] is int, "ERROR: second arg is not an in"
		print(sys.argv)
		ft_filter(sys.argv[1], int(sys.argv[2]))
	except AssertionError as msg:
		print(msg)
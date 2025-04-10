import sys

def text_analyzer(arg=None):
	'''This function counts the number of upper characters, lower characters,
	punctuation and spaces in a given text.'''
	upperLen = 0
	lowerLen = 0
	punctuationMarks = ['!', "," ,"\'" ,";" ,"\"", ".", "-" ,"?"]
	punctuationLen = 0
	spacesLen = 0
	digitsLen = 0
	# arg = input("What is the text to count?\n") if ac == 1 else av[1]
	if arg == None:
		arg = input("What is the text to count?\n")
	try:
		assert type(arg) is str, "argument is not a string"
		for i in arg:
			if i.isupper():
				upperLen += 1
			elif i.islower():
				lowerLen += 1
			elif i in punctuationMarks:
				punctuationLen += 1
			elif i == ' ':
				spacesLen += 1
			elif i.isdigit():
				digitsLen += 1
		print("The text contains", len(arg), "characters:")
		print(upperLen, "upper letters")
		print(lowerLen, "lower letters")
		print(punctuationLen, "punctuation marks")
		print(spacesLen, "spaces")
		print(digitsLen, "digits")
	except AssertionError as msg:
		print(msg)

if __name__ == "__main__":
	try:
		assert len(sys.argv) == 2, "wrong number of arguments"
		text_analyzer(sys.argv[1])
	except AssertionError as msg:
		print(msg)
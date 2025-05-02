import sys

argv = ' '.join(sys.argv[1:])
res = ''

for i in range(len(argv)):
	if argv[i].isalpha():
		if argv[i].isupper():
			res += argv[i].lower()
		else:
			res += argv[i].upper()
	else:
		res += argv[i]
print(res[::-1])
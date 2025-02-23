kata = (19,42,21)
nums = []
for i in kata:
	nums.append(str(i))
aa = ', '.join(nums)
str = "the {tuplesize} numbers are: {nums}".format(tuplesize=len(kata), nums=aa)
print(str)
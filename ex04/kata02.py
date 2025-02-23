kata = (2019, 9, 25, 3, 30)

print("{month}/{day}/{year} {h}:{m}".format(
	month=kata[1] if kata[1] > 9 else "0"+str(kata[1]),
	day=kata[2] if kata[2] > 9 else "0"+str(kata[2]),
	year=kata[0],
	h=kata[3] if kata[3] > 9 else "0"+str(kata[3]),
	m=kata[4] if kata[4] > 9 else "0"+str(kata[4]))
)
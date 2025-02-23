kata = (0, 4, 132.42222, 10000, 12345.67)

n = f"{kata[0]:02d}"
e = f"{kata[1]:02d}"
idk1 = f"{kata[2]:.2f}"
idk2 = "{:e}".format(kata[3])
idk3 = "{:e}".format(kata[4])

ans = "module_{n}, ex_{e} : {idk1}, {idk2}, {idk3}".format(n=n, e=e, idk1=idk1, idk2=idk2, idk3=idk3)
print(ans)
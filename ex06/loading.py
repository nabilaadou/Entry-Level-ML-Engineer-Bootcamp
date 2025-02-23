from time import sleep

def ft_progress(r: range):
	t = len(r)
	for i in r:
		total = f"{(i / t * 100):.2f}"
		print(f"\rETA [{total}%]",end='', flush=True)
		yield


for i in ft_progress(range(20)):
	sleep(0.05)
print()
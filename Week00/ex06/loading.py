from time import sleep

def ft_progress(r: range):
    t = len(r)
    for i in r:
        percent = (i + 1) / t  # Add 1 so bar reaches 100%
        total = f"{percent * 100:.2f}"
        bar_length = 30  # Total length of the bar
        filled_length = int(bar_length * percent)
        bar = '-' * filled_length + '>' + ' ' * (bar_length - filled_length - 1)
        print(f"\r[{bar}] {total}%", end='', flush=True)
        yield


for i in ft_progress(range(500)):
	sleep(0.05)
print()
import itertools
import sys
def take_input(fn):
    return [fn(x) for x in sys.stdin.readline().split()]

t = int(input())
f= 0
for i in range(t):
	chocs = take_input(int)
	chocs = chocs[1:]
	num_children = int(input())
	if num_children in chocs:
		print("YES")
		break
	else:
		for L in range(2, len(chocs)+1):
			for subset in itertools.combinations(chocs, L):
				# print(subset)
				if (sum(subset) == num_children):
					print("YES")
					f = 1
					break
			if (f == 1):
				break
		if (f==0):
			print("NO")

# print()
# print(chocs)
# print(num_children)

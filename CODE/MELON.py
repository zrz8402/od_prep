n = int(input())

stones = list(map(int, input().split()))
total_weight = 0
for stone in stones:
	total_weight += stone

if (total_weight % 2 != 0):
	print(-1)
else:
	target_weight = total_weight / 2

	dp = [0] * (target_weight + 1)
	

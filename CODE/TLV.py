def	get_length(str):
	return int(str, 16)

def main():
	tag = input().strip()

	hex_array = input().strip().split()

	i = 0
	while i < len(hex_array):
		length = get_length(hex_array[i + 2] + hex_array[i + 1])
		if hex_array[i] == tag:
			value = []
			for j in range(i + 3, i + 3 + length):
				value.append(hex_array[j])
			print(" ".join(value).upper().strip())
			break
		else:
			i += (2 + length + 1)

if __name__ == "__main__":
	main()

# print(int("01", 16))
# 32 01 00 AE 90 02 00 01 02 30 03 00 AB 32 31 31 02 00 32 33 33 01 00 CC
# 32 - 01 00 - AE
# 90 - 02 00 - 01 02
# 30 - 03 00 - AB 32 31
# 31 - 02 00 - 32 33
# 33 - 01 00 - CC

def addBinary(a: str, b: str) -> int:
	return bin(int(a, 2) + int(b, 2))[2:]

print(addBinary("11", "1"))
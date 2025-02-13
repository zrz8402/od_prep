def	convert(s: str, numRows: int) -> int:
	if numRows == 1:
		return s
	
	rows = [""] * numRows
	currentRow = 0
	direction = 0
	
	for char in s:
		rows[currentRow] += char
		currentRow += direction
		if currentRow == 0 or currentRow == numRows - 1:
			direction *= -1
	
	return "".join(rows)
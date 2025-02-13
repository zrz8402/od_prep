# expand_around_center method, pay attention to have odd and even

def longest_palindrome(s: str) -> str:
	def expand_around_center(left: int, right: int) -> str:
		while left >= 0 and right < len(s) and s[left] == s[right]:
			left -= 1
			right += 1
		return s[left + 1:right]

	longest = ""
	for i in range(len(s)):
		odd = expand_around_center(i, i)
		even = expand_around_center(i, i + 1)
		longest = max(longest, odd, even, key=len)

	return longest

s = "babad"
print(longest_palindrome(s))


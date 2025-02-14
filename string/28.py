def strStr(haystack: str, needle: str) -> int:
	if not needle:
		return 0
	n = len(haystack)
	m = len(needle)
	for i in range(n - m + 1):
		if haystack[i:i+m] == needle:
			return i
	return -1


# def strStr(haystack: str, needle: str) -> int:
#     if not needle:
#         return 0
    
#     def buildLPS(needle):
#         lps = [0] * len(needle)
#         length = 0
#         i = 1
#         while i < len(needle):
#             if needle[i] == needle[length]:
#                 length += 1
#                 lps[i] = length
#                 i += 1
#             else:
#                 if length != 0:
#                     length = lps[length - 1]
#                 else:
#                     lps[i] = 0
#                     i += 1
#         return lps
    
#     lps = buildLPS(needle)
#     i = 0
#     j = 0
#     while i < len(haystack):
#         if haystack[i] == needle[j]:
#             i += 1
#             j += 1
#         if j == len(needle):
#             return i - j
#         elif i < len(haystack) and haystack[i] != needle[j]:
#             if j != 0:
#                 j = lps[j - 1]
#             else:
#                 i += 1
#     return -1

haystack = "ABABDABACDABABCABAB"
needle = "ABABCABAB"
print(strStr(haystack, needle))
# print(haystack.find(needle))
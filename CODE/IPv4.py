'''
parsing:
	invalid cases:
		not 4 sections
		empty section
		non-digit
		leading 0
		out of range(0-255)

convert
	* 256
'''


def main():
	input_str = input()

	ip_section = input_str.split("#")

	if (len(ip_section) != 4):
		print("invalid IP")
		return
	
	ip_value = 0
	for i in range(4):
		if (len(ip_section[i]) == 0 or not ip_section[i].isdigit()):
			print("invalid IP")
			return
		if (len(ip_section[i]) > 1 and ip_section[i][0] == '0'):
			print("invalid IP")
			return
		if (i == 0):
			if (int(ip_section[i]) < 1 or int(ip_section[i]) > 128):
				print("invalid IP")
				return
		else:
			if (int(ip_section[i]) < 1 or int(ip_section[i]) > 255):
				print("invalid IP")
				return			
		ip_value = ip_value * 256 + int(ip_section[i])
	print(ip_value)

if __name__ == "__main__":
	main()
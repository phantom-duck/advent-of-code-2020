import sys

if __name__=="__main__":
	if len(sys.argv) > 1:
		filename = sys.argv[1]
	else:
		filename = "input.txt"

	with open(filename, "rt") as infile:
		text = infile.read()
	
	text = text.split("\n")
	if text[-1] == "":
		del text[-1]
	text = [line.split() for line in text]
	
	##### for question 1
	# n_valid = 0
	# for data in text:
		# low = int(data[0].split("-")[0])
		# high = int(data[0].split("-")[1])
		# char = data[1][0]
		
		# n_char = 0
		# for letter in data[2]:
			# if letter == char:
				# n_char += 1
		
		# if n_char >= low and n_char <= high:
			# n_valid += 1
	
	##### for question 2
	n_valid = 0
	for data in text:
		pos1 = int(data[0].split("-")[0]) - 1
		pos2 = int(data[0].split("-")[1]) - 1
		char = data[1][0]
		password = data[2]
		
		if (password[pos1] == char and password[pos2] != char) or (password[pos1] != char and password[pos2] == char):
			n_valid += 1
	
	print(n_valid)
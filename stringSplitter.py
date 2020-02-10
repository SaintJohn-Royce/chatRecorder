lines = []

newLines = []

with open('3.txt', 'r', encoding = 'utf-8-sig') as file:

	for line in file:

		lines.append(line.strip())

for line in lines:

	s = line.split(' ')

	str1 = s[0]

	rest = s[1:]

	# this can be better represented as s[0][:5]
	firstHalfStr1 = str1[:5]

	# this can be better represented as s[0][5:]
	secondHalfStr1 = str1[5:]

#with open('returned.txt', 'w', encoding = 'utf-8-sig') as file

	#for line in lines

	#f.write([first])
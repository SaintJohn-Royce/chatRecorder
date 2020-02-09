
def read_file(filename):

	lines = []

	# 'utf-8-sig' is like 'utf-8', but the '-sig' removes the text signature '\ufeff'
	with open(filename, 'r', encoding = 'utf-8-sig') as file:

		for line in file:

			# .strip() removes all of the '\n'
			lines.append(line.strip())

	return lines

def convert(lines):

	new = []

	# declares a variable, but assigns it NO VALUE
	person = None

	for line in lines:

		if line == 'Allen':

			person = 'Allen'

			continue

		elif line == 'Tom':

			person = 'Tom'

			continue

		if person:

			new.append(person + ': ' + line)

	return new

def write_file(filename, new):

	outputTxt = []

	with open(filename, 'w', encoding = 'utf-8-sig') as file:

		for line in new:

			file.write(line + '\n')

def main():

	lines = read_file('input.txt')

	new = convert(lines)

	write_file('output.txt', new)

main()
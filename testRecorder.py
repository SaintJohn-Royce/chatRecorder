#def compose_name():

	#nameList = []

	#amount = input('how many people are involved in this conversation? ')

	#amount = int(amount)

	#for index in range(amount):

		#names = input('please input the name of the person number ' + str(index + 1) + ': ')

		#nameList.append(names)

	#return nameList

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

	with open(filename, 'w', encoding = 'utf-8-sig') as file:

		for line in new:

			file.write(line + '\n')

def main():

	#nameList = compose_name()

	lines = read_file('input.txt')

	new = convert(lines)

	write_file('output.txt', new)

main()
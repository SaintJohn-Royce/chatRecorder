def read_file(filename):

	lines = []

	# 'utf-8-sig' is like 'utf-8', but the '-sig' removes the text signature '\ufeff'
	with open(filename, 'r', encoding = 'utf-8-sig') as file:

		for line in file:

			# .strip() removes all of the '\n'
			lines.append(line.strip())

	return lines

def convert(lines):

	# declares a variable, but assigns it NO VALUE
	person = None

	allen_word_count = 0
	viki_word_count = 0
	allen_sticker_count = 0
	viki_sticker_count = 0
	allen_image_count = 0
	viki_image_count = 0

	for line in lines:

		# note: splitting this way WILL create multiple strings in one bracket
		s = line.split(' ')

		time = s[0]

		name = s[1]

		if name == 'Allen':

			if s[2] == '贴图':

				allen_sticker_count += 1

			elif s[2] == '图片':

				allen_image_count += 1

			else:

				for msg in s[2:]:

					allen_word_count += len(msg)

		elif name == 'Viki':

			if s[2] == '贴图':

				viki_sticker_count += 1

			elif s[2] == '图片':

				viki_image_count += 1

			else:

				for msg in s[2:]:

					viki_word_count += len(msg)

	print([allen_word_count, allen_image_count, allen_sticker_count])

	print([viki_word_count, viki_image_count, viki_sticker_count])

def write_file(filename, new):

	with open(filename, 'w', encoding = 'utf-8-sig') as file:

		for line in new:

			file.write(line + '\n')

def main():

	lines = read_file('-LINE-Viki.txt')

	new = convert(lines)

	# write_file('output.txt', new)

main()
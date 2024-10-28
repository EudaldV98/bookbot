with open('books/frankenstein.txt', 'r') as file:
	text = file.read()
	print("--- Begin report of books/frankenstein.txt ---")
	words = text.split()
	print("{} words found in the document".format(len(words)))
	character_counts = {}
	for character in text:
		if character in character_counts:
			character_counts[character] += 1
		else:
			character_counts[character] = 1
	# print(character_counts)
	for character, count in character_counts.items():
		if character == '\n':
			print("The newline character was found {} times".format(count))
		else:
			print("The {} character was found {} times".format(character, count))
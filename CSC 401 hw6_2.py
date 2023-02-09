#Lukasz Grzybek
def wordSearch(fname, wordLst):
	word_dict = {}
	number = []
	for word in wordLst:
		word_dict[word] = number
	ct = 0
	from string import punctuation
	p = punctuation.replace("'", " ")

	while True:
		infile = open(fname,'r')
		content = infile.readline()
		infile.close()

		ct += 1
		transTable = content.maketrans(punctuation, ' '*len(punctuation))
		s = content.translate(transTable)

		for word in wordLst:
			if word in s:
				number.append(ct)
	
	if word in word_dict.keys():
		print(word, number)
	else:
		print('{} is not in the dictionary'.format(word))




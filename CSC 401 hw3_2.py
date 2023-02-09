#Lukasz Grzybek

def wordGame():
    fname = 'Pride_and_Prejudice.txt'
    infile = open(fname, 'r')
    strContents = infile.read()
    infile.close()
    
    p = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    for c in p:
    	if c in strContents:
    		strContents = strContents.replace(c, ' ')
    wordList = strContents.split()
    
    import random

    wordOne = random.choice(wordList)
    wordOne = wordOne.lower()
    amountOne = strContents.count(wordOne)
    
    wordTwo = random.choice(wordList)
    wordTwo = wordTwo.lower()
    amountTwo = strContents.count(wordTwo)
    
    if wordOne != wordTwo:
    	x = input('Which word did the writer use more often ' + '"{}"'.format(wordOne) + ' or ' + '"{}"'.format(wordTwo) + '?')
    

    if amountOne > amountTwo:
    	if x == wordOne:
    		print(' ' + wordOne + ' you are correct')
    	elif x == wordTwo:
    		print(' ' + wordTwo + ' you are incorrect')
    if amountOne < amountTwo:
    	if x == wordOne:
    		print(' ' + wordOne + ' you are incorrect')
    	elif x == wordTwo:
    		print(' ' + wordTwo + ' you are correct')
    if wordOne == wordTwo:
    	x = 'Chosen words are the same'
    	print(x)
    if amountOne == amountTwo and wordOne != wordTwo:
    	num = amount_One
    	print('Each word has ' + num + ' occurences.')
    print('Verification: ' + '"{}"'.format(wordOne) + ' occurs ' + str(amountOne) + ' times, ' + '"{}"'.format(wordTwo) + ' occurs ' + str(amountTwo) + ' times.')









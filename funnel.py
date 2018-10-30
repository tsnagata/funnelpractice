source = 'apple'

def funnel(word, word2):
	i = 0
	istrue = False

	while (i<=len(word)):
		word1 = word[0:i]+word[i+1:len(word)]
		istrue = (word1 == word2) or False or istrue
		i += 1

	print(istrue)


def funnelbonus(word):
	with open('C:/Users/tsnag/Desktop/wordlist.txt', 'r') as wordfile:
		wordlist = wordfile.read().splitlines()
		
		out = []
		wordperms = []
		i = 0

		while (i<len(word)):
			wordperms = wordperms + [str(word[0:i]+word[i+1:len(word)])]
			i += 1

		for words in wordlist:
			if (words in wordperms):
				out.append(words)

		print(out)


funnelbonus(input('Enter a word: '))
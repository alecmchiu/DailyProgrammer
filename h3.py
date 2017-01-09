#!/Users/Alec/anaconda/bin/python

'''
Challenge H3
https://www.reddit.com/r/dailyprogrammer/comments/pkwgf/2112012_challenge_3_difficult/
'''

txt = open('h3_wordlist.txt','r')
word_list = []

for line in txt:
	word_list.append(line.strip())

txt.close()

txt = open('h3_unscramble.txt','r')
unscramble = []

for line in txt:
	unscramble.append(line.strip())
txt.close()

for garble in unscramble:
	garble_letters = sorted(list(garble))
	for potential in word_list:
		potential_letters = sorted(list(potential))
		if (garble_letters == potential_letters):
			print garble, potential

#!/Users/Alec/anaconda/bin/python
# -*- coding: utf-8 -*-

#Challenge E279 - Uuencoding
#https://www.reddit.com/r/dailyprogrammer/comments/4xy6i1/20160816_challenge_279_easy_uuencoding/

def encode(string,file_out):

	print 'begin 644 ' + file_out

	interval_string = [string[i:i+45] for i in range(0,len(string),45)]

	for each in interval_string:
		full_line = ''
		for i in range(0,len(each),3):
			section = each[i:i+3]
			bits = ''.join([bin(ord(x))[2:].zfill(8) for x in list(section)])
			groupings = [chr(int(bits[j:j+6],2)+32) for j in range(0,len(bits),6)]
			full_line = full_line + ''.join(groupings)
		print chr(int(len(each))+32) + full_line

	print '`\nend'

if __name__=='__main__':
	s = 'I feel very strongly about you doing duty. Would you give me a little more documentation about your reading in French? I am glad you are happy — but I never believe much in happiness. I never believe in misery either. Those are things you see on the stage or the screen or the printed pages, they never really happen to you in life.'
	encode(s,'file.txt')

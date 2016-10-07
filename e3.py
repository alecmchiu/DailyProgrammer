#!/Users/Alec/anaconda/bin/python

# Challenge E3
# https://www.reddit.com/r/dailyprogrammer/comments/pkw2m/2112012_challenge_3_easy/

def encrypt(text):
	characters = list(text)
	#new_chars = [chr(((ord(x)+824)%95)+32) for x in characters]
	new_chars = []
	for each in characters:
		new = ord(each)+22
		if (new < 127):
			new_chars.append(chr(new))
		else:
			new=(new%127)+32
			new_chars.append(chr(new))
	encrypted = ''.join(new_chars)
	return encrypted

def decrypt(text):
	characters = list(text)
	new_chars = []
	for each in characters:
		new = ord(each)
		if (new < 54):
			new = (new-32)+127
		new=new-22
		new_chars.append(chr(new))
	decrypted = ''.join(new_chars)
	return decrypted

if __name__=='__main__':
	text = 'I am not a couch potato! I am a full potato!'
	e = encrypt(text)
	print e
	print decrypt(e)
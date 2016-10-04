#!/Users/Alec/anaconda/bin/python

# https://www.reddit.com/r/dailyprogrammer/comments/pjbj8/easy_challenge_2/

print 'Force Calculator'
print 'Please put x for the missing variable.'
print 'F = M * A'

F = raw_input('F? ')
M = raw_input('M? ')
A = raw_input('A? ')

if (F == 'x'):
	print float(M)*float(A)
elif (M == 'x'):
	print float(F)/float(A)
else:
	print float(F)/float(M)

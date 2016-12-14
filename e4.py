#!/Users/Alec/anaconda/bin/python

# Challenge - E4
# https://www.reddit.com/r/dailyprogrammer/comments/pm6oj/2122012_challenge_4_easy/

import random
import string

length = int(raw_input("What is the length of the passwords? "))
number_passwords = int(
    raw_input("How many passwords do you want to generate? "))

for i in range(number_passwords):
    password = ''
    for j in range(length):
        password = password + \
            random.choice(string.digits + string.ascii_letters)
    print password

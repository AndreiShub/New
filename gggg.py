import string
import random


def pass_gen(size = 9, chars = string.ascii_letters + string.digits + string.punctuation):
	return ''.join(random.choice(chars) for i in range(size))


def check_pass(str):
	for i in range(len(str) - 1):
		if str[i] == str[i + 1]:
			return False
	if any(ch.isupper() for ch in str) and\
		any(ch.islower() for ch in str) and\
		any(ch.isdigit() for ch in str) and\
		any(ch in string.punctuation for ch in str):
		return True
	return False


passw = pass_gen()
print(passw)
print(check_pass(passw))



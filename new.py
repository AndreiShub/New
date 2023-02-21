import random
# temper = [[random.randrange(0, 50) for hour in range(24)] for day in range(30)]
# count = 0
# for i in temper:
# 	if i[15] >= 40:
# 		count += 1
#
# print(lst1)
# cn = 0
# for i in lst1:
# 	for j in i:
# 		for x in j:
# 			if x:
# 				cn += 1
# lst1 = [[[random.randrange(0, 2) for i in range(20)] for j in range(30)] for x in range(3)]
#
#
# def count(lst, a = 0, b = 0):
# 	x = 0
# 	for f in lst[a][b]:
# 		if f:
# 			x += 1
# 	return x
#
#
# print(count(lst1))


def fib(x):
	if x < 2:
		return x
	else:
		return fib(x - 1) + fib(x - 2)


print(fib(10))

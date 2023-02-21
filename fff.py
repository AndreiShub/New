import random

# def func(arg, fun):
# 	for i in arg:
# 		print(f"f({i}) = {fun(i)}")
# print(temp, end = " ")
#
# func([x for x in range(-4, 4)], lambda x: x * x)

# lst = list(map(lambda x: x ** 2, [i for i in range(6)]))

lstt = [random.randint(0, 100) for i in range(10)]


def func(lst):
	x = 0
	result = 1000
	for i in range(90):
		summ = 0
		for j in range(10):
			summ += lst[i + j]
		if summ < result:
			result = summ
			x = i
	return x


def sort(lst):
	flag = len(lst)
	while flag:
		for j in range(len(lst) - 1):
			if lst[j] > lst[j + 1]:
				temp = lst[j]
				lst[j] = lst[j + 1]
				lst[j + 1] = temp
		flag -= 1

print(lstt)
sort(lstt)
print(lstt)

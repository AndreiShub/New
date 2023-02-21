# x = int(input())
# y = int(input())
# print((x + y)+"\n", (x - y), "\n", (x * y), "\n", (x / y), "\n",)

# x = float(input())
# y = float(input())
# print(x / 100 * y)


# if print("1"):
# 	print("true")
# else:
# 	print("false")

import math
while True:
	try:
		x = int(input("Диаметр:"))
		op = int(input("1 - площадь 2 - периметр"))
		if op == 1:
			print(f"Площадь:{math.pi*(x/2)**2}")
			break
		if op == 2:
			print(f"Периметр::{math.pi * x}")
			break
		else:
			continue
	except ValueError:
		print("Введите целое число")


def func():
	try:
		pass
	except ValueError:
		return 1


while func():
	pass

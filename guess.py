import random


def game():
	tries = 0
	max_tries = 10
	answer = random.randint(1, 100)
	print("Угадайте число:")
	while tries < max_tries:
		print(f"Осталось попыток {max_tries - tries}")
		try:
			guess = int(input())
		except ValueError:
			print("Введите число")
			tries += 1
			continue
		if guess == answer:
			print("Угадали!")
			return
		elif guess in range(answer - 10, answer + 10):
			print("Тепло")
			tries += 1
			continue
		elif guess in range(answer - 5, answer + 5):
			print("Горячо!")
			tries += 1
			continue
		else:
			print("Холодно...")
			tries += 1
			continue
	else:
		print("Проиграли!")


game()

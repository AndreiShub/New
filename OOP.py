class Stack:
	def __init__(self):
		self.__list = []
	
	def push(self, coin):
		self.__list.append(coin)
	
	def pop(self):
		coin = self.__list[-1]
		self.__list.pop()
		return coin
	
	def get_list(self):
		return self.__list
	
	
class SummStack(Stack):
	def __init__(self):
		Stack.__init__(self)
		self.__summ = 0
	
	def get_summ(self):
		return self.__summ
	
	def push(self, coin):
		self.__summ += coin
		Stack.push(self, coin)
	
	def pop(self):
		coin = Stack.pop(self)
		self.__summ -= coin
		return coin


class Car:
	__counter = 0
	
	def __init__(self, model = None, year = None, manufacturer = None, capacity = None, color = None, price = None):
		self.__model = model
		self.__year = year
		self.__manufacturer = manufacturer
		self.__capacity = capacity
		self.__color = color
		self.__price = price
		Car.__counter += 1

	def get_counter():
		return Car.__counter

	def get_model(self):
		return self.__model
	
	def get_year(self):
		return self.__year
	
	def get_manufacturer(self):
		return self.__manufacturer
	
	def get_capacity(self):
		return self.__capacity
	
	def get_color(self):
		return self.__color
	
	def get_price(self):
		return self.__price
	
	def change_model(self, i):
		self.__model = i
	
	def change_year(self, i):
		self.__year = i
	
	def change_manufacturer(self, i):
		self.__manufacturer = i
	
	def change_capacity(self, i):
		self.__capacity = i
	
	def change_color(self, i):
		self.__color = i
	
	def change_price(self, i):
		self.__price = i

	def get_all(self):
		lst = [self.__model, self.__year, self.__manufacturer, self.__capacity, self.__color, self.__price]
		return lst


class Drob:
	def __init__(self, chisl = 0, znamen = 0):
		self.__chisl = chisl
		self.__znamen = znamen
	
	def get_chisl(self):
		return self.__chisl
	
	def get_znamen(self):
		return self.__znamen
	
	def change_chisl(self, i):
		self.__chisl = i
		
	def change_znamen(self, i):
		self.__znamen = i
	
	def print_drob(self):
		print(f"{self.__chisl}/{self.__znamen}")
	
	def summ(a, b):
		chisl = a.get_chisl() * b.get_znamen() + b.get_chisl() * a.get_znamen()
		znamen = a.get_znamen() * b.get_znamen()
		return Drob(chisl, znamen)


# drob_1 = Drob(2,3)
# drob_2 = Drob(3, 4)
# drob_1.print_drob()
# drob_2.print_drob()
# Drob.summ(drob_1, drob_2).print_drob()

# car = Car()
# car_2 = Car()
# car_3 = Car()
# car_4 = Car()
# car_5 = Car()
# print(Car.get_counter())

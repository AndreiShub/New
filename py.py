class Car:
	allDir = ["Forward", "Right", "Backward", "Left"]

	def __init__(self, color = "black", wheels = 4):
		self.color = color
		self.wheels = wheels
		self.__dirIndex = 0
		self.dir = Car.allDir[self.dirIndex]

	def turnRight(self):
		print("Машина повернуласть направо")

	def turnLeft(self):
		print("Машина повернуласть налево")

	def getColor(self):
		print(self.color)

	def numbOfWheels(self):
		print(self.wheels)
	
	def getDir(self):
		print(self.dir)


car = Car()
car.getDir()


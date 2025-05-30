class Dog:
	species = "Canine" # Class Attribute

	def __init__(self, name, age):
		self.name = name # Instrance attribute
		self.age = age # instance attribute

dog1 = Dog("To", 4)
dog2 = Dog("Po", 3)
print(f"dog1 name: {dog1.name}, alter: {dog1.age}")
print(f"dog2 name: {}, dog2.alter: {dog2.age}")



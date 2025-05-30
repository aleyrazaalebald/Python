class Dog:
	def __init__(self, name):
		self.name = name

	def display_name(self):
		print(f"Dog's name: {self.name}")

class Labrador(Dog):	# single inherittance
	def sound(self):
		print("Labradog woofs")


#Multilevel Inheritance
class GuideDog(Labrador):
	def guide(self):
		print(f"{self.name} guides the way!")


# Multiple Inheritance
class Friendly:
	def greet(self):
		print(f"I am a friendly Dog")

class GoldenRetriever(Dog, Friendly):
	def sound(self):
		print("Golden Retriever Barks")


# Example Usage

lab = Labrador("Buddy")
lab.display_name()
lab.sound()

guide_dog = GuideDog("Max")
guide_dog.display_name()
guide_dog.guide()

retriever = GoldenRetriever("Charlie")
retriever.display_name()
retriever.greet()
retriever.sound()

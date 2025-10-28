print('\n') 

class Dog:
    """A simple attempt to model a dog."""

    # CONSTRUCTOR
    def __init__(self, name, age):
        """Initialize name and age attributes"""

        self.name = name
        self.age = age
        self.dog_years = age * 7 #this is my own thing so that i can see how i can modify what i want the function to do


    # METHODS 
    def sit(self):
        """Simulate a dog sitting in response to a command."""

        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Simulate rolling over in respinse to a command."""

        print(f"{self.name} rolled over.")

# # INSTANTIATE DOG OBJECT 
# my_dog = Dog('Willie', 6)

# print(f"My dog's name is {my_dog.name}")
# print(f"My dog is {my_dog.dog_years} years old in dog years but on my timeline he is {my_dog.age} years old")

# print('\n') 

# #CALLING THE METHODS NOW 

# my_dog.sit()
# my_dog.roll_over()

print('\n') 

# CREATING MUTIPLE INSTANCES 

my_dog = Dog('Willie', 6)
your_dog = Dog('Lucky', 3)

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.dog_years} years old in dog years but on my timeline he is {my_dog.age} years old")
my_dog.sit()

print('\n')

print(f"Your dog's name is {your_dog.name}.")
print(f"Your dog is {your_dog.dog_years} years old in dog years but on my timeline he is {your_dog.age} years old")
your_dog.sit()

print('\n') 


import random 
print("Welcome to Pet Adoption System")
class Pet_Adoption:
    def __init__(self,name,age,species):
        self.name=name
        self.age=age
        self.species=species
        self.adopted = False 
    def display_info(self):
        print(f"Name:{self.name}")
        print(f"Age:{self.age}")
        print(f"Species:{self.species}")
        print(f"Adopted: {'Yes' if self.adopted else 'No'}")

class Dog(Pet_Adoption):
    def __init__(self,name,age,species, breed,color):
        self.breed=breed
        self.color=color
        super().__init__(name, age, species)
    def display_info(self):
        super().display_info()
        print(f"Breed:{self.breed}")
        print(f"color:{self.color}")

class Cat(Pet_Adoption):
    def __init__(self,name,age,species, breed,color):
        self.breed=breed
        self.color=color
        super().__init__(name, age, species)
    def display_info(self):
        super().display_info()
        print(f"Breed:{self.breed}")
        print(f"color:{self.color}")


def generate_pet_id():
    return f"PETID{random.randint(1000,1999)}"

Pet_Store={}

def add_pets():
    species_input = input("Choose a Pet Dog/Cat:").lower()
    name = input("Enter name: ")
    age = input("Enter age: ")
    breed = input("Enter Breed: ")
    color = input("Enter Color: ")
    species = species_input.capitalize() 
    if species_input == "dog":
        pet = Dog(name, age, species, breed, color)
    elif species_input == "cat":
        pet = Cat(name, age, species, breed, color)
    else:
        print("Invalid Pet species")
        return

    pet_id = generate_pet_id()
    while pet_id in Pet_Store:
        pet_id = generate_pet_id()
    Pet_Store[pet_id] = pet
    print(f"{species} added with Id: {pet_id}")


def pet_view():
    if not Pet_Store:
        print("Pets are unavailable")
        return 
    else:
        for pet_id,pet in Pet_Store.items():
            print(f"Pet Id :{pet_id}")
            pet.display_info()

def adopt_Pet():
    while True:
        pet_id = input("Enter the Pet Id: ")
        if pet_id in Pet_Store:
            print("You have adopted the following pet:\n")
            Pet_Store[pet_id].display_info()
            Pet_Store[pet_id].adopted = True
        else:
            print("Invalid Pet Id")

        more = input("Do you want to adopt one more pet? (y/n): ").lower()
        if more != 'y':
            break


def Pet():
    print("1. Add Pet")
    while True:
        add_pets()
        more = input("Do you want to add more pets? (y/n): ").lower()
        if more != 'y':
            break

    print("\n2. Adopt Pet")
    adopt_Pet()

    while True:
        choice = input("Choose an option: (1 - View Pets | 2 - Exit): ")
        if choice == "1":
            pet_view()
        elif choice == "2":
            print("Thank you for using the Pet Adoption System!")
            break
        else:
            print("Invalid choice. Please try again.")

Pet()

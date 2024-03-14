class Pet:
    # variable pet type
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    # class variable that stores all pet instances
    all = []

    def __init__(self, name, pet_type, owner=None):
        self.name = name
        # hecks whether the pet_type provided during initialization (__init__) is not present in the list of allowed pet types (self.PET_TYPES).
        if pet_type not in self.PET_TYPES:
            # If the pet_type is not in the list of allowed pet types, this line raises an exception
            raise Exception("Invalid pet type,the allowed pet types are: {}".format(self.PET_TYPES))
        self.pet_type = pet_type
        self.owner = owner
        if owner:
            owner.add_pet(self)
        self.all.append(self)

    def set_owner(self, owner):
        if not isinstance(owner, Owner):
            raise Exception("The provided object is not of  the type of Owner.")
        self.owner = owner
# defining a class owner with an argument name
class Owner:
    def __init__(self, name):
        self.name = name
        self._pets = []
# returns a full list of the owners pets
    def pets(self):
        return self._pets

    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception("The provided object is not of type Pet.")
        pet.set_owner(self)
        self._pets.append(pet)
# returns a sorted list of pets by their names
    def get_sorted_pets(self):
        # lambda is afunction that returns the name of the pet attribute
        sorted_pets = sorted(self._pets, key=lambda pet: pet.name)
        return sorted_pets



# Example usage:

# Create an owner
owner = Owner("John")

# Create some pets and assign them to the owner
pet1 = Pet("Buddy", "dog", owner)
pet2 = Pet("Fluffy", "cat", owner)
pet3 = Pet("Spike", "dog", owner)

# Get the list of pets for the owner
print("Owner's pets:", [pet.name for pet in owner.pets()])

# Sort the owner's pets by their names
sorted_pets = owner.get_sorted_pets()
print("Sorted pets:", [pet.name for pet in sorted_pets])

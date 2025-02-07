class Owner:
    def __init__(self, name):
        self.name = name
    
    def pets(self):
        """Returns a list of pets owned by this owner."""
        return [pet for pet in Pet.all if pet.owner == self]
    
    def add_pet(self, pet):
        """Assigns this owner to the pet, ensuring it's a valid Pet instance."""
        if not isinstance(pet, Pet):
            raise Exception("Only instances of Pet can be added.")
        pet.owner = self
    
    def get_sorted_pets(self):
        """Returns a sorted list of pets owned by this owner by name."""
        return sorted(self.pets(), key=lambda pet: pet.name)


class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []  # Stores all instances of Pet
    
    def __init__(self, name, pet_type, owner=None):
        if pet_type not in Pet.PET_TYPES:
            raise Exception(f"Invalid pet type. Must be one of: {Pet.PET_TYPES}")
        
        self.name = name
        self.pet_type = pet_type
        self.owner = owner if owner is None or isinstance(owner, Owner) else None
        
        if owner is not None and not isinstance(owner, Owner):
            raise Exception("Owner must be an instance of Owner class.")
        
        Pet.all.append(self)  # Add the instance to the all list
    
    def __repr__(self):
        return f"{self.name} ({self.pet_type})"

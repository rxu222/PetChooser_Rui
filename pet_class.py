# Set up properties and methods
class Pets:
    def __init__(self, pet_id, pet_name, pet_age, pet_type, owner_name):
        self.pet_id = pet_id
        self.pet_name = pet_name
        self.pet_age = pet_age
        self.pet_type = pet_type
        self.owner_name = owner_name

    def __str__(self):
        return f"{self.pet_name} is a {self.pet_type}. {self.pet_name} is {self.pet_age} years old. {self.pet_name}'s owner is {self.owner_name}"

class Pet:
    vet_name = "Logan's Veterinary Office"

    def __init__(self, owner_first_name, owner_last_name, pet_id, pet_name, pet_type):
        self.__owner_first_name = owner_first_name
        self.__owner_last_name = owner_last_name
        self.__pet_id = pet_id
        self.__pet_name = pet_name
        self.__pet_type = pet_type

    def get_owner_first_name(self):
        return self.__owner_first_name
    
    def get_owner_last_name(self):
        return self.__owner_last_name
    
    def get_pet_id(self):
        return self.__pet_id
    
    def get_pet_name(self):
        return self.__pet_name
    
    def get_pet_type(self):
        return self.__pet_type
    
    def set_owner_first_name(self, value):
        self.__owner_first_name = value
    
    def set_owner_last_name(self, value):
        self.__owner_last_name = value

    def set_pet_id(self, value):
        self.__pet_id = value

    def set_pet_name(self, value):
        self.__pet_name = value
    
    def set_pet_type(self, value):
        self.__pet_type = value


    def display_pet_info(self):
        print("Pet Details: ", vars(self))

    def print_info(self):
        print(self.__owner_first_name + "" + self.__owner_last_name)
        print(self.__pet_id)
        print(self.__pet_name)
        print(self.__pet_type)


def main():

    def check_property(obj, prop):
        if hasattr (obj, prop):
            print (f"{prop} exists for the given object.")
        else:
            print(f"{prop} does not exist for the given object")


    pet1 = Pet("Jolene", "Peters", "0123", "Stinky", "Dog")
    pet2 = Pet("Roger", "Alvarez", "4388", "Tater", "Dog")
    pet3 = Pet("Alison", "Litchfield", "0054", "Biscuit", "Dog")

    
    pet1.display_pet_info()
    pet2.display_pet_info()
    pet3.display_pet_info()

    print()
    check_property(pet1, "owner_last_name")
    check_property(pet2, "pet_id")
    check_property(pet3, "pet_name")

main()  
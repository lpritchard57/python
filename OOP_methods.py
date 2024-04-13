class Pet:
    vet_name = "Logan's Vet Office"

    def __init__(self, kind, breed, name):
        
        self.__kind = kind
        self.__breed = breed
        self.__name = name

    def get_kind(self):
        return self.__kind
    
    def get_breed(self):
        return self.__breed
    
    def get_name(self):
        return self.__name
    
    def set_kind(self, value):
        self.__kind = value

    def set_breed(self, value):
        self.__breed = value

    def set_name(self, value):
        self.__name = value

    def print_pet_details(self):
        print("Pet Details:", vars(self))

    def print_info(self):
        print(f"{self.__kind}\n{self.__breed}\n{self.__name}")

def main():
    pet1 = Pet("Dog", "Golden Retriever", "Roger")
    print("\nName:")
    print(pet1.__class__.__name__)

    print("\nDictionary:")
    print(pet1.__dict__)

    print("\nBreed:")
    print(pet1.get_breed())


main()
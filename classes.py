class Person:
    def __init__(self, name, address, age, phone_number):
        self.name = name
        self.address = address
        self.age = age
        self.phone_number = phone_number

    def get_info(self):
        return f"{self.name}, Address: {self.address}, Age: {self.age}, Phone Number: {self.phone_number}"
    
    def set_name(self, name):
        self.name = name

    def set_address(self, address):
        self.address = address

    def set_age(self, age):
        self.age = age

    def set_phone_number(self, phone_number):
        self.phone_number = phone_number
        
person1 = Person("Logan Pritchard", "2367 Oak Street", "23", "2245678775")
person2 = Person("Alan Peralta", "889 Haven Way", "44", "8156448722")
person3 = Person("Rachel Green", "1 Willow Court", "25", "6303320447")

print(person1.get_info())
print(person2.get_info())
print(person3.get_info())
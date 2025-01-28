class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def greet(self):
        print(f"Cześć, jestem {self.first_name} {self.last_name}!")

person = Person("Jan", "Kowalski")
person.greet()
#commit
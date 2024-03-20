from person import Person

class Stupid(Person):
    def greet(self,other_person):
        return f"Hello, {other_person.name}"
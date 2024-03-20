from person import Person

class Realist(Person):
    def greeting(self,other_person):
        if other_person.age >= 5:
            return f"Hello realist, {other_person.name}"
        else:
            pass
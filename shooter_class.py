import random


class Shooter:
    def __init__(self, name, age, passport, experience):
        self.shoot_probability = None
        self.name = name
        self.age = age
        self.__passport = passport
        self.experience = experience
        self.hit_target = None

    def shoot_probability(self):
        self.shoot_probability = 0.02 * self.experience * 100
        return self.shoot_probability

    def shoot(self):

        random_number = random.randint(1, 100)
        if random_number in range(1, int(self.shoot_probability) + 1):
            self.hit_target = True
        else:
            self.hit_target = False
        return self.hit_target

    def get_passport(self):
        return self.__passport

    def set_passport(self):
        return self.__passport

import random


class Shooter:
    def __init__(self, name, age, experience):
        self.__name = name
        self.__age = age
        self.__experience = experience

    def shoot_probability(self):
        self.shoot_probability = 0.02 * self.__experience * 100
        return int(self.shoot_probability)

    def shoot(self):
        hit_target = None
        random_number = random.randint(1, 100)
        if random_number in range(1, self.shoot_probability + 1):
            hit_target = True
        else:
            hit_target = False
        return hit_target

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_experience(self):
        return self.__experience

    def set_name(self):
        return self.__name

    def set_age(self):
        return self.__age

    def set_experience(self):
        return self.__experience

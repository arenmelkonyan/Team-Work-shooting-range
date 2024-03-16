class Shooter:
    def __init__(self, name, age, experience, shoot_rate):
        self.__name = name
        self.__age = age
        self.__experience = experience
        self.__shoot_rate = shoot_rate

    def shoot_probability(self):
        shoot_probability = self.__shoot_rate * self.__experience
        return shoot_probability

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





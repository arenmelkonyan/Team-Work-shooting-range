class Shooter:
    def __init__(self, name, years_old, experience, shoot_rate):
        self.name = name
        self.years_old = years_old
        self.experience = experience
        self.shooting_experience = shoot_rate

    def shoot_probability(self):
        shoot_probability = self.shooting_experience * self.experience
        return shoot_probability

    def get_name(self):
        return self.name

    def get_age(self):
        return self.years_old

    def get_experience(self):
        return self.experience

    def set_name(self):
        return self.name

    def set_age(self):
        return self.years_old

    def set_experience(self):
        return self.experience

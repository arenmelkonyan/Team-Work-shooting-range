from shooter_class import Shooter


class Beginner(Shooter):
    def __init__(self, name, age, passport, experience):
        super().__init__(name, age, passport, experience)
        self.shoot_probability = Shooter.shoot_probability(self)
        self.passport = Shooter.get_passport(self)

    def display_info(self):
        return (f"Shooter name: {self.name},\nShooter age: {self.age},\nShooter passport: {self.passport},"
                f"\nShooter experience: {self.experience},\nShooting result: {self.hit_target}")

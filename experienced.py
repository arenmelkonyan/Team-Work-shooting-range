from Shooter_class import Shooter


class ExperiencedShooter(Shooter):
    def __init__(self, name, years_old, shoot_rate):
        super().__init__(name, years_old, shoot_rate)

    def display_info(self):
        return (f"Hello shooter:\nName:\t{self.name}\nYears old in this world:\t{self.years_old}"
                f"\nShooting experience:\t{self.shoot_rate}")
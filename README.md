Project 1: Shooter Target Practice
Description
This program simulates a shooting competition where shooters of different skill levels attempt to hit a target. Shooters are divided into three groups: Novice, Experienced, and Expert. Each shooter has a name, age, and shooting experience.


Classes
Shooter: Base class for all shooters.


Attributes: name, age, experience
Methods: fire() - a polymorphic method that returns True if the shooter hits the target, False otherwise.
Novice: Subclass of Shooter for novice shooters.


Inherits from Shooter class.
Probability of hitting the target: 0.01 * experience.
Experienced: Subclass of Shooter for experienced shooters.


Inherits from Shooter class.
Probability of hitting the target: 0.05 * experience.
Expert: Subclass of Shooter for expert shooters.


Inherits from Shooter class.
Probability of hitting the target: 0.9 - 0.01 * age.

Main File

Create an array of shooters: Novice, Experienced, Expert, Experienced, Novice.
Simulate shooting competition until a shooter hits the target or all shooters have attempted.

Output

Log information about each shot (shooter's details and result) in "shooting_results_log.txt" file (one information per line).
Files

shooter_class.py - Contains the Shooter base class.

beginner_class.py - Contains the Novice subclass.

experienced.py - Contains the Experienced subclass.

expert.py - Contains the Expert subclass.

main.py - Contains the main program logic.

Running the Program
To run the program, execute the main.py file. Ensure all Python files are in the same directory.

OOP Concepts

Encapsulation: Attributes and methods are encapsulated within classes to ensure data integrity and protect implementation details.

Inheritance: Subclasses inherit attributes and methods from the base Shooter class, promoting code reusability.

Polymorphism: The fire() method is implemented differently in each subclass, demonstrating polymorphic behavior.

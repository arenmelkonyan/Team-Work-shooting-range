import random
from person import Person
from positive import Positive
from realist import Realist
from stupid import Stupid


people = [
    Positive("Aram",random.randint(20,40)),
    Realist("Sanasar",random.randint(20,40)),
    Stupid("Armen",random.randint(20,40)),
    Realist("Baghdasar",random.randint(20,40)),
    Positive("Irina",random.randint(20,40)),
]

with open("conversation_log.txt","a") as log_textfile:
    for i,person in enumerate(people):
        for j,other_person in enumerate(people):
            if i != j:
                greeting = person.greet(other_person)
                log_textfile.write(f"{person.name} greets {other_person.name}: {greeting}\n")
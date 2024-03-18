from beginner_class import Beginner
from expert import Expert
from Tnayinner.Project1.expierenced_class import Experienced

beginner_1 = Beginner('Suren', 32, 'AP1234567', 4)
experienced_1 = Experienced('Klara', 25, 'AL418151', 8)
expert = Expert('Jorik', 40, 'AN245847', 17)
experienced_2 = Experienced('Sona', 35, 'AG1561681', 7)
beginner_2 = Beginner('Karlen', 17, 'AN45861', 2)

player_lst = [beginner_1, expert]

for o in (beginner_1,experienced_1, expert, experienced_2, beginner_2):

    while not o.shoot():
        file = open('shooting_results_log.txt', 'a')
        file.write(o.display_info() + '\n' + '\n')
        file.close()
    else:
        file = open('shooting_results_log.txt', 'a')
        file.write(f'!!!!!!{o.name} is winner!!!!!\n')
        file.write(o.display_info() + '\n' + '\n')
        file.close()
        break


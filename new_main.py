from beginner_class import *
from expert import *

beginner = Beginner("kjks", 17, 182989, 4)
expert = Expert("jdshk", 34, 3498983, 10)




players_list = [beginner, expert]
for i in players_list:
    if i.shoot():
        print("\n",i.display_info())
        print(i.hit_target)
        break
    else:
        print("False")
        print(i.hit_target)
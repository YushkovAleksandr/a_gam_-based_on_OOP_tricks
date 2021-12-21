import random
"""

Create some game with OOP!    

"""
class Door:     
    def __init__(self, number):
        self.__id = number
class Wall:     
    def __init__(self):
        pass
class Room: 
    def __init__(self, num):
        self.walls = (Wall(), Wall(), Wall(), Wall())
        self.__number = num
    def get_number(self):
        return self.__number
class Character:
    def __init__(self, room):
        self.alive = True
        self.room = room
    def move(self, room, maze):        
        list_of_doors = []
        for door in maze:
            if room in door:
                list_of_doors.append(door)
        rand_room = [x for x in random.choice(list_of_doors) if x != room]
        new_room = rand_room[0]
        return new_room
    def fight(self, dice): 
        pass
class Hero(Character): 
    def __init__(self, room):
        self.alive = True
        self.room = room
    def fight(self, dice):
        fighting = {1: "Hero looks pretty tasty",
                    2: "Mighty Hero rises his sword",
                    3: "Hero looks at Monster",
                    4: "Hero sees Monster and immediately falls on the floor",
                    5: "Hero pulls out a rocket launcher",
                    6: "Hero stares severely at Monster"}
        print(fighting[dice])      
class Monster(Character): 
    def __init__(self, room):
        self.alive = True
        self.room = room 
    def fight(self, dice):         
        fighting = {1: "Monster has a great om-nom-nom", 
                    2: "Monster falls down on the floor",
                    3: "Monster looks at Hero\nThey both have better things to do than fighting.",
                    4: "Monster has poor eyesight, so he just goes on.",
                    5: "\"Wait! You'll blow us up!\" BOOM!!!",
                    6: "Monster runs away calling for his Mommy!"}
        print(fighting[dice])
class MazeMaster:    
    def build_rooms(self, number_of_rooms):        
        rooms = []
        for num in range(number_of_rooms):
            rooms.append(Room(num).get_number())    
        return rooms
    def make_doors(self, num_of_rooms):
        number_of_doors = num_of_rooms * random.randrange(2, 3)
        doors = []
        for num in range(number_of_doors):
            doors.append(Door(num))
        return doors
    def built_maze(self, num_of_rooms):
        rooms = self.build_rooms(num_of_rooms)
        doors = self.make_doors(len(rooms))
        maze = []
        for door in doors:
            door = [random.choice(rooms), random.choice(rooms)]            
            maze.append(door)        
        for door in maze:
            if door[0] == door[1]:
                door[1] = random.choice(rooms)       
        return maze
    def main(self):
        number_of_rooms = int(input("How many rooms should be in the game(1 or 2)?\n"))
        maze = self.built_maze(number_of_rooms)

        hero = Hero(random.randrange(0, number_of_rooms))
        monster = Monster(random.randrange(0, number_of_rooms))
        while hero.alive and monster.alive == True:
            if hero.room == monster.room:
                print("Hero and Monster have met! Now they have to fight!")
                input("Let's roll the dice to choose the battle outcome!\nPress Enter to roll the dice!(from 1 to 6")
                dice = random.randrange(1, 6)
                print(f"Result is {dice}")
                hero.fight(dice)
                monster.fight(dice)
                if dice == 1:
                    input("Hero is dead, Moster wins!\nPress Enter to quit")
                    hero.alive = False
                elif dice == 2:
                    input("Monster is dead, Hero wins!\nPress Enter to quit")
                    monster.alive = False
                elif dice == 5:
                    input("They both are dead. Someone should choose better weapon next time!\nPress Enter to quit")
                    hero.alive = False
                    monster.alive = False
                else:
                    hero.room = hero.move(hero.room, maze)
                    print(f"Hero goes to room {hero.room}")
                    monster.room = hero.move(monster.room, maze)
                    print(f"Monster goes to room {monster.room}")
            else:
                hero.room = hero.move(hero.room, maze)
                print(f"Hero goes to room {hero.room}")
                monster.room = hero.move(monster.room, maze)
                print(f"Monster goes to room {monster.room}")     
if __name__ == "__main__":
    gm = MazeMaster()
    game = gm.main()
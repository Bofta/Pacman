#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''
import sys; sys.path.append('../examples/')
import g2d
from random import choice


board = ["#############################",
         "#             #             #",
         "# ------------# ------------#",
         "# -### -#### -# -#### -### -#",
         "# +### -#### -# -#### -### +#",
         "# -    -     -  -     -    -#",
         "# --------------------------#",
         "# -### -# -####### -# -### -#",
         "# -    -# -   #    -# -    -#",
         "# ------# ----# ----# ------#",
         "###### -####  #  #### -######",
         "###### -#           # -######",
         "###### -#           # -######",
         "###### -#  #######  # -######",
         "       -   #######    -      ",
         "       -   #######    -      ",
         "###### -#  #######  # -######",
         "###### -#           # -######",
         "###### -#           # -######",
         "###### -#  #######  # -######",
         "#      -      #       -     #",
         "# ------------# ------------#",
         "# -### -#### -# -#### -### -#",
         "# -  # -     -  -     -#   -#",
         "# +--# -------  -------# --+#",
         "### -# -# -####### -# -# -###",
         "#   -  -# -   #    -# -  -  #",
         "# ------# ----# ----# ------#",
         "# -######### -# -######### -#",
         "# -          -  -          -#",
         "# --------------------------#",
         "#############################"]


from random import choice, randrange
from time import time
from actor import Actor, Arena



class Red_Ghost(Actor):
    def __init__(self, arena, pos):
        self._x, self._y = pos
        self._w, self._h = 16, 16
        self._dx, self._dy = 0, 0
        self._arena = arena
        arena.add(self)
        self._visible = True
        
    def in_wall(self ,x: int, y: int) -> bool:
        c, r, w, h = x//8, y//8, 3 if x%8 else 2, 3 if y%8 else 2
        return "#" in "".join(line[c:c+w] for line in board[r:r+h])
#         for line in board[r:r+h]:
#             if "#" in line[c:c+w]: return True
#         return False

    def move(self):
        arena_w, arena_h = self._arena.size() #First Milestone
        # If Actor(Ghost) is in board -> move in a certain direction without colliding in a wall (no front - back)
        directions = [(0, -4), (4, 0), (0, 4), (-4, 0)]
        opposite = (-self._dx, -self._dy)
        if opposite in directions:
            directions.remove(opposite) # No turning back

        self._dx, self._dy = choice(directions)
            #assert((dx, dy) != opposite)  #  check, always true
        
        if self.in_wall(self._x + self._dx , self._y + self._dy):
            self._dx, self._dy = 0 , 0
        self._x += self._dx
        self._y += self._dy
        if opposite in directions:
            directions.remove(opposite) # No turning back

        self._dx, self._dy = choice(directions)
            
        

        if randrange(100) == 0:
            self._visible = not self._visible        

    def collide(self, other):
        pass
    
    def position(self):
        return self._x, self._y

    def size(self):
        return self._w, self._h

    def symbol(self):
        if self._visible:
            return 128, 80
        return 0, 64
    
class Purple_Ghost(Actor):
    def __init__(self, arena, pos):
        self._x, self._y = pos
        self._w, self._h = 16, 16
        self._dx, self._dy = 0, 0
        self._arena = arena
        arena.add(self)
        self._visible = True
        
    def in_wall(self ,x: int, y: int) -> bool:
        c, r, w, h = x//8, y//8, 3 if x%8 else 2, 3 if y%8 else 2
        return "#" in "".join(line[c:c+w] for line in board[r:r+h])
#         for line in board[r:r+h]:
#             if "#" in line[c:c+w]: return True
#         return False

    def move(self):
        arena_w, arena_h = self._arena.size() #First Milestone
        # If Actor(Ghost) is in board -> move in a certain direction without colliding in a wall (no front - back)
        directions = [(0, -4), (4, 0), (0, 4), (-4, 0)]
        opposite = (-self._dx, -self._dy)
        if opposite in directions:
            directions.remove(opposite) # No turning back

        self._dx, self._dy = choice(directions)
            #assert((dx, dy) != opposite)  #  check, always true
        
        if self.in_wall(self._x + self._dx , self._y + self._dy):
            self._dx, self._dy = 0 , 0
        self._x += self._dx
        self._y += self._dy
        if opposite in directions:
            directions.remove(opposite) # No turning back

        self._dx, self._dy = choice(directions)
        print(self._x, self._y, self._dx, self._dy, sep="\t")
      
                      

        if randrange(100) == 0:
            self._visible = not self._visible
        

    def collide(self, other):
        pass
    

    def position(self):
        return self._x, self._y

    def size(self):
        return self._w, self._h

    def symbol(self):
        if self._visible:
            return 128, 80
        return 0, 80
    
class Orange_Ghost(Actor):
    def __init__(self, arena, pos):
        self._x, self._y = pos
        self._w, self._h = 16, 16
        self._dx, self._dy = 0, 0
        self._arena = arena
        arena.add(self)
        self._visible = True
        
    def in_wall(self ,x: int, y: int) -> bool:
        c, r, w, h = x//8, y//8, 3 if x%8 else 2, 3 if y%8 else 2
        return "#" in "".join(line[c:c+w] for line in board[r:r+h])
#         for line in board[r:r+h]:
#             if "#" in line[c:c+w]: return True
#         return False

    def move(self):
        arena_w, arena_h = self._arena.size() #First Milestone
        # If Actor(Ghost) is in board -> move in a certain direction without colliding in a wall (no front - back)
        directions = [(0, -4), (4, 0), (0, 4), (-4, 0)]
        opposite = (-self._dx, -self._dy)
        if opposite in directions:
            directions.remove(opposite) # No turning back

        self._dx, self._dy = choice(directions)
            #assert((dx, dy) != opposite)  #  check, always true
        
        if self.in_wall(self._x + self._dx , self._y + self._dy):
            self._dx, self._dy = 0 , 0
        self._x += self._dx
        self._y += self._dy
        if opposite in directions:
            directions.remove(opposite) # No turning back

        self._dx, self._dy = choice(directions)
                
        

        if randrange(100) == 0:
            self._visible = not self._visible
        

    def collide(self, other):
        pass
    

    def position(self):
        return self._x, self._y

    def size(self):
        return self._w, self._h

    def symbol(self):
        if self._visible:
            return 128, 80
        return 0, 112


class PacMan(Actor):
    def __init__(self, arena, pos):
        self._x, self._y = pos
        self._w, self._h = 16, 16
        self._speed = 2
        self._dx, self._dy = 0, 0
        self._lives = 3
        self._score = 0
        self._last_collision = 0
        self._arena = arena
        arena.add(self)
        
    def move(self): #Second Milestone
        # If Actor(PacMan) is in board -> move in a certain direction without colliding in a wall 
        if self.in_wall(self._x + self._dx, self._y + self._dy):
            self._dx = 0
            self._dy = 0
        self._y += self._dy
        self._x += self._dx
        arena_w, arena_h = self._arena.size()
        if self._y < 0:
                self._y = 0
        elif self._y > arena_h - self._h:
            self._y = arena_h - self._h
            self._x += self._dx
            if self._x < 0:
                self._x = 0
            elif self._x > arena_w - self._w:
                self._x = arena_w - self._w
    
    def in_wall(self ,x: int, y: int) -> bool:
        c, r, w, h = x//8, y//8, 3 if x%8 else 2, 3 if y%8 else 2
        return "#" in "".join(line[c:c+w] for line in board[r:r+h])
#         for line in board[r:r+h]:
#             if "#" in line[c:c+w]: return True
#         return False
                

    def control(self, keys):
        u, d, l, r = "ArrowUp", "ArrowDown", "ArrowLeft", "ArrowRight"
        #u, d, l, r = "w", "s", "a", "d"

        if u in keys:
            self._dy = -self._speed
        elif d in keys:
            self._dy = self._speed
            return 16 , 48
        else: self._dy = 0

        if l in keys: self._dx = -self._speed
        elif r in keys: self._dx = self._speed
        else: self._dx = 0
            
            
    def message(self) -> str :
        print("Callable debug function")
            

    def lives(self) -> int:
        return self._lives
    
    def score(self) -> int:
        return self._score

    def collide(self, other):
        if self._arena.count() - self._last_collision < 30:
            return
        self._last_collision = self._arena.count()
        if isinstance(other, Red_Ghost):
            self._lives -= 1
        elif isinstance(other, Purple_Ghost):
            self._lives -= 1
        elif isinstance(other, Orange_Ghost):
            self._lives -= 1
        elif isinstance(other, Biscotti):
            self._score += 100
        elif isinstance(other, Super_Biscotti):
            self._score += 300
            

    def position(self):
        return self._x, self._y

    def size(self):
        return self._w, self._h

    def symbol(self):
        return 16, 0
                
        
            
class Biscotti(Actor):
    def __init__(self, arena, pos):
        self._x, self._y = pos
        self._w, self._h = 16, 14 
        self._score = 100
        self._arena = arena
        arena.add(self)
        
    def symbol(self):
        return 160, 50
    
    def position(self):
        return self._x, self._y

    def size(self):
        return self._w, self._h
    
    def move(self):
        pass
    
    def collide(self, other):
        if isinstance(other, Red_Ghost):
            pass
        elif isinstance(other, Purple_Ghost):
            pass
        elif isinstance(other, Orange_Ghost):
            pass
        elif isinstance(other, PacMan):
            self._arena.remove(self)
            
            
class Super_Biscotti(Actor):
    def __init__(self, arena, pos):
        self._x, self._y = pos
        self._w, self._h = 16, 14 
        self._score = 100
        self._arena = arena
        arena.add(self)
        
    def symbol(self):
        return 176, 48
    
    def position(self):
        return self._x, self._y

    def size(self):
        return self._w, self._h
    
    def move(self):
        pass
    
    def collide(self, other):
        if isinstance(other, Red_Ghost):
            pass
        elif isinstance(other, Purple_Ghost):
            pass
        elif isinstance(other, Orange_Ghost):
            pass
        elif isinstance(other, PacMan):
            self._arena.remove(self)
            
    
def print_position_biscotti(arena):  #function to locate normal biscuits positions in "board" list -> dosent work 
    pos_biscotti_list = []
    for x in board:
        if "-" in x:
            pos_biscotti_list.append(x)
    print(pos_biscotti_list)
            

def print_arena(arena):  
    for a in arena.actors():
        print(type(a).__name__, '@', a.position())
        
                                
def main():
    arena = Arena((232, 256))
    Red_Ghost(arena,(8, 225))      #First ghost
    Purple_Ghost(arena,(205, 8))     #Second ghost
    Orange_Ghost(arena, (205, 225))   #Third ghost
    PacMan(arena,(8, 8))
    Biscotti(arena,(20,20))
     

    for i in range(1):
        print_arena(arena)
        print_position_biscotti(arena)
        arena.move_all()

main()  # call main to start the program



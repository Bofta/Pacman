#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

from time import time
from pacmanbase import Actor, Arena, Red_Ghost, Purple_Ghost , Orange_Ghost , PacMan , Biscotti , Super_Biscotti


class PacManGame:
    def __init__(self):
#         self._arena = Arena((232, 256))
        self._arena = Arena((232, 300))

        Red_Ghost(self._arena, (16, 232))      #First ghost
        Purple_Ghost(self._arena, (8, 16))     #Second ghost
        Orange_Ghost(self._arena, (208, 224))  #Third ghost
        Super_Biscotti(self._arena, (208, 32))
        Super_Biscotti(self._arena, (208, 208))
        Super_Biscotti(self._arena, (8, 32))
        Super_Biscotti(self._arena, (8, 208))
        
        Biscotti(self._arena,(8,8))
        Biscotti(self._arena,(30,8))
        Biscotti(self._arena,(50,8))
        Biscotti(self._arena,(70,8))
        Biscotti(self._arena,(85,8))
        Biscotti(self._arena,(122,8))
#2         
        Biscotti(self._arena,(140,8))
        Biscotti(self._arena,(160,8))
        Biscotti(self._arena,(175,8))
        Biscotti(self._arena,(190,8))
        
        # Biscotti first line verticali
        Biscotti(self._arena,(50,8))
        Biscotti(self._arena,(50,64))
        Biscotti(self._arena,(50,94))
        Biscotti(self._arena,(50,128))
        Biscotti(self._arena,(50,148))
        
        # Biscotti second line verticali
         
        Biscotti(self._arena,(100,8))
        Biscotti(self._arena,(100,64))
        Biscotti(self._arena,(100,94))
        Biscotti(self._arena,(150,128))
        Biscotti(self._arena,(150,148))
        Biscotti(self._arena,(150,64))
        Biscotti(self._arena,(150,94))

       
        
        # second line of biscotti
        
        Biscotti(self._arena,(8,208))
        Biscotti(self._arena,(24,208))
        Biscotti(self._arena,(40,208))
        
        
        Biscotti(self._arena,(80,208))
        Biscotti(self._arena,(100,208))
        Biscotti(self._arena,(100,208))
        
        Biscotti(self._arena,(120,208))
        Biscotti(self._arena,(142,208))
        Biscotti(self._arena,(170,208))
        Biscotti(self._arena,(190,208))
        Biscotti(self._arena,(210,208))
        



        self._my_biscotti = []
        x, y = 4, 4
        for i in range(28):
            x += x
            y += y
            self._my_biscotti.append(Biscotti(self._arena,(x,y)))
        
        # Biscotti inizializati staticamente perchè all'inzio non potevo ricavare le posizioni dal board

        
        
        self._hero = PacMan(self._arena, (208, 8))        
        self._playtime = 120  # seconds
        self._numbers = 5
        
           

    def arena(self) -> Arena:
        return self._arena

    def hero(self) -> PacMan:
        return self._hero

    def game_over(self) -> bool:
        return self._hero.lives() <= 0

    def game_won(self) -> bool:
        return self.remaining_time() <= 0 or self._hero._score >= 2000
#         len(self._my_biscotti)==0    #PacMan vince quando mangia tutti i biscotti(3rd Milestone)
      
        #Per esmpio 13 biscotti objects = 13 * 100 = 1300 score                                                          
  

    def remaining_time(self) -> int:
        return (self._playtime - self._arena.count() // 30)
    
    
    
    
    
   

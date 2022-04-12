#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

import g2d
from pacmangioco import PacManGame


class PacManGui:
    def __init__(self):
        self._game = PacManGame()
        g2d.init_canvas(self._game.arena().size())
        self._sprites = g2d.load_image("pacmansprite.png")
        self._background = g2d.load_image("pac-man-bg.png")
        g2d.main_loop(self.tick)

    def tick(self):
        self._game.hero().control(g2d.current_keys())
        arena = self._game.arena()
        arena.move_all() # Game logic
        g2d.clear_canvas()
        
        g2d.draw_image("pac-man-bg.png",(0, 0)) #Background image(PacMan Maze)
        
        for a in arena.actors():
            if a.symbol() != None:
                g2d.draw_image_clip(self._sprites, a.symbol(), a.size(), a.position())
            else:
                g2d.fill_rect(a.position(), a.size())
                
        lives = "Lives: " + str(self._game.hero().lives()) # Lives layout 
        toplay = "Time: " + str(self._game.remaining_time()) # playing time layout
        score = "Score: " + str(self._game.hero().score())
        YOLO = "Remaning       : " + str(self._game.hero().lives())
        g2d.set_color((250,205,82))                   
        g2d.draw_text(score + " " , (142, 258), 24)
        for i in range(self._game.hero().lives()):
            g2d.draw_text(YOLO + " " , (3, 258), 24)
            g2d.draw_image("16px_heart.png",(90 ,258))
            
            
        if self._game.game_over():
            g2d.alert("Game over")
            g2d.close_canvas()
        elif self._game.game_won():
            g2d.alert("Game won")
            g2d.close_canvas()

gui = PacManGui()

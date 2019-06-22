'''
Borrowed from Asteroid.py which was created by Lukas Peraza
    url: https://github.com/LBPeraza/Pygame-Asteroids

Subzero sprite borrowed from: https://www.spriters-resource.com/playstation/mkmsz/sheet/37161/
'''

import pygame
import math
from CollegiateObjectFile import CollegiateObject

class Projectile(CollegiateObject):
    speed = 15
    time = 50 # last 1 second

    def __init__(self, x, y, image, r, isRight):
    
        self.timeOnScreen = 0
        
        margin = 5
        
        self.isRight = isRight
        
        if self.isRight: self.velocity = Projectile.speed
        else: self.velocity = -Projectile.speed
        
        super(Projectile, self).__init__(x, y, image, r)

    def update(self, screenWidth, screenHeight):
        self.x += self.velocity
        super(Projectile, self).update(screenWidth, screenHeight)
        self.timeOnScreen += 1
        if self.timeOnScreen > Projectile.time or self.x <= 0 or self.x >= screenWidth:
            self.kill()

'''
Borrowed from GameObject.py which was created by Lukas Peraza
    url: https://github.com/LBPeraza/Pygame-Asteroids
'''
import pygame


class CollegiateObject(pygame.sprite.Sprite):
    
    def __init__(self, x, y, image, radius):
        
        super(CollegiateObject, self).__init__()
        
        # x, y define the center of the object
        self.x, self.y, self.image, self.radius = x, y, image, radius
        
        self.baseImage = image.copy()  # non-rotated version of image
        self.updateRect()
        
        print("Loaded Object")

    def updateRect(self):
        
        # update the object's rect attribute with the new x,y coordinates
        w, h = self.image.get_size()
        self.width, self.height = w, h
        self.rect = pygame.Rect(self.x - w / 2, self.y - h / 2, w, h)

    def update(self, screenWidth, screenHeight):
        
        self.image = self.baseImage
        self.updateRect()
import pygame
# from CollegiateCombatFile import CollegiateCombat

class DrawText(object):
    """ text code idea borrowed from https://stackoverflow.com/questions/20842801/how-to-display-text-in-pygame and https://www.youtube.com/watch?v=l-Sup0DLquM"""
    
    def __init__(self):
        pygame.init()
        
    def createFont(fontType = None, size = 25):
        # Create a font: specify the font and size; None gives default font or specify a TTF font file from C:/Windows/Fonts
        try:
            myFont = pygame.font.Font("C:/Windows/Fonts/%s.TTF" %fontType, size)
            return myFont
        except:
            print("Default font created")
            myFont = pygame.font.Font(None, size)
            return myFont
    
    def createText(text, color = (0, 0, 0), fontType = None, size = 25):
        # Create text using a already made font, or the default font
        try:
            if fontType == None:
                myFont = pygame.font.Font(None, size)
            else: 
                myFont = fontType

            myText = myFont.render(text, True, color)
            return myText
        except:
            print("Error in text rendering")
    
    def drawText(screen, text, cX, cY):
        try:
            textRect = text.get_rect()
            textRect.centerx = cX
            textRect.centery = cY
            screen.blit(text, textRect)
        except:
            print("Could not draw text")
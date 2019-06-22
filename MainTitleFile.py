'''
MainTitleFile
- implements the title screen
- initializes program
'''
import pygame
from CollegiateCombatFile import CollegiateCombat
from MenuFile import Menu
from DrawTextFile import DrawText

# Run This file to run the game

# right in variable means facing right, left means facing left
class MainTitle(CollegiateCombat):
    def init(self):
        
        CollegiateCombat.mode = "MainTitle"
        
        # Start Music
        CollegiateCombat.playMusic()
        
        # Import and resize background image
        self.background = pygame.image.load("images/backgrounds/fireicefists.png")

        wBackground, hBackground = self.width, self.height
        self.background = pygame.transform.scale( self.background, ( wBackground, hBackground) )
        
        # Import and resize title image        
        self.titleImage = CollegiateCombat.titleImage
        
        wTitle, hTitle = self.titleImage.get_size()
        factorTitle = 1
        if wTitle > (self.width // 2):
            factorTitle = (self.width // 2) / wTitle
        elif hTitle > (self.height // 2):
            factorTitle = (self.height // 2) / hTitle
        self.titleImage = pygame.transform.scale( self.titleImage, ( int(wTitle * factorTitle), int(hTitle * factorTitle) ) )
        
        self.timePassed = 0
        
        # Render text for name
        self.NameFont = DrawText.createFont("Alger", 30)
        self.NameText = DrawText.createText(text = "By: Lucky Wavai", color = CollegiateCombat.blue, fontType = self.NameFont)
        self.NameTextCX, self.NameTextCY = self.width // 7, self.height - 50
    
    def timerFired(self, dt):
        
        # Transition to game after the time alloted
        self.timePassed += 1
        transitionTime = 100
        
        if self.timePassed >= transitionTime:
            Menu().run()
            # CharacterSelect(1200, 600).run()

    def redrawAll(self, screen):
        
        # Add background
        screen.blit( self.background, (0, 0) )
        
        # Add title to title page
        titleLocationMod = - (screen.get_rect().centery // 5)
        titleRect = self.titleImage.get_rect()
        titleRect.centerx = screen.get_rect().centerx
        titleRect.centery = screen.get_rect().centery
        screen.blit(self.titleImage, titleRect)
        
        # Draw My Credits
        DrawText.drawText(screen, self.NameText, self.NameTextCX, self.NameTextCY)

MainTitle().run()

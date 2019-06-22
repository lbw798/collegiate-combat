'''
Borrowed from Game.py which was created by Lukas Peraza
    url: https://github.com/LBPeraza/Pygame-Asteroids

Actually implements the game

'''
import pygame
import string
from CollegiateCombatFile import CollegiateCombat
import os
from RunGameFile import RunGame
from DrawTextFile import DrawText

# right in variable means things on right side of screen, left means left side of screen
class BackgroundSelect(CollegiateCombat):
    def init(self):
        
        CollegiateCombat.mode == "BackgroundSelect"
        
        # Create background and board sizes
        margin = 10
        self.iconImageWidth = 200
        self.iconImageHeight = 200
        self.iconImageY = self.height // 8 - 15
        self.iconImageLeftX = margin + (self.width // 5)
        self.iconImageRightX = self.width - margin - self.iconImageWidth - (self.width // 5)
        
        self.backImageWidth = 300
        self.backImageHeight = 200
        self.backImageY = self.height // 8 - 15
        self.backImageX1 = margin + (self.width // 2) - (self.backImageWidth // 2)
        self.backImageX2 = self.width - margin - self.backImageWidth - (self.width // 5)
        
        self.rectWidth = 100
        self.rectHeight = 100
        self.rectY = self.height // 4
        self.leftRectX = margin + (self.width // 5)
        self.rightRectX = self.width - margin - self.rectWidth - (self.width // 5)
        
        self.imageY = (self.rectY )
        self.imageLeftX = (self.leftRectX )
        self.imageRightX = (self.rightRectX)
        
        # Upload each icon image and resize accordingly
        
        self.backgrounds = ["0-outside uc", "1-outside hammershlag", "2-fence", "3-wiegand", "4-tennis courts", "5-maggy mo", "6-gates bridge", "7-hunt", "8-the maze baker-porter", "9-mcconomy", "10-practice field", "11-stadium", "12-pittsburgh winter", "13-pittsburgh spring"]
        
        self.images = []
        self.selectedImages = []
        
        for imageName in self.backgrounds:
            image = pygame.image.load("images/backgrounds/game/%s.png" %imageName)
            selectedImage = image
            
            image = pygame.transform.scale( image, ( self.rectWidth, self.rectHeight ) )
            selectedImage = pygame.transform.scale( image, ( self.backImageWidth, self.backImageHeight ) )
            
            self.images.append(image)
            self.selectedImages.append(selectedImage)
        
        print("Num backgrounds: %d, NumImages: %d" %(len(self.backgrounds), len(self.images)))
        
        # Create a dictionary of backgrounds
        
        self.backBoard =    [   [{}, {}, {}, {}, {}, {}, {}],
                                [{}, {}, {}, {}, {}, {}, {}]
                            ]
        rowLst = []
        j = 0
        for row in range(len(self.backBoard)):
            for col in range(len(self.backBoard[0])):
                dict = {}
                dict = {self.backgrounds[j]: [ self.images[j], self.selectedImages[j] ]}
                self.backBoard[row][col] = dict
                j += 1
        
        self.imageRow = 0
        self.imageCol = 0
                
        for row in range(len(self.backBoard)):
            print(self.backBoard[row])
        
        for back in self.backBoard[self.imageRow][self.imageCol]:
            self.currentBackground = back
            self.currentImage = self.backBoard[self.imageRow][self.imageCol][back][1]
        
        self.SelectBackFont = DrawText.createFont("Alger", 50)
        self.SelectBackText = DrawText.createText(text = "Select Background", color = CollegiateCombat.red, fontType = self.SelectBackFont)
        self.SelectBackTextCX, self.SelectBackTextCY = ( ( (2 * self.backImageX1) + self.backImageWidth ) // 2), 20
        
        self.InfoFont = DrawText.createFont("Alger", 25)
        self.InfoText = DrawText.createText(text = "Use Arrow Keys", color = CollegiateCombat.white, fontType = self.InfoFont)
        self.InfoTextCX, self.InfoTextCY = (self.width // 6), (self.height // 3)
        
        self.BackgroundFont = DrawText.createFont("Alger", 20)
        self.BackgroundText = DrawText.createText(text = "%s" %self.currentBackground, color = CollegiateCombat.white, fontType = self.BackgroundFont)
        self.BackgroundTextCX, self.BackgroundTextCY = ( ( (2 * self.backImageX1) + self.backImageWidth) // 2), (self.backImageY + self.backImageHeight + 25)
        
        self.PressEnterFont = DrawText.createFont("Alger", 40)
        self.PressEnterText = DrawText.createText(text = "Press Enter To Continue", color = CollegiateCombat.red, fontType = self.PressEnterFont)
        self.PressEnterTextCX, self.PressEnterTextCY = ( ( (2 * self.backImageX1) + self.backImageWidth ) // 2), (self.BackgroundTextCY + 30)

    def keyPressed(self, code, mod, dt):
        
        if code == pygame.K_UP:
            if self.imageRow > 0:
                self.imageRow -= 1
            else: self.imageRow = (len(self.backBoard) - 1)
        if code == pygame.K_DOWN:
            if self.imageRow < (len(self.backBoard) - 1):
                self.imageRow += 1
            else: self.imageRow = 0
        if code == pygame.K_LEFT:
            if self.imageCol > 0:
                self.imageCol -= 1
            else: self.imageCol = (len(self.backBoard[0]) - 1)
        if code == pygame.K_RIGHT:
            if self.imageCol < (len(self.backBoard[0]) - 1):
                self.imageCol += 1
            else: self.imageCol = 0
        
        for back in self.backBoard[self.imageRow][self.imageCol]:
            self.currentBackground = back
            self.currentImage = self.backBoard[self.imageRow][self.imageCol][back][1]
        
        if code == pygame.K_RETURN:
            print("Starting Game! at %s" %self.currentBackground)
            
            # Set the chosen backgrounds
            CollegiateCombat.gameBackground = self.currentBackground
            
            # Run the game
            RunGame(1200, 600).run()
    
    def timerFired(self, dt):
        pass

    def redrawAll(self, screen):
        
        # Fill Background first
        screen.fill(CollegiateCombat.purple)
        
        # Create boarder attributes i.e. dimensions and color
        selectColor = CollegiateCombat.blue
        
        rectTobackImageSpace = 5
        backRectX1 = self.backImageX1 - rectTobackImageSpace
        backRectY = self.backImageY - rectTobackImageSpace
        backRectWidth = self.backImageWidth + (2*rectTobackImageSpace)
        backRectHeight = self.backImageHeight + (2*rectTobackImageSpace)
        
        # Create Background Boarder
        pygame.draw.rect( screen, selectColor, (backRectX1, backRectY, backRectWidth, backRectHeight) )
        screen.blit( self.currentImage, (self.backImageX1, self.backImageY) )
        
        # Create board of backgrounds with selection boarders
        
        # Create selection boarders
        rectToImageSpace = 5
        boardRectWidth = self.rectWidth + (2*rectToImageSpace)
        boardRectWidth = self.rectHeight + (2*rectToImageSpace)
        
        selectX = self.width // 2 - self.rectWidth - 250 - rectToImageSpace + self.imageCol * ( self.rectWidth + (2*rectToImageSpace) )
        selectY = self.boardY = self.PressEnterTextCY + 30 - rectToImageSpace + self.imageRow * ( self.rectHeight + (2*rectToImageSpace) )
        pygame.draw.rect( screen, selectColor, (selectX, selectY, boardRectWidth, boardRectWidth) )
        
        # Draw images of the board
        for row in range(len(self.backBoard)):
            for col in range(len(self.backBoard[0])):
                for key in self.backBoard[row][col]:
                    self.boardX = self.width // 2 - self.rectWidth - 250 + col * ( self.rectWidth + (2*rectToImageSpace) )
                    self.boardY = self.PressEnterTextCY + 30 + row * ( self.rectHeight + (2*rectToImageSpace) )
                    screen.blit( self.backBoard[row][col][key][0], (self.boardX, self.boardY) )
        
        # Draw Text
        flag = True
        i = 0
        while flag:
            text = self.currentBackground[i:]
            if text[0] in string.ascii_letters:
                flag = False
            i += 1
        self.BackgroundText = DrawText.createText(text = "%s" %text, color = CollegiateCombat.white, fontType = self.BackgroundFont)
        
        # Draw Text
        DrawText.drawText(screen, self.SelectBackText, self.SelectBackTextCX, self.SelectBackTextCY)
        DrawText.drawText(screen, self.PressEnterText, self.PressEnterTextCX, self.PressEnterTextCY)
        DrawText.drawText(screen, self.InfoText, self.InfoTextCX, self.InfoTextCY)
        DrawText.drawText(screen, self.BackgroundText, self.BackgroundTextCX, self.BackgroundTextCY)

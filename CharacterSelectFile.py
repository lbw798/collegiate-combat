'''
CharacterSelectFile
- allows user to select characters
- once selected moves onto map selection
'''
import pygame
from CollegiateCombatFile import CollegiateCombat
import os
from BackgroundSelectFile import BackgroundSelect
from DrawTextFile import DrawText

# right in variable means things on right side of screen, left means left side of screen
class CharacterSelect(CollegiateCombat):
    def init(self):
        
        CollegiateCombat.mode == "CharacterSelect"
        
        # Create icon and board sizes
        wBackground, hBackground = self.width, self.height

        margin = 10
        self.iconImageWidth = 200
        self.iconImageHeight = 200
        self.iconImageY = self.height // 8 - 15
        self.iconImageLeftX = margin + (self.width // 5)
        self.iconImageRightX = self.width - margin - self.iconImageWidth - (self.width // 5)
        
        self.rectWidth = 100
        self.rectHeight = 100
        self.rectY = self.height // 4
        self.leftRectX = margin + (self.width // 5)
        self.rightRectX = self.width - margin - self.rectWidth - (self.width // 5)
        
        self.imageY = (self.rectY )
        self.imageLeftX = (self.leftRectX )
        self.imageRightX = (self.rightRectX)
        
        # Upload each icon image and resize accordingly
        
        self.images = []
        
        path = "images/icons"
        
        for imageName in os.listdir(path):
            
            image = pygame.image.load(path + os.sep + imageName)
            
            image = pygame.transform.scale( image, ( self.rectWidth, self.rectHeight ) )
            
            self.images.append(image)
        
        # Create a dictionary of characters
        
        self.characters = ["subzero", "scorpion", "raizen", "goku", "naruto", "sasuke"]
        #print("Num Characters: %d, NumImages: %d" %(len(self.characters), len(self.images)))
        
        self.charBoard =    [   [{}, {}, {}],
                                [{}, {}, {}]
                            ]
        rowLst = []
        j = 0
        for row in range(len(self.charBoard)):
            for col in range(len(self.charBoard[0])):
                dict = {}
                dict = {self.characters[j]: self.images[j]}
                self.charBoard[row][col] = dict
                j += 1
        
        self.imageRowLeft = 0
        self.imageColLeft = 0
        self.imageRowRight = 0
        self.imageColRight = len(self.charBoard[0]) - 1
                
        #for row in range(len(self.charBoard)):
            #print(self.charBoard[row])
                
        for charLeft in self.charBoard[self.imageRowLeft][self.imageColLeft]:
            self.currentLeftCharacter = charLeft
            self.currentLeftImage = self.charBoard[self.imageRowLeft][self.imageColLeft][charLeft]
        
        for charRight in self.charBoard[self.imageRowRight][self.imageColRight]:
            self.currentRightCharacter = charRight
            self.currentRightImage = self.charBoard[self.imageRowRight][self.imageColRight][charRight]
        
        self.SelectCharFont = DrawText.createFont("Alger", 50)
        self.SelectCharText = DrawText.createText(text = "Select Character", color = CollegiateCombat.red, fontType = self.SelectCharFont)
        self.SelectCharTextCX, self.SelectCharTextCY = self.width // 2, 20
        
        self.PressEnterFont = DrawText.createFont("Alger", 40)
        self.PressEnterText = DrawText.createText(text = "Press Enter To Continue", color = CollegiateCombat.red, fontType = self.PressEnterFont)
        self.PressEnterTextCX, self.PressEnterTextCY = self.width // 2, (self.height // 2 + 15)
        
        self.LeftInfoFont = DrawText.createFont("Alger", 25)
        self.LeftInfoText = DrawText.createText(text = "Use W,A,S,D", color = CollegiateCombat.white, fontType = self.LeftInfoFont)
        self.LeftInfoTextCX, self.LeftInfoTextCY = self.width // 9, self.height // 4
        
        self.RightInfoFont = DrawText.createFont("Alger", 25)
        self.RightInfoText = DrawText.createText(text = "Use Arrow Keys", color = CollegiateCombat.white, fontType = self.RightInfoFont)
        self.RightInfoTextCX, self.RightInfoTextCY = (8 * self.width) // 9, self.height // 4
        
        self.CharacterLeftFont = DrawText.createFont("Alger", 20)
        self.CharacterLeftText = DrawText.createText(text = "%s" %self.currentLeftCharacter, color = CollegiateCombat.white, fontType = self.CharacterLeftFont)
        self.CharacterLeftTextCX, self.CharacterLeftTextCY = ( ( (2 * self.iconImageLeftX) + self.iconImageWidth) // 2), (self.iconImageY + self.iconImageHeight + 25)
        
        self.CharacterRightFont = DrawText.createFont("Alger", 20)
        self.CharacterRightText = DrawText.createText(text = "%s" %self.currentRightCharacter, color = CollegiateCombat.white, fontType = self.CharacterRightFont)
        self.CharacterRightTextCX, self.CharacterRightTextCY = ( ( (2 * self.iconImageRightX) + self.iconImageWidth) // 2), (self.iconImageY + self.iconImageHeight + 25)

    def keyPressed(self, code, mod, dt):
        
        # Move around character selection board with wrap around
        if code == pygame.K_w:
            if self.imageRowLeft > 0:
                self.imageRowLeft -= 1
            else: self.imageRowLeft = (len(self.charBoard) - 1)
        if code == pygame.K_s:
            if self.imageRowLeft < (len(self.charBoard) - 1):
                self.imageRowLeft += 1
            else: self.imageRowLeft = 0
        if code == pygame.K_a:
            if self.imageColLeft > 0:
                self.imageColLeft -= 1
            else: self.imageColLeft = (len(self.charBoard[0]) - 1)
        if code == pygame.K_d:
            if self.imageColLeft < (len(self.charBoard[0]) - 1):
                self.imageColLeft += 1
            else: self.imageColLeft = 0
        
        if code == pygame.K_UP:
            if self.imageRowRight > 0:
                self.imageRowRight -= 1
            else: self.imageRowRight = (len(self.charBoard) - 1)
        if code == pygame.K_DOWN:
            if self.imageRowRight < (len(self.charBoard) - 1):
                self.imageRowRight += 1
            else: self.imageRowRight = 0
        if code == pygame.K_LEFT:
            if self.imageColRight > 0:
                self.imageColRight -= 1
            else: self.imageColRight = (len(self.charBoard[0]) - 1)
        if code == pygame.K_RIGHT:
            if self.imageColRight < (len(self.charBoard[0]) - 1):
                self.imageColRight += 1
            else: self.imageColRight = 0
            
        for charLeft in self.charBoard[self.imageRowLeft][self.imageColLeft]:
            self.currentLeftCharacter = charLeft
            self.currentLeftImage = self.charBoard[self.imageRowLeft][self.imageColLeft][charLeft]
        
        for charRight in self.charBoard[self.imageRowRight][self.imageColRight]:
            self.currentRightCharacter = charRight
            self.currentRightImage = self.charBoard[self.imageRowRight][self.imageColRight][charRight]
        #print("Left=(%d, %d), Right=(%d, %d)" %(self.imageRowLeft, self.imageColLeft, self.imageRowRight, self.imageColRight))
        
        if code == pygame.K_RETURN:
            #print("Starting Game! with Left:%s and Right:%s" %(self.currentLeftCharacter, self.currentRightCharacter))
            # Set the chosen characters
            CollegiateCombat.character1 = self.currentLeftCharacter
            CollegiateCombat.character2 = self.currentRightCharacter
            # Continue to next screen
            BackgroundSelect().run()
    
    def timerFired(self, dt):
        pass

    def redrawAll(self, screen):
        # Fill Background first
        screen.fill(CollegiateCombat.purple)
        
        # Create boarder attributes i.e. dimensions and color
        leftSelectColor = CollegiateCombat.green
        rightSelectColor = CollegiateCombat.gold
        
        rectToIconImageSpace = 5
        iconLeftRectX = self.iconImageLeftX - rectToIconImageSpace
        iconRightRectX = self.iconImageRightX - rectToIconImageSpace
        iconRectY = self.iconImageY - rectToIconImageSpace
        iconRectWidth = self.iconImageWidth + (2*rectToIconImageSpace)
        iconRectHeight = self.iconImageHeight + (2*rectToIconImageSpace)
        
        # Create Left Icon Boarder
        pygame.draw.rect( screen, leftSelectColor, (iconLeftRectX, iconRectY, iconRectWidth, iconRectHeight) )
        leftIconImage = pygame.transform.scale( self.currentLeftImage, (self.iconImageWidth, self.iconImageHeight) )
        screen.blit( leftIconImage, (self.iconImageLeftX, self.iconImageY) )
            
        # Create right icon boarder
        pygame.draw.rect( screen, rightSelectColor, (iconRightRectX, iconRectY, iconRectWidth, iconRectHeight))
        rightIconImage = pygame.transform.scale( self.currentRightImage, (self.iconImageWidth, self.iconImageHeight) )
        screen.blit( rightIconImage, (self.iconImageRightX, self.iconImageY) )
        
        # Create board of characters with selection boarders
        
        # Create left and right selection boarders
        rectToImageSpace = 5
        boardIconRectWidth = self.rectWidth + (2*rectToImageSpace)
        boardIconRectWidth = self.rectHeight + (2*rectToImageSpace)
        
        leftSelectX = self.width // 2 - self.rectWidth - 60 - rectToImageSpace + self.imageColLeft * ( self.rectWidth + (2*rectToImageSpace) )
        leftSelectY = self.boardY = self.height // 2 + 50 - rectToImageSpace + self.imageRowLeft * ( self.rectHeight + (2*rectToImageSpace) )
        pygame.draw.rect( screen, leftSelectColor, (leftSelectX, leftSelectY, boardIconRectWidth, boardIconRectWidth) )
        
        rightSelectX = self.width // 2 - self.rectWidth - 60 - rectToImageSpace + self.imageColRight * ( self.rectWidth + (2*rectToImageSpace) )
        rightSelectY = self.boardY = self.height // 2 + 50 - rectToImageSpace + self.imageRowRight * ( self.rectHeight + (2*rectToImageSpace) )
        pygame.draw.rect( screen, rightSelectColor, (rightSelectX, rightSelectY, boardIconRectWidth, boardIconRectWidth) )
        
        # Draw images of the board
        for row in range(len(self.charBoard)):
            for col in range(len(self.charBoard[0])):
                for key in self.charBoard[row][col]:
                    self.boardX = self.width // 2 - self.rectWidth - 60 + col * ( self.rectWidth + (2*rectToImageSpace) )
                    self.boardY = self.height // 2 + 50 + row * ( self.rectHeight + (2*rectToImageSpace) )
                    screen.blit( self.charBoard[row][col][key], (self.boardX, self.boardY) )
        
        # Draw Text
        self.CharacterLeftText = DrawText.createText(text = "%s" %self.currentLeftCharacter, color = CollegiateCombat.white, fontType = self.CharacterLeftFont)
        self.CharacterRightText = DrawText.createText(text = "%s" %self.currentRightCharacter, color = CollegiateCombat.white, fontType = self.CharacterRightFont)
        
        DrawText.drawText(screen, self.SelectCharText, self.SelectCharTextCX, self.SelectCharTextCY)
        DrawText.drawText(screen, self.PressEnterText, self.PressEnterTextCX, self.PressEnterTextCY)
        DrawText.drawText(screen, self.LeftInfoText, self.LeftInfoTextCX, self.LeftInfoTextCY)
        DrawText.drawText(screen, self.RightInfoText, self.RightInfoTextCX, self.RightInfoTextCY)
        DrawText.drawText(screen, self.CharacterLeftText, self.CharacterLeftTextCX, self.CharacterLeftTextCY)
        DrawText.drawText(screen, self.CharacterRightText, self.CharacterRightTextCX, self.CharacterRightTextCY)

# CharacterSelect(1200, 600).run()
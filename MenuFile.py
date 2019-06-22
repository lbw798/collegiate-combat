'''
Borrowed from Game.py which was created by Lukas Peraza
    url: https://github.com/LBPeraza/Pygame-Asteroids

Actually implements the game

'''
import pygame
from CollegiateCombatFile import CollegiateCombat
import os
from CharacterSelectFile import CharacterSelect
from DrawTextFile import DrawText

# right in variable means things on right side of screen, left means left side of screen
class Menu(CollegiateCombat):
    def init(self):
        
        CollegiateCombat.mode == "Menu"
        
        # Add a background
        self.background = pygame.image.load("images/backgrounds/menuBackground.png")
        
        wBackground, hBackground = self.width, self.height
        self.background = pygame.transform.scale( self.background, ( wBackground, hBackground) )
        
        # Add credit Images
        
        self.creditX, self.creditY = 0, 0
        
        self.creditImages = []
        
        self.creditsIndex = 0
        
        path = "images/credits"
        
        for imageName in os.listdir(path):
            
            image = pygame.image.load(path + os.sep + imageName)
            
            w, h = image.get_size()
            
            factor = self.width // w
            
            w = self.width
            
            h = 1580
            
            image = pygame.transform.scale( image, ( w, h ) )
            
            self.creditImages.append(image)
        
        self.creditWidth, self.creditHeight = self.creditImages[0].get_size()
        
        print("credit height =", self.creditHeight)
        print("screen height =", self.height)
        
        
        self.isOptions = False
        self.isCredits = False
        
        self.isMusicPlaying = True
        
        # Main menu title
        
        self.TitleFont = DrawText.createFont("Alger", 110)
        self.TitleText = DrawText.createText(text = "Collegiate Combat", color = CollegiateCombat.white, fontType = self.TitleFont)
        self.TitleCX, self.TitleCY = self.width // 2, 100
        
        # Make main menu buttons
        
        self.mainRectOutline = 2
        self.mainRectBoarder = 4
        self.mainRectWidth = 150
        self.mainRectHeight = 70
        self.mainRectSpace = 20 + self.mainRectHeight
        self.mainRectX = (self.width // 2) - (self.mainRectWidth // 2)
        
        self.playRectY = (3 * self.height) // 7
        
        self.optionsRectY = self.playRectY + self.mainRectSpace
        
        self.creditsRectY = self.optionsRectY + self.mainRectSpace
        
            # Render Text:
        
        self.PlayFont = DrawText.createFont("Alger", 50)
        self.PlayText = DrawText.createText(text = "Play", color = CollegiateCombat.black, fontType = self.PlayFont)
        self.PlayTextCX, self.PlayTextCY = ( (2 * self.mainRectX) + self.mainRectWidth) // 2, ( (2 * self.playRectY) + self.mainRectHeight) // 2
        
        self.OptionsFont = DrawText.createFont("Alger", 35)
        self.OptionsText = DrawText.createText(text = "Options", color = CollegiateCombat.black, fontType = self.OptionsFont)
        self.OptionsTextCX, self.OptionsTextCY = ( (2 * self.mainRectX) + self.mainRectWidth) // 2, ( (2 * self.optionsRectY) + self.mainRectHeight) // 2
        
        self.CreditsFont = DrawText.createFont("Alger", 35)
        self.CreditsText = DrawText.createText(text = "Credits", color = CollegiateCombat.black, fontType = self.CreditsFont)
        self.CreditsTextCX, self.CreditsTextCY = ( (2 * self.mainRectX) + self.mainRectWidth) // 2, ( (2 * self.creditsRectY) + self.mainRectHeight) // 2
        # Draw options menu buttons and text
            
        self.marginOptionsMenu = 10
        self.textSizeOptionsMenu = 50
        
            # Options title
        self.OptionsFontOptionsMenu = DrawText.createFont("Alger", 70)
        self.OptionsTextOptionsMenu = DrawText.createText(text = "Options", color = CollegiateCombat.white, fontType = self.OptionsFontOptionsMenu)
        self.OptionsTextOptionsMenuCX, self.OptionsTextOptionsMenuCY = self.width // 2, 35
        
            # Music text
        self.MusicFontOptionsMenu = DrawText.createFont("Alger", self.textSizeOptionsMenu)
        self.MusicTextOptionsMenu = DrawText.createText(text = "Music", color = CollegiateCombat.white, fontType = self.MusicFontOptionsMenu)
        self.MusicTextOptionsMenuCX, self.MusicTextOptionsMenuCY = self.marginOptionsMenu + (2 * self.textSizeOptionsMenu), self.OptionsTextOptionsMenuCY + (2 * self.textSizeOptionsMenu)
        
            # On/Off buttons and text
                
        self.onOffRectOutline = 2
        self.onffRectBoarder = 4
        self.onOffRectWidth = 150
        self.onOffRectHeight = 70
        self.onOffRectSpace = 20 + self.onOffRectWidth
        self.onOffRectY = self.MusicTextOptionsMenuCY - 35
        
        self.onRectX = self.MusicTextOptionsMenuCX + (self.onOffRectSpace // 2)
        
        self.offRectX = self.onRectX + self.onOffRectSpace
        
        self.OnFontOptionsMenu = DrawText.createFont("Alger", self.textSizeOptionsMenu)
        self.OnTextOptionsMenu = DrawText.createText(text = "On", color = CollegiateCombat.white, fontType = self.OnFontOptionsMenu)
        self.OnTextOptionsMenuCX, self.OnTextOptionsMenuCY = ( (2 * self.onRectX) + self.onOffRectWidth) // 2, ( (2 * self.onOffRectY) + self.onOffRectHeight) // 2
        
        self.OffFontOptionsMenu = DrawText.createFont("Alger", self.textSizeOptionsMenu)
        self.OffTextOptionsMenu = DrawText.createText(text = "Off", color = CollegiateCombat.white, fontType = self.OffFontOptionsMenu)
        self.OffTextOptionsMenuCX, self.OffTextOptionsMenuCY = ( (2 * self.offRectX) + self.onOffRectWidth) // 2, ( (2 * self.onOffRectY) + self.onOffRectHeight) // 2
        
            # Back button
        
        self.backWidth = 50
        self.backHeight = 25
        self.backP1 = (self.marginOptionsMenu, self.OptionsTextOptionsMenuCY)
        self.backP2 = ( (self.backP1[0] + self.backWidth), ( self.backP1[1] - (self.backHeight // 2) ) )
        self.backP3 = ( self.backP2[0], (self.backP2[1] + self.backHeight) )
        self.backPoints = [self.backP1, self.backP2, self.backP3]
        
            # In game info
            
                # In-Game Text Title
        self.InGameFontOptionsMenu = DrawText.createFont("Alger", 50)
        self.InGameTextOptionsMenu = DrawText.createText(text = "In-Game Controls", color = CollegiateCombat.white, fontType = self.InGameFontOptionsMenu)
        self.InGameTextOptionsMenuCX, self.InGameTextOptionsMenuCY = self.OptionsTextOptionsMenuCX, self.MusicTextOptionsMenuCY + 100
        
                # Move Labels
        self.moveTextSize = 40
        self.moveFont = DrawText.createFont("Alger", self.moveTextSize)
        self.MoveText = DrawText.createText(text = "Move", color = CollegiateCombat.silver, fontType = self.moveFont)
        self.MotionText = DrawText.createText(text = "Motion", color = CollegiateCombat.white, fontType = self.moveFont)
        self.BlockText = DrawText.createText(text = "Block", color = CollegiateCombat.red, fontType = self.moveFont)
        self.PunchText = DrawText.createText(text = "Punch", color = CollegiateCombat.lightBlue, fontType = self.moveFont)
        self.KickText = DrawText.createText(text = "Kick", color = CollegiateCombat.green, fontType = self.moveFont)
        self.SpecialText = DrawText.createText(text = "Special", color = CollegiateCombat.gold, fontType = self.moveFont)
        self.moveText = [self.MoveText, self.MotionText, self.BlockText, self.PunchText, self.KickText, self.SpecialText]
        
        self.moveTextCX, self.moveTextCY = (self.width // 4), self.InGameTextOptionsMenuCY + 50
            
                # Move Buttons
        self.buttonTextSize = 30
        self.buttonFont = DrawText.createFont("Alger", self.buttonTextSize)
        
        self.Player1Text = DrawText.createText(text = "Player 1", color = CollegiateCombat.orange, fontType = self.buttonFont)
        self.Player2Text = DrawText.createText(text = "Player 2", color = CollegiateCombat.orange, fontType = self.buttonFont)
        
        self.Motion1Text = DrawText.createText(text = "W, A, D", color = CollegiateCombat.white, fontType = self.buttonFont)
        self.Motion2Text = DrawText.createText(text = "Up, Left, Right", color = CollegiateCombat.white, fontType = self.buttonFont)
        
        self.Block1Text = DrawText.createText(text = "S", color = CollegiateCombat.red, fontType = self.buttonFont)
        self.Block2Text = DrawText.createText(text = "Down", color = CollegiateCombat.red, fontType = self.buttonFont)
        
        self.Punch1Text = DrawText.createText(text = "V", color = CollegiateCombat.lightBlue, fontType = self.buttonFont)
        self.Punch2Text = DrawText.createText(text = "L", color = CollegiateCombat.lightBlue, fontType = self.buttonFont)
        
        self.Kick1Text = DrawText.createText(text = "C", color = CollegiateCombat.green, fontType = self.buttonFont)
        self.Kick2Text = DrawText.createText(text = "K", color = CollegiateCombat.green, fontType = self.buttonFont)
        
        self.Special1Text = DrawText.createText(text = "Space x 2", color = CollegiateCombat.gold, fontType = self.buttonFont)
        self.Special2Text = DrawText.createText(text = "J x 2", color = CollegiateCombat.gold, fontType = self.buttonFont)
        
        self.buttonText1 = [self.Player1Text, self.Motion1Text, self.Block1Text, self.Punch1Text, self.Kick1Text, self.Special1Text]
        self.buttonText2 = [self.Player2Text, self.Motion2Text, self.Block2Text, self.Punch2Text, self.Kick2Text, self.Special2Text]
        
        self.button1TextCX, self.button2TextCX = self.moveTextCX - 200, self.moveTextCX + 200
        
                # Music In game controls
        
        self.MusicInGameFontOptionsMenu = DrawText.createFont("Alger", self.textSizeOptionsMenu)
        self.MusicInGameTextOptionsMenu = DrawText.createText(text = "Music", color = CollegiateCombat.white, fontType = self.MusicInGameFontOptionsMenu)
        self.MusicInGameTextOptionsMenuCX, self.MusicInGameTextOptionsMenuCY = ( (3 * self.width) // 4 ), self.InGameTextOptionsMenuCY + 100
        
                    # On and Off in game buttons
        self.OnOffInGameTextOptionsMenuCY = self.MusicInGameTextOptionsMenuCY + 50
        self.OnOffInGameTextOptionsMenuSpace = 100
        
        self.OnOffInGameFontOptionsMenu = DrawText.createFont("Alger", self.textSizeOptionsMenu)
        
        self.OnInGameTextOptionsMenu = DrawText.createText(text = "On: 'M'", color = CollegiateCombat.white, fontType = self.OnOffInGameFontOptionsMenu)
        self.OnInGameTextOptionsMenuCX = self.MusicInGameTextOptionsMenuCX - self.OnOffInGameTextOptionsMenuSpace
        
        self.OffInGameTextOptionsMenu = DrawText.createText(text = "Off: 'N'", color = CollegiateCombat.white, fontType = self.OnOffInGameFontOptionsMenu)
        self.OffInGameTextOptionsMenuCX = self.MusicInGameTextOptionsMenuCX + self.OnOffInGameTextOptionsMenuSpace
        
                # Pause In game controls
        
        self.PauseInGameFontOptionsMenu = DrawText.createFont("Alger", self.textSizeOptionsMenu)
        self.PauseInGameTextOptionsMenu = DrawText.createText(text = "Pause: 'P'", color = CollegiateCombat.white, fontType = self.PauseInGameFontOptionsMenu)
        self.PauseInGameTextOptionsMenuCX, self.PauseInGameTextOptionsMenuCY = ( (3 * self.width) // 4 ), self.OnOffInGameTextOptionsMenuCY + 65
        
        self.RestartInGameFontOptionsMenu = DrawText.createFont("Alger", self.textSizeOptionsMenu)
        self.RestartInGameTextOptionsMenu = DrawText.createText(text = "Restart: 'R'", color = CollegiateCombat.white, fontType = self.RestartInGameFontOptionsMenu)
        self.RestartInGameTextOptionsMenuCX, self.RestartInGameTextOptionsMenuCY = self.PauseInGameTextOptionsMenuCX, self.PauseInGameTextOptionsMenuCY + 65

    def keyPressed(self, code, mod, dt):
        
        # Move between documents, and through document
        
        if not self.isOptions and self.isCredits:
            
            if code == pygame.K_LEFT and self.creditsIndex > 0:
                self.creditsIndex -= 1
                
            if code == pygame.K_RIGHT and self.creditsIndex < ( len(self.creditImages) - 1):
                self.creditsIndex += 1
            
            if code == pygame.K_UP and self.creditY < 0:
                self.creditY += 50
                
            if code == pygame.K_DOWN and self.creditY > -930:
                self.creditY -= 50
    
    def mousePressed(self, x, y):
        
        # Main menu functionality:
        
        if not self.isOptions and not self.isCredits:
            
            if ( x >= (self.mainRectX - self.mainRectBoarder) and x <= ( self.mainRectX + self.mainRectWidth + (2 * self.mainRectBoarder) ) ) and ( y >= (  self.playRectY - self.mainRectBoarder ) and y <= ( self.playRectY + self.mainRectHeight + (2 * self.mainRectBoarder) ) ):
                CollegiateCombat.characterSelectClass = CharacterSelect
                print(CollegiateCombat.characterSelectClass)
                CharacterSelect(1200, 600).run()
                print("clicked play")
                
            if ( x >= (self.mainRectX - self.mainRectBoarder) and x <= ( self.mainRectX + self.mainRectWidth + (2 * self.mainRectBoarder) ) ) and ( y >= (  self.optionsRectY - self.mainRectBoarder ) and y <= ( self.optionsRectY + self.mainRectHeight + (2 * self.mainRectBoarder) ) ):
                self.isOptions = True
                print("clicked options")
            
            if ( x >= (self.mainRectX - self.mainRectBoarder) and x <= ( self.mainRectX + self.mainRectWidth + (2 * self.mainRectBoarder) ) ) and ( y >= (  self.creditsRectY - self.mainRectBoarder ) and y <= ( self.creditsRectY + self.mainRectHeight + (2 * self.mainRectBoarder) ) ):
                self.isCredits = True
                print("clicked credits")
        
        # Options menu functionality:
        if self.isOptions and not self.isCredits:
            
            # Turn Music on
            if ( x >= (self.onRectX - self.onffRectBoarder) and x <= ( self.onRectX + self.onOffRectWidth + (2 * self.onffRectBoarder) ) ) and ( y >= (  self.onOffRectY - self.onffRectBoarder ) and y <= ( self.onOffRectY + self.onOffRectHeight + (2 * self.onffRectBoarder) ) ) and not CollegiateCombat.isMusicPlaying:
                CollegiateCombat.isMusicPlaying = True
                CollegiateCombat.playMusic()
                print("music on")
            
            # Turn music off
            if ( x >= (self.offRectX - self.onffRectBoarder) and x <= ( self.offRectX + self.onOffRectWidth + (2 * self.onffRectBoarder) ) ) and ( y >= (  self.onOffRectY - self.onffRectBoarder ) and y <= ( self.onOffRectY + self.onOffRectHeight + (2 * self.onffRectBoarder) ) ) and CollegiateCombat.isMusicPlaying:
                CollegiateCombat.isMusicPlaying = False
                CollegiateCombat.stopMusic()
                print("music off")
        
        # Back button functionality:
        if self.isOptions or self.isCredits:
            
            if (x >= self.backP1[0] and x <= self.backP2[0]) and ( y >= self.backP2[1] and y<= self.backP3[1] ):
                
                self.isOptions, self.isCredits = False, False
                 
    def timerFired(self, dt):
        pass

    def redrawAll(self, screen):

        # Draw Main Menu
        if not self.isOptions and not self.isCredits:
            
            # Add background
            screen.blit( self.background, (0, 0) )
            
            # Add Title
            DrawText.drawText(screen, self.TitleText, self.TitleCX, self.TitleCY)
        
            # Draw Menu Text
            
                # Play Button
            pygame.draw.rect( screen, CollegiateCombat.white, ( self.mainRectX - self.mainRectBoarder, self.playRectY - self.mainRectBoarder, self.mainRectWidth + (2 * self.mainRectBoarder), self.mainRectHeight + (2 * self.mainRectBoarder) ) )
            pygame.draw.rect( screen, CollegiateCombat.black, ( self.mainRectX - self.mainRectOutline, self.playRectY - self.mainRectOutline, self.mainRectWidth + (2 * self.mainRectOutline), self.mainRectHeight + (2 * self.mainRectOutline) ) )
            pygame.draw.rect( screen, CollegiateCombat.silver, (self.mainRectX, self.playRectY, self.mainRectWidth, self.mainRectHeight) )
            DrawText.drawText(screen, self.PlayText, self.PlayTextCX, self.PlayTextCY)
            
                # Options Button
            pygame.draw.rect( screen, CollegiateCombat.white, ( self.mainRectX - self.mainRectBoarder, self.optionsRectY - self.mainRectBoarder, self.mainRectWidth + (2 * self.mainRectBoarder), self.mainRectHeight + (2 * self.mainRectBoarder) ) )
            pygame.draw.rect( screen, CollegiateCombat.black, ( self.mainRectX - self.mainRectOutline, self.optionsRectY - self.mainRectOutline, self.mainRectWidth + (2 * self.mainRectOutline), self.mainRectHeight + (2 * self.mainRectOutline) ) )
            pygame.draw.rect( screen, CollegiateCombat.silver, (self.mainRectX, self.optionsRectY, self.mainRectWidth, self.mainRectHeight) )
            DrawText.drawText(screen, self.OptionsText, self.OptionsTextCX, self.OptionsTextCY)
            
                # Credits Button
            pygame.draw.rect( screen, CollegiateCombat.white, ( self.mainRectX - self.mainRectBoarder, self.creditsRectY - self.mainRectBoarder, self.mainRectWidth + (2 * self.mainRectBoarder), self.mainRectHeight + (2 * self.mainRectBoarder) ) )
            pygame.draw.rect( screen, CollegiateCombat.black, ( self.mainRectX - self.mainRectOutline, self.creditsRectY - self.mainRectOutline, self.mainRectWidth + (2 * self.mainRectOutline), self.mainRectHeight + (2 * self.mainRectOutline) ) )
            pygame.draw.rect( screen, CollegiateCombat.silver, (self.mainRectX, self.creditsRectY, self.mainRectWidth, self.mainRectHeight) )
            DrawText.drawText(screen, self.CreditsText, self.CreditsTextCX, self.CreditsTextCY)
        
        # Draw Options Menu
        
        if self.isOptions and not self.isCredits:
            
            # Fill Background first
            screen.fill(CollegiateCombat.purple)
        
            # Draw Options Menu Text
                
                # Options Title
            DrawText.drawText(screen, self.OptionsTextOptionsMenu, self.OptionsTextOptionsMenuCX, self.OptionsTextOptionsMenuCY)
                
                # Music text
            DrawText.drawText(screen, self.MusicTextOptionsMenu, self.MusicTextOptionsMenuCX, self.MusicTextOptionsMenuCY)
            
                # In-Game Controls Instruction
                
                    # In-Game Text Title
            
            DrawText.drawText(screen, self.InGameTextOptionsMenu, self.InGameTextOptionsMenuCX, self.InGameTextOptionsMenuCY)
            
                    # Music Info
            DrawText.drawText(screen, self.MusicInGameTextOptionsMenu, self.MusicInGameTextOptionsMenuCX, self.MusicInGameTextOptionsMenuCY)
                        
                        # On
            DrawText.drawText(screen, self.OnInGameTextOptionsMenu, self.OnInGameTextOptionsMenuCX, self.OnOffInGameTextOptionsMenuCY)
                        
                        # Off
            DrawText.drawText(screen, self.OffInGameTextOptionsMenu, self.OffInGameTextOptionsMenuCX, self.OnOffInGameTextOptionsMenuCY)
            
                # Pause Text
                
            DrawText.drawText(screen, self.PauseInGameTextOptionsMenu, self.PauseInGameTextOptionsMenuCX, self.PauseInGameTextOptionsMenuCY)
            
                # Restart Text
                
            DrawText.drawText(screen, self.RestartInGameTextOptionsMenu, self.RestartInGameTextOptionsMenuCX, self.RestartInGameTextOptionsMenuCY)
            
            moveSpace = 50
            self.moveTextCY = self.InGameTextOptionsMenuCY + 50
            for i in range(len(self.moveText)):
                print( "self.moveTextCX: %d self.moveTextCY: %d self.button1TextCX: %d self.button2TextCX: %d" %(self.moveTextCX, self.moveTextCY, self.button1TextCX, self.button2TextCX) )
                DrawText.drawText(screen, self.moveText[i], self.moveTextCX, self.moveTextCY)
                DrawText.drawText(screen, self.buttonText1[i], self.button1TextCX, self.moveTextCY)
                DrawText.drawText(screen, self.buttonText2[i], self.button2TextCX, self.moveTextCY)
                self.moveTextCY += moveSpace
            
                # On and Off text and buttons
                    
                    # On
            if CollegiateCombat.isMusicPlaying:
                
                pygame.draw.rect( screen, CollegiateCombat.white, ( self.onRectX - self.onffRectBoarder, self.onOffRectY - self.onffRectBoarder, self.onOffRectWidth + (2 * self.onffRectBoarder), self.onOffRectHeight + (2 * self.onffRectBoarder) ) )
                pygame.draw.rect( screen, CollegiateCombat.black, ( self.onRectX - self.onOffRectOutline, self.onOffRectY - self.onOffRectOutline, self.onOffRectWidth + (2 * self.onOffRectOutline), self.onOffRectHeight + (2 * self.onOffRectOutline) ) )
                pygame.draw.rect( screen, CollegiateCombat.green, (self.onRectX, self.onOffRectY, self.onOffRectWidth, self.onOffRectHeight) )   
            
            DrawText.drawText(screen, self.OnTextOptionsMenu, self.OnTextOptionsMenuCX, self.OnTextOptionsMenuCY)
                    # Off
            if not CollegiateCombat.isMusicPlaying:
                
                pygame.draw.rect( screen, CollegiateCombat.white, ( self.offRectX - self.onffRectBoarder, self.onOffRectY - self.onffRectBoarder, self.onOffRectWidth + (2 * self.onffRectBoarder), self.onOffRectHeight + (2 * self.onffRectBoarder) ) )
                pygame.draw.rect( screen, CollegiateCombat.black, ( self.offRectX - self.onOffRectOutline, self.onOffRectY - self.onOffRectOutline, self.onOffRectWidth + (2 * self.onOffRectOutline), self.onOffRectHeight + (2 * self.onOffRectOutline) ) )
                pygame.draw.rect( screen, CollegiateCombat.red, (self.offRectX, self.onOffRectY, self.onOffRectWidth, self.onOffRectHeight) )   
            
            DrawText.drawText(screen, self.OffTextOptionsMenu, self.OffTextOptionsMenuCX, self.OffTextOptionsMenuCY)
            
        if not self.isOptions and self.isCredits:
            screen.blit( self.creditImages[self.creditsIndex], (self.creditX, self.creditY) )
            
        if self.isOptions or self.isCredits:
            
            # Draw back button
            pygame.draw.polygon(screen, CollegiateCombat.silver, self.backPoints, 5)          

'''
Borrowed from Game.py which was created by Lukas Peraza
    url: https://github.com/LBPeraza/Pygame-Asteroids

Actually implements the game

'''
import pygame
from CollegiateCombatFile import CollegiateCombat
from CharacterFile import Character
from ProjectileFile import Projectile
from DrawTextFile import DrawText

# right in variable means facing right, left means facing left
class RunGame(CollegiateCombat):
    def init(self):
        
        CollegiateCombat.mode = "RunGame"
        
        CollegiateCombat.stopMusic()
        CollegiateCombat.playMusic()
        
        # Resize title image:
        self.titleImageDim = 125
        self.titleImage = pygame.transform.scale( CollegiateCombat.titleImage, (self.titleImageDim, self.titleImageDim) )
        self.titleImageW, self.titleImageH = self.titleImage.get_size()
        
        # Set game over and pause booleans
        self.isGameOver = False
        self.isPaused = False
        
        # Set ending sound boolean
        self.isEnding = False
        
        # Obtain and resize background
        w, h = self.width, self.height
        
        if "spring" in CollegiateCombat.gameBackground:
            
            self.initialBackground = pygame.image.load("images/backgrounds/game/13-pittsburgh spring.png")
            self.initialBackground = pygame.transform.scale( self.initialBackground, (w, h) )
            
            self.realBackground = pygame.image.load("images/backgrounds/game/14-pittsburgh spring alt.png")
            w, h = self.width, self.height
            self.realBackground = pygame.transform.scale( self.realBackground, (w, h) )
            
            self.background = self.initialBackground
            
        elif "spring" not in CollegiateCombat.gameBackground:
            
            self.background = pygame.image.load("images/backgrounds/game/%s.png" %CollegiateCombat.gameBackground)
            self.background = pygame.transform.scale( self.background, (w, h) )
        
        self.gameOverImage = pygame.image.load("images/gameover.png")
        # Resize game over image
        wGameOver, hGameOver = self.width, self.height
        self.gameOverImage = pygame.transform.scale( self.gameOverImage, ( wGameOver, hGameOver) )
        
        character1 = super().character1
        character2 = super().character2
        Character.init(character1)
        Character.init(character2)
        
        self.characterGroup = pygame.sprite.Group()
        self.characterRight = Character(character1, self.width, self.height, True, 1)
        self.characterGroup = pygame.sprite.Group(self.characterRight)
        
        self.characterLeft = Character(character2, self.width, self.height, False, 2)
        self.characterGroup.add(self.characterLeft)
        
        # Get character icons and resize for health and energy bars
        charIconDim = 40
        self.imageLeft = self.characterLeft.spriteDict["icon"]
        self.imageLeft = pygame.transform.scale( self.imageLeft, ( charIconDim, charIconDim ) )
        self.imageRight = self.characterRight.spriteDict["icon"]
        self.imageRight = pygame.transform.scale( self.imageRight, ( charIconDim, charIconDim ) )
        
        # Get character icons and resize for pause menu
        self.pauseCharIconDim = 100
        self.pauseImageLeft = self.characterLeft.spriteDict["icon"]
        self.pauseImageLeft = pygame.transform.scale( self.pauseImageLeft, ( self.pauseCharIconDim, self.pauseCharIconDim ) )
        self.pauseImageRight = self.characterRight.spriteDict["icon"]
        self.pauseImageRight = pygame.transform.scale( self.pauseImageRight, ( self.pauseCharIconDim, self.pauseCharIconDim ) )
        
        self.characterRightProjectiles = pygame.sprite.Group()
        self.characterLeftProjectiles = pygame.sprite.Group()
        
        # Set the sounds dictionaries equal to their appropriate sounds
        self.characterLeft.sounds = CollegiateCombat.characterSounds[self.characterLeft.character]
        
        self.characterRight.sounds = CollegiateCombat.characterSounds[self.characterRight.character]
        # print(self.characterRight.sounds)
        
        self.damage = 0
        
        self.timerFiredCounter = 0
        self.timeCount = 0
        
        self.characterLeft.isProbation = False
        self.characterRight.isProbation = False
        
        # Create a font: specify the font and size; None gives default font or specify a TTF font file from C:/Windows/Fonts
        
        # Render text
        
        self.fightFont = DrawText.createFont("Alger", 50)
        self.fightText = DrawText.createText(text = "Fight!", color = CollegiateCombat.red, fontType = self.fightFont)

        self.QPAFont = DrawText.createFont("Alger", 25)
        self.QPAText = DrawText.createText(text = "QPA", color = CollegiateCombat.red, fontType = self.QPAFont)
        self.QPATextLeftCX, self.QPATextLeftCY = 0, 0
        self.QPATextRightCX, self.QPATextRightCY = 0, 0
        
        self.SleepFont = DrawText.createFont("Alger", 25)
        self.SleepText = DrawText.createText(text = "Sleep", color = CollegiateCombat.red, fontType = self.SleepFont)
        self.SleepTextLeftCX, self.SleepTextLeftCY = 0, 0
        self.SleepTextRightCX, self.SleepTextRightCY = 0, 0
        
        # Pause Screen text
           
            # Move Labels
        self.moveTextSize = 40
        self.moveFont = DrawText.createFont("Alger", self.moveTextSize)
        self.MotionText = DrawText.createText(text = "Motion", color = CollegiateCombat.white, fontType = self.moveFont)
        self.BlockText = DrawText.createText(text = "Block", color = CollegiateCombat.red, fontType = self.moveFont)
        self.PunchText = DrawText.createText(text = "Punch", color = CollegiateCombat.lightBlue, fontType = self.moveFont)
        self.KickText = DrawText.createText(text = "Kick", color = CollegiateCombat.green, fontType = self.moveFont)
        self.SpecialText = DrawText.createText(text = "Special", color = CollegiateCombat.gold, fontType = self.moveFont)
        self.moveText = [self.MotionText, self.BlockText, self.PunchText, self.KickText, self.SpecialText]
        
        self.moveTextCX, self.moveTextCY = 0, 0
            
            # Move Buttons
        self.buttonTextSize = 25
        self.buttonFont = DrawText.createFont("Alger", self.buttonTextSize)
        
        self.Motion1Text = DrawText.createText(text = "W, A, D", color = CollegiateCombat.white, fontType = self.buttonFont)
        self.Motion2Text = DrawText.createText(text = "Up, Left, Right", color = CollegiateCombat.white, fontType = self.buttonFont)
        
        self.Block1Text = DrawText.createText(text = "S", color = CollegiateCombat.red, fontType = self.buttonFont)
        self.Block2Text = DrawText.createText(text = "Down", color = CollegiateCombat.red, fontType = self.buttonFont)
        
        self.Punch1Text = DrawText.createText(text = "V", color = CollegiateCombat.lightBlue, fontType = self.buttonFont)
        self.Punch2Text = DrawText.createText(text = "L", color = CollegiateCombat.lightBlue, fontType = self.buttonFont)
        
        self.Kick1Text = DrawText.createText(text = "C", color = CollegiateCombat.green, fontType = self.buttonFont)
        self.Kick2Text = DrawText.createText(text = "K", color = CollegiateCombat.green, fontType = self.buttonFont)
        
        self.Special1Text = DrawText.createText(text = "Space x 2: %s" %self.characterRight.specialName, color = CollegiateCombat.gold, fontType = self.buttonFont)
        self.Special2Text = DrawText.createText(text = "J x 2: %s" %self.characterLeft.specialName, color = CollegiateCombat.gold, fontType = self.buttonFont)
        
        self.buttonText1 = [self.Motion1Text, self.Block1Text, self.Punch1Text, self.Kick1Text, self.Special1Text]
        self.buttonText2 = [self.Motion2Text, self.Block2Text, self.Punch2Text, self.Kick2Text, self.Special2Text]
        
        self.button1TextCX, self.button2TextCX, self.buttonTextCY = 0, 0, 0
        
            # Select Character Text
        
        self.restartRectOutline = 2
        self.restartRectBoarder = 4        
        self.restartRectWidth = 200
        self.restartRectHeight = 70
        self.restartRectSpace = 20 + self.restartRectWidth
        self.restartRectY = (self.height // 2) + 130
        self.restartRectX = (self.width // 2) - (self.restartRectWidth // 2)
        
        self.RestartFont = DrawText.createFont("Alger", 35)
        self.RestartText = DrawText.createText(text = "Restart", color = CollegiateCombat.white, fontType = self.RestartFont)
        self.RestartTextCX, self.RestartTextCY = ( (2 * self.restartRectX) + self.restartRectWidth) // 2, ( (2 * self.restartRectY) + self.restartRectHeight) // 2
        
        # Create Winner Screen
        self.winner = ""
        self.WinnerFont = DrawText.createFont("Alger", 80)
        self.WinnerTextCX, self.WinnerTextCY = self.width // 2, (3 * self.height) // 4
        
    def mousePressed(self, x, y):
        
        # Allow mouse pressed functionality inpause screen:
        
        if self.isPaused:
            if ( x >= (self.restartRectX - self.restartRectBoarder) and x <= ( self.restartRectX + self.restartRectWidth + (2 * self.restartRectBoarder) ) ) and ( y >= (  self.restartRectY - self.restartRectBoarder ) and y <= ( self.restartRectY + self.restartRectHeight + (2 * self.restartRectBoarder) ) ):
                
                RunGame().run()

    def keyPressed(self, code, mod, dt):
        
        # Enables pausing
        if code == pygame.K_p:
            self.isPaused = not self.isPaused
        
        if code == pygame.K_r:
            RunGame().run()
        
        # Control Music
        if code == pygame.K_n:
            if CollegiateCombat.isMusicPlaying:
                CollegiateCombat.stopMusic()
        
        if code == pygame.K_m:
            if not CollegiateCombat.isMusicPlaying:
                CollegiateCombat.playMusic()
        
        if code == pygame.K_t:
            self.isGameOver = False
            CollegiateCombat.characterSelectClass().run()
        
        if not self.isGameOver and not self.isPaused:
            
            characterRightMoves = [pygame.K_SPACE]
            characterLeftMoves = [pygame.K_j]
            
            if code in characterRightMoves and len(self.characterRightProjectiles) == 0 and self.characterRight.specialCount < 30:
                self.characterRight.sounds["effect1"].play()
                if self.characterRight.isRight:
                    x = self.characterRight.x + self.characterRight.width
                else:
                    x = self.characterRight.x - self.characterRight.width
                y = self.characterRight.y
                image = self.characterRight.spriteDict["effect1"]
                w, h = image.get_size()
                r = max(w,h) // 2
                self.characterRightProjectiles.add(Projectile(x, y, image, r, self.characterRight.isRight))
            
            if code in characterLeftMoves and len(self.characterLeftProjectiles) == 0 and self.characterLeft.specialCount < 30:
                self.characterLeft.sounds["effect1"].play()
                if self.characterLeft.isRight:
                    x = self.characterLeft.x + self.characterLeft.width
                else:
                    x = self.characterLeft.x - self.characterLeft.width
                y = self.characterLeft.y
                image = self.characterLeft.spriteDict["effect1"]
                w, h = image.get_size()
                r = max(w,h) // 2
                self.characterLeftProjectiles.add(Projectile(x, y, image, r, self.characterLeft.isRight))
    
    def timerFired(self, dt):
        
        if not self.isGameOver and not self.isPaused:
            
            self.timerFiredCounter += 1
            # Timer Fired is called about 50 times per second which was initiallized as fps in the Collegiate Combat File: self.fps
            if self.timerFiredCounter > 0 and self.timerFiredCounter % self.fps == 0: 
                self.timeCount += 1

                #print("Facing Left: Taking Damage:", self.characterLeft.isDamage, "Attacking:", self.characterLeft.isAttack)
                #print("Facing Right: Taking Damage:", self.characterRight.isDamage, "Attacking:", self.characterRight.isAttack)
                
                if self.characterLeft.isDamage:
                    self.characterLeft.damageCount -= 1
                
                if self.characterLeft.damageCount <= 0:
                    if not self.characterLeft.isBlock:
                        self.characterLeft.baseImage = self.characterLeft.spriteDict["idle"]
                    self.characterRight.isAttack = False
                    self.characterLeft.isDamage = False
                    self.characterLeft.damageCount = 1
                    
                
                if self.characterRight.isDamage: 
                    self.characterRight.damageCount -= 1
                
                if self.characterRight.damageCount <= 0:
                    if not self.characterRight.isBlock:
                        self.characterRight.baseImage = self.characterRight.spriteDict["idle"]
                    self.characterLeft.isAttack = False
                    self.characterRight.isDamage = False
                    self.characterRight.damageCount = 1
            
            if not self.characterLeft.isProbation and self.characterLeft.healthColor == CollegiateCombat.red:
                self.characterLeft.isProbation = True
                CollegiateCombat.academicProbation.play()
            
            if not self.characterRight.isProbation and self.characterRight.healthColor == CollegiateCombat.red:
                self.characterRight.isProbation = True
                CollegiateCombat.academicProbation.play()
                
            if self.characterLeft.isDead or self.characterRight.isDead:
                self.isGameOver = True
            
            # Auto-reface characters towards each other    
            if self.characterLeft.x <= self.characterRight.x:
                
                self.characterLeft.isRight = True
                if not self.characterLeft.isFlipped:
                    self.characterLeft.isFlipped = True
                    
                self.characterRight.isRight = False
                if not self.characterRight.isFlipped:
                    self.characterRight.isFlipped = True
            
            elif self.characterLeft.x > self.characterRight.x:
                
                self.characterLeft.isRight = False
                if self.characterLeft.isFlipped:
                    self.characterLeft.isFlipped = True
                    
                self.characterRight.isRight = True
                if self.characterRight.isFlipped:
                    self.characterRight.isFlipped = True
            
            # Update All Sprites        
            self.characterGroup.update(dt, self.isKeyPressed, self.width, self.height)
            self.characterRightProjectiles.update(self.width, self.height)
            self.characterLeftProjectiles.update(self.width, self.height)
            
            # Configure damage code
            self.damage = 0
            if pygame.sprite.collide_circle(self.characterLeft, self.characterRight):
                if self.characterLeft.isPunch and self.characterLeft.punchCount == 20:
                    #print("Left Punch")
                    self.characterLeft.isAttack = True
                    self.characterRight.isDamage = True
                    self.damage = self.characterLeft.punchDamage
                    if self.characterRight.isBlock:
                        self.damage //= 3
                    self.characterRight.loseHealth(self.damage)
                    self.characterLeft.getEnergy()
                if self.characterLeft.isKick and self.characterLeft.kickCount == 20:
                    #print("Left Kick")
                    self.characterLeft.isAttack = True
                    self.characterRight.isDamage = True
                    self.damage = self.characterLeft.kickDamage
                    if self.characterRight.isBlock:
                        self.damage //= 3
                    self.characterRight.loseHealth(self.damage)
                    self.characterLeft.getEnergy()
                if self.characterRight.isPunch and self.characterRight.punchCount == 20:
                    #print("Right Punch")
                    self.characterRight.isAttack = True
                    self.characterLeft.isDamage = True
                    self.damage = self.characterRight.punchDamage
                    if self.characterLeft.isBlock:
                        self.damage //= 3
                    self.characterLeft.loseHealth(self.damage)
                    self.characterRight.getEnergy()
                if self.characterRight.isKick and self.characterRight.kickCount == 20:
                    #print("Right Kick")
                    self.characterRight.isAttack = True
                    self.characterLeft.isDamage = True
                    self.damage = self.characterRight.kickDamage
                    if self.characterLeft.isBlock:
                        self.damage //= 3
                    self.characterLeft.loseHealth(self.damage)
                    self.characterRight.getEnergy()
            
            for specialLeft in self.characterLeftProjectiles:
                if pygame.sprite.collide_circle(self.characterRight, specialLeft):
                    #print("Left Special")
                    self.characterLeft.isAttack = True
                    self.characterRight.isDamage = True
                    self.damage = self.characterLeft.specialDamage
                    if self.characterRight.isBlock:
                        self.damage //= 3
                    self.characterRight.loseHealth(self.damage)
                    specialLeft.kill()
            
            for specialRight in self.characterRightProjectiles:
                if pygame.sprite.collide_circle(self.characterLeft, specialRight):
                    #print("Right Special")
                    self.characterRight.isAttack = True
                    self.characterLeft.isDamage = True
                    self.damage = self.characterRight.specialDamage
                    if self.characterLeft.isBlock:
                        self.damage //= 3
                    self.characterLeft.loseHealth(self.damage)
                    specialRight.kill()
            
            if "spring" in CollegiateCombat.gameBackground:
                if self.timeCount == 10:
                    self.background = self.realBackground

    def redrawAll(self, screen):
        # Add background
        screen.blit( self.background, (0, 0) )
        
        # Draw Character Bars
        if self.timeCount <= 2:

            # Draw Fight Text
            DrawText.drawText(screen, self.fightText, self.width // 2, self.height // 2)
                
        # Left Facing Character Energy Health & Icon
        imageDistance = 45
        imageY = self.characterLeft.healthY
        imageLeftX = self.characterLeft.healthX - imageDistance
        
        screen.blit( self.imageLeft, (imageLeftX, imageY) )
        
        pygame.draw.rect( screen, self.characterLeft.healthColor, (self.characterLeft.healthX, self.characterLeft.healthY, self.characterLeft.health, self.characterLeft.barHeight) )
        
        pygame.draw.rect( screen, CollegiateCombat.blue, (self.characterLeft.energyX, self.characterLeft.energyY, self.characterLeft.energy, self.characterLeft.barHeight) )
        
        # Right Facing Character Energy Health & Icon
        imageRightX = self.characterRight.healthX - imageDistance
        
        screen.blit( self.imageRight, (imageRightX, imageY) )
        
        pygame.draw.rect( screen, self.characterRight.healthColor, (self.characterRight.healthX, self.characterRight.healthY, self.characterRight.health, self.characterRight.barHeight) )
        
        pygame.draw.rect( screen, CollegiateCombat.blue, (self.characterRight.energyX, self.characterRight.energyY, self.characterRight.energy, self.characterRight.barHeight) )
        
        # Add other game objects in specified order
        self.characterGroup.draw(screen)
        self.characterRightProjectiles.draw(screen)
        self.characterLeftProjectiles.draw(screen)
        
        # Draw Health and Energy Labels
        labelSpace = 35
        
        self.QPATextLeftCX, self.QPATextLeftCY = (self.characterLeft.healthX + self.characterLeft.maxHealth + labelSpace), ( self.characterLeft.healthY + (self.characterLeft.barHeight // 2) )
        DrawText.drawText(screen, self.QPAText, self.QPATextLeftCX, self.QPATextLeftCY)
        
        self.QPATextRightCX, self.QPATextRightCY = (self.characterRight.healthX + self.characterRight.maxHealth + labelSpace), ( self.characterRight.healthY + (self.characterRight.barHeight // 2) )
        DrawText.drawText(screen, self.QPAText, self.QPATextRightCX, self.QPATextRightCY)
        
        labelSpace = 45
        
        self.SleepTextLeftCX, self.SleepTextLeftCY = (self.characterLeft.energyX + self.characterLeft.maxEnergy + labelSpace), ( self.characterLeft.energyY + (self.characterLeft.barHeight // 2) )
        DrawText.drawText(screen, self.SleepText, self.SleepTextLeftCX, self.SleepTextLeftCY)
        
        self.SleepTextRightCX, self.SleepTextRightCY = (self.characterRight.energyX + self.characterRight.maxEnergy + labelSpace), ( self.characterRight.energyY + (self.characterRight.barHeight // 2) )
        DrawText.drawText(screen, self.SleepText, self.SleepTextRightCX, self.SleepTextRightCY)
            
        # Draw pause Screen
        if self.isPaused:
            
            pauseRectX = self.width // 9
            pauseRectY = self.height // 9
            pauseRectWidth = (7 * self.width) // 9
            pauseRectHeight = (7 * self.height) // 9
            pygame.draw.rect( screen, CollegiateCombat.purple, (pauseRectX, pauseRectY, pauseRectWidth, pauseRectHeight) )
            
            # Draw Icons and character controls:
            
                # Draw Character Icons and title image
            pauseImageMarginX = 150
            pauseImageMarginY = 25
            pauseImageRightX = pauseRectX + pauseRectWidth - self.pauseCharIconDim - pauseImageMarginX
            pauseImageLeftX = pauseRectX + pauseImageMarginX
            pauseTitleImageX = ( (2 * pauseRectX) + pauseRectWidth ) // 2 - (self.titleImageDim // 2)
            pauseImageY = pauseRectY + pauseImageMarginY
            
            screen.blit( self.titleImage, (pauseTitleImageX, pauseImageY) )
            screen.blit( self.pauseImageRight, (pauseImageLeftX, pauseImageY) )
            screen.blit( self.pauseImageLeft, (pauseImageRightX, pauseImageY) )
            
                # Draw Controls Text
            pauseTextMarginY = pauseImageY + self.pauseCharIconDim + self.moveTextSize
            pauseTextSpaceY = self.moveTextSize
            
            self.button1TextCX = pauseRectX + 200
            self.button2TextCX = pauseRectX + pauseRectWidth - 200
            self.moveTextCX = ( (2 * pauseRectX) + pauseRectWidth ) // 2
            for i in range(len(self.moveText)):
                self.moveTextCY = pauseTextMarginY + (i * pauseTextSpaceY)
                DrawText.drawText(screen, self.moveText[i], self.moveTextCX, self.moveTextCY)
                DrawText.drawText(screen, self.buttonText1[i], self.button1TextCX, self.moveTextCY)
                DrawText.drawText(screen, self.buttonText2[i], self.button2TextCX, self.moveTextCY)
                
            pygame.draw.rect( screen, CollegiateCombat.white, ( self.restartRectX - self.restartRectBoarder, self.restartRectY - self.restartRectBoarder, self.restartRectWidth + (2 * self.restartRectBoarder), self.restartRectHeight + (2 * self.restartRectBoarder) ) )
            pygame.draw.rect( screen, CollegiateCombat.black, ( self.restartRectX - self.restartRectOutline, self.restartRectY - self.restartRectOutline, self.restartRectWidth + (2 * self.restartRectOutline), self.restartRectHeight + (2 * self.restartRectOutline) ) )
            pygame.draw.rect( screen, CollegiateCombat.red, (self.restartRectX, self.restartRectY, self.restartRectWidth, self.restartRectHeight) )   
            
            DrawText.drawText(screen, self.RestartText, self.RestartTextCX, self.RestartTextCY)
            
        # Draw game over screen
        if self.isGameOver:
            
            # CollegiateCombat.stopMusic()
            
            if not self.isEnding:
                
                CollegiateCombat.kanyeGodSpeech.play()
                CollegiateCombat.kanyeGodSpeech.set_volume(1.0)
                
                self.isEnding = True
            
            screen.blit( self.gameOverImage, (0, 0) )
            
            if self.characterLeft.health > self.characterRight.health:
                #print(self.characterLeft.health, self.characterRight.health)
                self.winner = CollegiateCombat.character2
            else: self.winner = CollegiateCombat.character1
            
            self.WinnerText = DrawText.createText(text = "%s Wins" %self.winner, color = CollegiateCombat.white, fontType = self.WinnerFont)
            
            DrawText.drawText(screen, self.WinnerText, self.WinnerTextCX, self.WinnerTextCY)
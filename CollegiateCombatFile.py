'''
Borrowed from pygamegame.py which was created by Lukas Peraza
    url: https://github.com/LBPeraza/Pygame-Asteroids

- you should remove the print calls from any function you aren't using
- you might want to move the pygame.display.flip() to your redrawAll function,
    in case you don't need to update the entire display every frame (then you
    should use pygame.display.update(Rect) instead)
'''
import pygame
from DrawTextFile import DrawText
import os


class CollegiateCombat(object):
    
    # Keep Track of whether music is playing:
    isMusicPlaying = True
    
    # Keep Track of what mode of the game is running
    mode = ""
    
    # Default characters to run game without character select and used to get characters from character select
    character1 = "scorpion"
    character2 = "subzero"
    
    # Initiate some colors
    black = (0, 0, 0)
    white = (255, 255, 255)
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)
    lightBlue = (51, 255, 255)
    purple = (51, 0, 102)
    lightGreen = (25, 255, 105)
    gold = (255, 204, 0)
    silver = (224, 224, 224)
    orange = (255, 128, 0)
    
    # Initiate Text Fonts
    algerFont = None
    gameBackground = "1-outside hammershlag"
    characterSounds = {}
    
    # Get the title image
    titleImage = pygame.image.load("images/collegiatecombattitle.png")
    
    # Initialize Volume
    volume = 0.1
    
    # Enables going back to character select once initialized in Menu File
    characterSelectClass = None
    
    def init(self):
        pass

    def mousePressed(self, x, y):
        pass

    def mouseReleased(self, x, y):
        pass

    def mouseMotion(self, x, y):
        pass

    def mouseDrag(self, x, y):
        pass

    def keyPressed(self, keyCode, modifier, dt):
        pass

    def keyReleased(self, keyCode, modifier):
        pass

    def timerFired(self, dt):
        pass

    def redrawAll(self, screen):
        pass

    def isKeyPressed(self, key):
        ''' return whether a specific key is being held '''
        return self._keys.get(key, False)

    def __init__(self, width=1200, height=600, fps=50, title="Collegiate Combat"):
        
        self.width = width
        self.height = height
        self.fps = fps
        self.title = title
        pygame.mixer.init()
        pygame.init()
        
        # Upload background music
        CollegiateCombat.backgroundMusic = pygame.mixer.Sound("music/FightGameMusic.ogg")
        CollegiateCombat.kanyeSong = pygame.mixer.Sound("music/kanyesong.ogg")
        CollegiateCombat.kanyeGodSpeech = pygame.mixer.Sound("music/kanyegodspeech.ogg")
        CollegiateCombat.academicProbation = pygame.mixer.Sound("sounds/academicprobation.ogg")
        
        
        # Upload all character sounds
        characters = ["subzero", "scorpion", "raizen", "goku", "naruto", "sasuke"]
        characterInstances = ["jump", "block", "damage1", "punch", "kick", "special1", "effect1"]
        
        for i in range(len(characters)):
            
            path = "sounds/%s/ordered sound/" %characters[i]
            sounds = {}
            j = 0
            
            for soundName in os.listdir(path):
                
                sound = pygame.mixer.Sound(path + os.sep + soundName)
                
                sound.set_volume(1.0)
                
                sounds[characterInstances[j]] = sounds.get(characterInstances[j], sound)
                
                j += 1
                
            CollegiateCombat.characterSounds[characters[i]] = CollegiateCombat.characterSounds.get(characters[i], sounds)
    
    def playMusic():
        
        # Function sets the volume of the uploaded background music, and plays it
        if CollegiateCombat.mode == "RunGame":
        
            CollegiateCombat.isMusicPlaying = True
            CollegiateCombat.volume = 0.1
            CollegiateCombat.backgroundMusic.set_volume(CollegiateCombat.volume)
            CollegiateCombat.backgroundMusic.play()
        
        else:
            CollegiateCombat.kanyeSong.play(-1)
    
    def stopMusic():
        
        # Function stops all currently running sound used for 
        CollegiateCombat.isMusicPlaying = False
        pygame.mixer.stop()

    def run(self):

        clock = pygame.time.Clock()
        screen = pygame.display.set_mode((self.width, self.height))
        
        # Set the title of the window
        pygame.display.set_caption(self.title)

        # Stores all the keys currently being held down
        self._keys = dict()

        # Call game-specific initialization
        self.init()
        playing = True
            
        while playing:
            
            # Get the number of times the run functions runs per second
            self.time = clock.tick(self.fps)
            
            # Run the timer fired and pass in the number of times the run function runs per second
            self.timerFired(self.time)
            
            # Obtain external event information
            for event in pygame.event.get():
                
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    self.mousePressed(*(event.pos))
                elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    self.mouseReleased(*(event.pos))
                elif (event.type == pygame.MOUSEMOTION and event.buttons == (0, 0, 0)):
                    self.mouseMotion(*(event.pos))
                elif (event.type == pygame.MOUSEMOTION and event.buttons[0] == 1):
                    self.mouseDrag(*(event.pos))
                elif event.type == pygame.KEYDOWN:
                    self._keys[event.key] = True
                    self.keyPressed(event.key, event.mod, self.time)
                elif event.type == pygame.KEYUP:
                    self._keys[event.key] = False
                    self.keyReleased(event.key, event.mod)
                elif event.type == pygame.QUIT:
                    playing = False
            
            screen.fill(CollegiateCombat.black)
            
            self.redrawAll(screen)
            
            pygame.display.flip()
            
        pygame.quit()


def main():
    game = CollegiateCombat()
    game.run()

if __name__ == '__main__':
    main()
import pygame
from gtts import gTTS 
import os
from pathlib import Path
import time

  
# import Os module to start the audio file

pygame.init()
pygame.mixer.init() # add this line
  
goRight = 'Go Right'
goLeft = 'Go Left'
goForward = 'Go Forward'

goBack = 'Go Back'

goDescend = "Descend"

  
# Language we want to use 
language = 'en'
  

# right = gTTS(text=goRight, lang=language, slow=False) 
# left = gTTS(text=goLeft, lang=language, slow=False) 
# forward = gTTS(text=goForward, lang=language, slow=False) 
# back = gTTS(text=goBack, lang=language, slow=False) 
# descend = gTTS(text=goDescend, lang=language, slow=False) 

# right.save("right.mp3")
# left.save("left.mp3")
# forward.save("forward.mp3")
# back.save("back.mp3")
# descend.save("descend.mp3")



  

# sound = pygame.mixer.Sound("output.wav")

pygame.mixer.music.load("sounds/descend.mp3")
pygame.mixer.music.play()

time.sleep(3)
# myobj.save("output.wav") 
  
# Play the converted file 

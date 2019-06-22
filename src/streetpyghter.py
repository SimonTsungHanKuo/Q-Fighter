import pygame, os
import config
import menu
#import gym
from game import Point

if __name__ == "__main__":
    print('loading...')
    options = config.OptionConfig()
    
    #gym.make('gym_qfighter:qfighter-v0')
    pygame.init()
    pygame.mixer.init()
    config.Screen()
    
    screen = pygame.Surface((320, 240), 0, 32)

    menu = menu.MainMenu(screen, Point(50,140))
    menu.mainloop()
    

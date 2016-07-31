import pygame
import tools

import config as c



class AttractMode(tools.ModeBase):

    def __init__(self):
        tools.ModeBase.__init__(self)


    def ProcessInput(self, events, pressed_keys):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                # Move to the next mode when the user pressed Enter
                self.SwitchToMode(c.GAME_MODE)


    def Render(self, screen):
        screen.fill((255, 0, 0))

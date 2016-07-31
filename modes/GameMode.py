import pygame
import tools

import config as c



class GameMode(tools.ModeBase):

    def __init__(self):
        tools.ModeBase.__init__(self)

        self.is_blue = True

        self.leftBarPosition  = 260
        self.rightBarPosition = 260

        self.limitLeftUp    = False
        self.limitLeftDown  = False
        self.limitRightUp   = False
        self.limitRightDown = False


    def ProcessInput(self, events, pressed_keys):

        for event in events:

            # If button is being pressed...
            if event.type == pygame.KEYDOWN:

                # Move to the next mode when the user pressed Enter
                if event.key == pygame.K_RETURN:
                    self.SwitchToMode(c.GAME_OVER_MODE)

                # Limit switches activation
                elif event.key == c.LEFT_LIMIT_TOP:
                    self.limitLeftUp = True
                elif event.key == c.LEFT_LIMIT_BOTTOM:
                    self.limitLeftDown = True
                elif event.key == c.RIGHT_LIMIT_TOP:
                    self.limitRightUp = True
                elif event.key == c.RIGHT_LIMIT_BOTTOM:
                    self.limitRightDown = True

            # If button is being released...
            elif event.type == pygame.KEYUP:

                if event.key == c.LEFT_LIMIT_TOP:
                    self.limitLeftUp = False
                elif event.key == c.LEFT_LIMIT_BOTTOM:
                    self.limitLeftDown = False
                elif event.key == c.RIGHT_LIMIT_TOP:
                    self.limitRightUp = False
                elif event.key == c.RIGHT_LIMIT_BOTTOM:
                    self.limitRightDown = False

        pressed = pygame.key.get_pressed()
        if pressed[c.LEFT_JOY_UP]    and not self.limitLeftUp:    self.leftBarPosition  -= 3
        if pressed[c.LEFT_JOY_DOWN]  and not self.limitLeftDown:  self.leftBarPosition  += 3
        if pressed[c.RIGHT_JOY_UP]   and not self.limitRightUp:   self.rightBarPosition -= 3
        if pressed[c.RIGHT_JOY_DOWN] and not self.limitRightDown: self.rightBarPosition += 3

        if self.is_blue: self.color = (0, 128, 255)
        else: self.color = (255, 100, 0)


    def Render(self, screen):
        #screen.fill((0, 0, 255))

        left_block_color  = (0, 128, 255)
        right_block_color = (0, 128, 255)

        if self.limitLeftUp  or self.limitLeftDown:  left_block_color  = (255, 100, 0)
        if self.limitRightUp or self.limitRightDown: right_block_color = (255, 100, 0)

        screen.fill((0, 0, 0))

        pygame.draw.rect(screen, left_block_color,  pygame.Rect(30,  self.leftBarPosition,  60, 60))
        pygame.draw.rect(screen, right_block_color, pygame.Rect(300, self.rightBarPosition, 60, 60))

        # Temporary; adds a line for the bar
        pygame.draw.line(screen, (200, 200, 200), (90, self.leftBarPosition + 30), (300, self.rightBarPosition + 30), 10)

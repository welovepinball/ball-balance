import pygame
import tools

import config as c



class GameMode(tools.ModeBase):

    def __init__(self):
        """ Override tools.ModeBase's __init__(). """

        # Call tools.ModeBase's __init__()
        tools.ModeBase.__init__(self)

        # Set limit switch watchers' default states to False
        self.limitLeftUp    = False
        self.limitLeftDown  = False
        self.limitRightUp   = False
        self.limitRightDown = False

        # TEMPORARY: these are for the proof-of-concept graphics
        self.leftBarPosition  = 260
        self.rightBarPosition = 260


    def ProcessInput(self, events, pressed_keys):
        """Process the filtered list of events. """

        for event in events:

            # If button is being pressed...
            if event.type == pygame.KEYDOWN:

                # Move to the next mode when the user presses the Start button
                if event.key == c.START_BUTTON:
                    self.SwitchToMode(c.GAME_OVER_MODE)
                elif event.key == c.SERVICE_BUTTON:
                    # Move to the Service Menu when the user presses the Service button
                    self.SwitchToMode(c.SERVICE_MENU_MODE)

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

                # Limit switch deactivation
                if event.key == c.LEFT_LIMIT_TOP:
                    self.limitLeftUp = False
                elif event.key == c.LEFT_LIMIT_BOTTOM:
                    self.limitLeftDown = False
                elif event.key == c.RIGHT_LIMIT_TOP:
                    self.limitRightUp = False
                elif event.key == c.RIGHT_LIMIT_BOTTOM:
                    self.limitRightDown = False

        pressed = pygame.key.get_pressed()

        # If a joystick is moved, move the carriage if a limit switch not active
        if pressed[c.LEFT_JOY_UP]    and not self.limitLeftUp:    self.leftBarPosition  -= 3
        if pressed[c.LEFT_JOY_DOWN]  and not self.limitLeftDown:  self.leftBarPosition  += 3
        if pressed[c.RIGHT_JOY_UP]   and not self.limitRightUp:   self.rightBarPosition -= 3
        if pressed[c.RIGHT_JOY_DOWN] and not self.limitRightDown: self.rightBarPosition += 3


    def Render(self, screen):
        """Render output.

        This whole section is showing temporary, proof-of-concept graphics to
        demonstrate the carriage functionality and will be removed.
        """

        # Set the left and right carriages to blue
        left_block_color  = (0, 128, 255)
        right_block_color = (0, 128, 255)

        # If a limit switch is active on either side, change its carriage to orange
        if self.limitLeftUp  or self.limitLeftDown:  left_block_color  = (255, 100, 0)
        if self.limitRightUp or self.limitRightDown: right_block_color = (255, 100, 0)

        # Fill the screen with black to redraw the graphics
        screen.fill((0, 0, 0))

        # Draw the carriages to the screen
        pygame.draw.rect(screen, left_block_color,  pygame.Rect(30,  self.leftBarPosition,  60, 60))
        pygame.draw.rect(screen, right_block_color, pygame.Rect(300, self.rightBarPosition, 60, 60))

        # Add a line for the bar between the carriage blocks
        pygame.draw.line(screen, (200, 200, 200), (90, self.leftBarPosition + 30), (300, self.rightBarPosition + 30), 10)

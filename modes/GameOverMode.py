import pygame
import tools

import config as c



class GameOverMode(tools.ModeBase):
    """Serves as the game over mode for the game. Placeholder for now. """

    def ProcessInput(self, events, pressed_keys):
        """Process the filtered list of events. """

        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == c.START_BUTTON:
                    # Move to the next mode when the user presses the Start button
                    self.SwitchToMode(c.ATTRACT_MODE)
                elif event.key == c.SERVICE_BUTTON:
                    # Move to the Service Menu when the user presses the Service button
                    self.SwitchToMode(c.SERVICE_MENU_MODE)


    def Render(self, screen):
        """Render output. """

        # Just fill the screen with all green
        screen.fill((0, 255, 0))

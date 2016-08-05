import pygame

import tools

import rod as r

import config as c

from modes import AttractMode, GameMode, ServiceMenuMode



# --------------------------------------------------------------------
# Main loop
# --------------------------------------------------------------------

def main():
    """Main loop that runs the game. """

    # Reduce the audio sample rate to limit CPU burden
    # (Must be done before pygame.init()! )
    pygame.mixer.pre_init(44100, -16, 2, 1024)

    # Initialize all modules required for PyGame
    pygame.init()

    # Launch window of desired size
    screen = pygame.display.set_mode([c.SCREEN_WIDTH, c.SCREEN_HEIGHT])

    # Set game window title
    pygame.display.set_caption('Ball balance game')

    # Hide the mouse cursor
    pygame.mouse.set_visible(False)

    # Create a clock to track time to limit game maximum FPS
    clock = pygame.time.Clock()
    rod = r.Rod()


    # Add new game modes here
    c.ATTRACT_MODE = AttractMode.AttractMode(rod)
    c.GAME_MODE = GameMode.GameMode(rod)
    c.SERVICE_MENU_MODE = ServiceMenuMode.ServiceMenuMode(rod);


    active_mode = c.ATTRACT_MODE



    while active_mode != None:

        # Reset active mode to self so that it doesn't immediately flip to the
        # next mode
        active_mode.refresh(rod)


        pressed_keys = pygame.key.get_pressed()


        # Clear out the event queue into 'events'
        events = pygame.event.get()

        for event in events:

            # If user clicks the window close button...
            if event.type == pygame.QUIT:
                active_mode = None

            # If a button is pressed down...
            elif event.type == pygame.KEYDOWN:

                # Set to True if either Alt button is pressed
                alt_pressed = pressed_keys[pygame.K_LALT] or \
                          pressed_keys[pygame.K_RALT]

                # If Escape key is pressed...
                if event.key == pygame.K_ESCAPE:
                    active_mode = None

                # If Alt + F4 is pressed...
                elif event.key == pygame.K_F4 and alt_pressed:
                    active_mode = None

                # Limit switches activation
                elif event.key == c.LEFT_LIMIT_TOP:
                    rod.limit_left_up = True
                elif event.key == c.LEFT_LIMIT_BOTTOM:
                    rod.limit_left_down = True
                elif event.key == c.RIGHT_LIMIT_TOP:
                    rod.limit_right_up = True
                elif event.key == c.RIGHT_LIMIT_BOTTOM:
                    rod.limit_right_down = True

                # If Service Mode button is pressed...
                elif event.key == c.SERVICE_BUTTON:
                    active_mode.switch_to_mode(c.SERVICE_MENU_MODE)


            # If button is being released...
            elif event.type == pygame.KEYUP:

                # Limit switches deactivation
                if event.key == c.LEFT_LIMIT_TOP:
                    rod.limit_left_up = False
                elif event.key == c.LEFT_LIMIT_BOTTOM:
                    rod.limit_left_down = False
                elif event.key == c.RIGHT_LIMIT_TOP:
                    rod.limit_right_up = False
                elif event.key == c.RIGHT_LIMIT_BOTTOM:
                    rod.limit_right_down = False


        # Send the events list to the active mode's process()
        active_mode.process(events, pressed_keys)

        # Use the active mode's render()
        active_mode.render(screen)

        # Change the active mode to the current active mode's next assigned
        active_mode = active_mode.next

        # Swap PyGame's buffers to update the graphics on the screen
        pygame.display.flip()

        # Delay the game to limit refresh rate to 60 FPS
        clock.tick(60)


    # Quit the game cleanly
    pygame.quit()



# --------------------------------------------------------------------



if __name__ == "__main__":
    main()

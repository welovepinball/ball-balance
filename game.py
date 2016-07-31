import pygame

import config as c

from modes import AttractMode, GameMode, GameOverMode, ServiceMenuMode



# Add new game modes here
c.ATTRACT_MODE = AttractMode.AttractMode()
c.GAME_MODE = GameMode.GameMode()
c.GAME_OVER_MODE = GameOverMode.GameOverMode();
c.SERVICE_MENU_MODE = ServiceMenuMode.ServiceMenuMode();



def run_game(width, height, fps, starting_mode):
    """Main loop that runs the game.

    Args:
        width (int):  Pixel dimension of the screen size
        height (int): Pixel dimension of the screen size
        fps (int):    framerate limit (frames per second)
        starting_mode (str): Mode to begin the game in

    """

    # Reduce the audio sample rate to limit CPU burden
    # (Must be done before pygame.init()! )
    pygame.mixer.pre_init(44100,-16,2, 1024)

    # Initialize all modules required for PyGame
    pygame.init()

    # Launch window of desired size
    screen = pygame.display.set_mode((width, height))

    # Create a clock to track time to limit game maximum FPS
    clock = pygame.time.Clock()

    # Set the active mode to the given mode in the called arguments
    active_mode = starting_mode


    while active_mode != None:

        # Reset active mode to self so that it doesn't immediately flip to the
        # next mode
        active_mode.Refresh()


        pressed_keys = pygame.key.get_pressed()

        # Event filtering: run_game gets first pass at the keypresses and
        # other events before the modes can do what they will with the rest
        filtered_events = []

        # For each event in the event queue...
        for event in pygame.event.get():

            # Variable to track user's quit attempt
            quit_attempt = False

            # If user clicks the window close button...
            if event.type == pygame.QUIT:
                quit_attempt = True

            # If a button is pressed...
            elif event.type == pygame.KEYDOWN:

                # Set to True if either Alt button is pressed
                alt_pressed = pressed_keys[pygame.K_LALT] or \
                              pressed_keys[pygame.K_RALT]

                # If Escape key is pressed...
                if event.key == pygame.K_ESCAPE:
                    quit_attempt = True

                # If Alt + F4 is pressed...
                elif event.key == pygame.K_F4 and alt_pressed:
                    quit_attempt = True

                # If Service Mode button is pressed...
                if event.key == c.SERVICE_BUTTON:
                    active_mode.SwitchToMode(c.SERVICE_MENU_MODE)

            # If the event triggered a quit attempt...
            if quit_attempt:

                # Use active mode's Terminate sequence
                active_mode.Terminate()
            else:

                # Add the event to the filtered list of events for the mode
                filtered_events.append(event)


        # Send the filtered list of events to the active mode's ProcessInput
        active_mode.ProcessInput(filtered_events, pressed_keys)

        # Use the active mode's Render sequence
        active_mode.Render(screen)

        # Change the active mode to the current active mode's next assigned
        active_mode = active_mode.next

        # Swap PyGame's buffers to update the graphics on the screen
        pygame.display.flip()

        # Delay the game to limit refresh rate to FPS
        clock.tick(fps)


# Run the game, in a 400x300 window, at 60fps, starting in the attract mode
run_game(400, 300, 60, c.ATTRACT_MODE)

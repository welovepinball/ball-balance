import pygame

import config as c

from modes import AttractMode, GameMode, GameOverMode



c.ATTRACT_MODE = AttractMode.AttractMode()
c.GAME_MODE = GameMode.GameMode()
c.GAME_OVER_MODE = GameOverMode.GameOverMode();



def run_game(width, height, fps, starting_mode):

    # Initialize all modules required for PyGame
    pygame.init()

    # Launch window of desired size
    screen = pygame.display.set_mode((width, height))

    # Create a clock to track time to limit game maximum FPS
    clock = pygame.time.Clock()

    active_mode = starting_mode

    while active_mode != None:

        active_mode.Refresh()

        pressed_keys = pygame.key.get_pressed()

        # Event filtering: run_game gets first pass at the keypresses and
        # other events before the modes can do what they will with them
        filtered_events = []

        for event in pygame.event.get():
            quit_attempt = False
            if event.type == pygame.QUIT:
                quit_attempt = True
            elif event.type == pygame.KEYDOWN:
                alt_pressed = pressed_keys[pygame.K_LALT] or \
                              pressed_keys[pygame.K_RALT]
                if event.key == pygame.K_ESCAPE:
                    quit_attempt = True
                elif event.key == pygame.K_F4 and alt_pressed:
                    quit_attempt = True

            if quit_attempt:
                active_mode.Terminate()
            else:
                filtered_events.append(event)

        active_mode.ProcessInput(filtered_events, pressed_keys)
        active_mode.Render(screen)

        active_mode = active_mode.next

        pygame.display.flip()

        # Delay the game to limit refresh rate to FPS
        clock.tick(fps)



run_game(400, 300, 60, c.ATTRACT_MODE)

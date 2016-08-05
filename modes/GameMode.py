import pygame

import tools

import rod

import config as c



# --------------------------------------------------------------------
# Custom Events and Timers
# --------------------------------------------------------------------

GENERIC_TIMER       = pygame.USEREVENT + 1
BONUS_REDUCE_TIMER  = pygame.USEREVENT + 2
INCREMENT_ROD_TIMER = pygame.USEREVENT + 3



class GameMode(tools.ModeBase):

    def __init__(self, rod):

        self.rod = rod
        self.reset_settings()



    def reset_settings(self):
        self.score = 0
        self.current_bonus = 0

        self.balls_left = 3
        self.star_lit = False

        self.extra_ball_earned = False

        self.current_hole = 1

        self.state = 'starting round'
        self.state_just_changed = True

        self.succeeded_hole = False

        self.skip_music = False



    def process(self, events, pressed_keys):

        if self.state == 'starting round' and self.state_just_changed:
            self.state_just_changed = False

            print('Starting round')

            if not self.balls_left:
                self.state = 'game over'
                self.state_just_changed = True

            if self.current_hole > 10:
                self.state = 'win'
                self.state_just_changed = True

            self.current_bonus = self.current_hole * 100

            if not self.skip_music:
                tools.play_song(c.AUDIO_THEME)

            self.rod.allowed_to_move = False


        elif self.state == 'starting round':
            self.rod.move(-1, -1)


        elif self.state == 'ball on rod' and self.state_just_changed:
            self.state_just_changed = False

            print('Ball loaded onto rod')

            pygame.time.delay(500)
            pygame.time.set_timer(GENERIC_TIMER, 1000)


        elif self.state == 'ball on rod':
            self.rod.move(1, 1)


        elif self.state == 'ball at origin' and self.state_just_changed:
            self.state_just_changed = False

            print('Ball at origin point')

            self.rod.allowed_to_move = True

            pygame.time.set_timer(BONUS_REDUCE_TIMER, 4000)
            pygame.time.set_timer(INCREMENT_ROD_TIMER, 4000)

            self.state = 'game in progress'
            self.state_just_changed = True


        elif self.state == 'game in progress' and self.state_just_changed:
            self.state_just_changed = False

            print('Game is in progress')


        elif self.state == 'end level' and self.state_just_changed:
            self.state_just_changed = False

            print('Level has ended')

            self.rod.allowed_to_move = False

            pygame.mixer.music.stop()

            pygame.time.set_timer(BONUS_REDUCE_TIMER, 0)
            pygame.time.set_timer(INCREMENT_ROD_TIMER, 0)

            if self.succeeded_hole:
                self.state = 'hole success'
            else:
                self.state = 'hole failure'


        elif self.state == 'hole success':

            print('Player was successful')

            pygame.mixer.music.load(c.AUDIO_SUCCESS)
            pygame.mixer.music.play(0)

            pygame.time.delay(2000)

            self.current_hole += 1

            self.state = 'count down bonus'


        elif self.state == 'count down bonus' and self.state_just_changed:
            self.state_just_changed = False
            self.extra_is_fresh = True


        elif self.state == 'count down bonus':
            if self.current_bonus > 0:
                self.current_bonus -= 10
                self.score        += 10
                tools.play_sound(c.AUDIO_BONUS)
                pygame.time.delay(150)
            else:
                pygame.time.delay(500)

                self.state = 'starting round'
                self.state_just_changed = True

            if self.score >= 4000 and not self.extra_ball_earned:
                self.extra_ball_earned = True

                print('Extra ball earned')

                pygame.mixer.music.load(c.AUDIO_EXTRA_BALL)
                pygame.mixer.music.play(0)

                self.balls_left += 1
                self.skip_music = True


        elif self.state == 'hole failure':

            print('Player failed')

            pygame.mixer.music.load(c.AUDIO_FAILURE)
            pygame.mixer.music.play(0)

            pygame.time.delay(2500)

            self.balls_left -= 1

            self.state = 'starting round'
            self.state_just_changed = True


        elif self.state == 'game over' and self.state_just_changed:
            self.state_just_changed = False

            print('Game over')

            self.rod.allowed_to_move = False

            pygame.time.set_timer(BONUS_REDUCE_TIMER, 0)
            pygame.time.set_timer(INCREMENT_ROD_TIMER, 0)

            pygame.mixer.music.stop()
            pygame.mixer.music.load(c.AUDIO_GAMEOVER)
            pygame.mixer.music.play(0)

            pygame.time.delay(10500)

            self.reset_settings()

            self.switch_to_mode(c.ATTRACT_MODE)


        elif self.state == 'win' and self.state_just_changed:
            self.state_just_changed = False

            print('Player won')

            self.rod.allowed_to_move = False

            pygame.time.set_timer(BONUS_REDUCE_TIMER, 0)
            pygame.time.set_timer(INCREMENT_ROD_TIMER, 0)

            pygame.mixer.music.stop()
            pygame.mixer.music.load(c.AUDIO_WIN)
            pygame.mixer.music.play(0)

            self.star_lit = True

            pygame.time.delay(9500)


        # ------------------------------------------------------------


        for event in events:

            # If a button is pressed down...
            if event.type == pygame.KEYDOWN:
                if event.key == c.HOLES_SWITCHES[self.current_hole]:
                    self.state = 'hole success'
                    self.state_just_changed = True


            # If button is being released...
            elif event.type == pygame.KEYUP:
                if event.key == c.HOLE_FAILURE_SWITCH:
                    if self.state == 'starting round':
                        self.state = 'ball on rod'
                        self.state_just_changed = True
                    elif self.state == 'game in progress':
                        self.state = 'end level'
                        self.state_just_changed = True


            elif event.type == BONUS_REDUCE_TIMER:
                if self.state == 'game in progress':
                    pygame.time.set_timer(BONUS_REDUCE_TIMER, 4000)
                    tools.play_sound(c.AUDIO_TICK)

                    if self.current_bonus > 0:
                        self.current_bonus -= 10


            elif event.type == INCREMENT_ROD_TIMER:
                if self.state == 'game in progress':
                    pygame.time.set_timer(INCREMENT_ROD_TIMER, 4000)
                    self.rod.move(1, 1)


            elif event.type == GENERIC_TIMER and self.state == 'ball on rod':
                pygame.time.set_timer(GENERIC_TIMER, 0)
                self.state = 'ball at origin'
                self.state_just_changed = True


        # ------------------------------------------------------------


        self.rod.activate_joysticks(pressed_keys)



    def render(self, screen):

        # Fill the screen with black to redraw the graphics
        screen.fill((0, 0, 0))

        font = pygame.font.Font(None, 36)

        # Score UI
        rendered_score = font.render('Score: ' + str(self.score), 1, (255, 127, 127))
        screen.blit(rendered_score, (150, 20))

        # Bonus UI
        rendered_bonus = font.render('Bonus: ' + str(self.current_bonus), 1, (0, 255, 0))
        screen.blit(rendered_bonus, (150, 60))

        # Balls left UI
        rendered_lives = font.render('Balls left: ' + str(self.balls_left), 1, (0, 255, 255))
        screen.blit(rendered_lives, (150, 100))

        # Generate the carriage and rod graphics
        self.rod.generate_graphics(screen)

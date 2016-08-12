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



class RodTestMode(tools.ModeBase):

    def __init__(self, rod):
        

        self.rod = rod
        self.rod.allowed_to_move = True
        #self.reset_settings()



##    def reset_settings(self):
##        self.score = 0
##        self.current_bonus = 0
##
##        self.balls_left = 3
##        self.star_lit = False
##
##        self.extra_ball_earned = False
##
##        self.current_hole = 1
##
##        self.state = 'starting round'
##        self.state_just_changed = True
##
##        self.succeeded_hole = False
##
##        self.skip_music = False



    def process(self, events, pressed_keys):
        # ------------------------------------------------------------


##        for event in events:

##            # If a button is pressed down...
##            if event.type == pygame.KEYDOWN:
##                if event.key == c.HOLES_SWITCHES[self.current_hole]:
##                    self.state = 'hole success'
##                    self.state_just_changed = True
##                elif event.key == c.HOLE_FAILURE_SWITCH:
##                    if self.state == 'game in progress':
##                        self.state = 'end level'
##                        self.state_just_changed = True
##
##
##            # If button is being released...
##            elif event.type == pygame.KEYUP:
##                if event.key == c.HOLE_FAILURE_SWITCH:
##                    if self.state == 'starting round':
##                        self.state = 'ball on rod'
##                        self.state_just_changed = True
##
##
##            elif event.type == BONUS_REDUCE_TIMER:
##                if self.state == 'game in progress':
##                    pygame.time.set_timer(BONUS_REDUCE_TIMER, 4000)
##                    tools.play_sound(c.AUDIO_TICK)
##
##                    if self.current_bonus > 0:
##                        self.current_bonus -= 10
##
##
##            elif event.type == INCREMENT_ROD_TIMER:
##                if self.state == 'game in progress':
##                    pygame.time.set_timer(INCREMENT_ROD_TIMER, 4000)
##                    self.rod.move(1, 1)
##
##
##            elif event.type == GENERIC_TIMER and self.state == 'ball on rod':
##                pygame.time.set_timer(GENERIC_TIMER, 0)
##                self.state = 'ball at origin'
##                self.state_just_changed = True


        # ------------------------------------------------------------
        self.rod.activate_joysticks(pressed_keys)



    def render(self, screen):

        # Fill the screen with black to redraw the graphics
        screen.fill((0, 0, 0))

        font = pygame.font.Font(None, 36)

##        # Score UI
##        rendered_score = font.render('Score: ' + str(self.score), 1, (255, 127, 127))
##        screen.blit(rendered_score, (150, 20))
##
##        # Bonus UI
##        rendered_bonus = font.render('Bonus: ' + str(self.current_bonus), 1, (0, 255, 0))
##        screen.blit(rendered_bonus, (150, 60))
##
##        # Balls left UI
##        rendered_lives = font.render('Balls left: ' + str(self.balls_left), 1, (0, 255, 255))
##        screen.blit(rendered_lives, (150, 100))

        # Generate the carriage and rod graphics
        self.rod.generate_graphics(screen)

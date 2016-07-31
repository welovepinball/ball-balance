class ModeBase:
    """Modes will inherit from this class. """

    def __init__(self):
        self.Refresh()


    def Refresh(self):
        """Set the mode's next property to self.

        If the program has already been in this mode before and switched to a
        different one, self.next will still be set to that last location, so
        run_game() will switch the mode back to that one if not for calling this
        method before that happens.

        """
        self.next = self


    def ProcessInput(self, events, pressed_keys):
        """Process the filtered list of events.

        Subclasses should override this method or else they get a warning.

        """
        print("You need to override ProcessInput() in the child class!")


    def Render(self, screen):
        """Render output, to screen and otherwise.

        Subclasses should override this method or else they get a warning.

        """
        print("You need to override Render() in the child class!")


    def SwitchToMode(self, next_mode):
        """Set mode's next property to the given mode."""

        self.next = next_mode


    def Terminate(self):
        """ End the game.

        In run_game(), when active_mode is set to None, the while loop will
        terminate the application

        """

        self.SwitchToMode(None)

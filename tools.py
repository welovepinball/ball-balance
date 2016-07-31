# Modes will inherit from this class
class ModeBase:

    def __init__(self):
        self.next = self


    def Refresh(self):
        self.next = self


    def ProcessInput(self, events, pressed_keys):
        print("You need to override ProcessInput() in the child class!")


    def Render(self, screen):
        print("You need to override Render() in the child class!")


    def SwitchToMode(self, next_mode):
        self.next = next_mode


    def Terminate(self):
        # In run_game(), when active_mode is set to None, the while loop will
        # terminate the application
        self.SwitchToMode(None)

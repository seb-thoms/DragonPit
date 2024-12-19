from game.game_env import DragonPitEnv
from gui.gui import PyGameGUI

class DragonPitGame:
    def __init__(self, screen_height:int = 600, screen_width:int =800):
        """
        Constructor for the game.

        Args:
            screen_height (int, optional): Height of the screen. Defaults to 600.
            screen_width (int, optional): Width of the screen. Defaults to 800.
        """
        self.width = screen_width
        self.height = screen_height

        self.gui = PyGameGUI(self.width, self.height)
        self.env = DragonPitEnv(self.height)
    
    def run_game(self):
        """
        Runs the game.
        """

        try:
            observation, rewards, done, info = self.env.reset()
            self.gui.render(self.env.get_state())
            while not done:
                action = (0, 1)

                observation, rewards, done, info = self.env.step(action)

                self.gui.render(self.env.get_state())
        
        except KeyboardInterrupt:
            pass

        finally:
            self.gui.close()


if __name__ == "__main__":
    game = DragonPitGame()
    game.run_game()
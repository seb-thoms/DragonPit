import pygame

class PyGameGUI:
    def __init__(self, screen_width: int, screen_height: int):
        """
        Constructor for the pygame GUI.

        Args:
            screen_width (int): Width of the pygame window.
            screen_height (int): Height of the pygame window.
        """
        self.width = screen_width
        self.height = screen_height
        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("DragonPit")
        self.clock = pygame.time.Clock()
    

    def render(self, state: dict):
        """
        Renders the state of the environment in the GUI.

        Args:
            state (dict): {
                            "dragon1" : <Position of dragon 1>,
                            "dragon2" : <Position of dragon 2>,
                            "dragon1_health" : <Health of dragon 1>,
                            "dragon2_health" : <Health of dragon 2>,
                          }
        """
        BLACK = (0, 0, 0)
        RED = (255, 0, 0)
        GREEN = (0, 255, 0)
        WHITE = (255, 255, 255)

        self.screen.fill(BLACK)

        dragon_width, dragon_height = 20, 60

        pygame.draw.rect(self.screen, RED, (50, state["dragon1"], dragon_width, dragon_height))  # Dragon 1
        pygame.draw.rect(self.screen, GREEN, (self.width - 70, state["dragon2"], dragon_width, dragon_height))  # Dragon 2

        pygame.draw.rect(self.screen, WHITE, (50, 10, 200, 20))  # Background bar for Dragon 1
        pygame.draw.rect(self.screen, WHITE, (self.width - 250, 10, 200, 20))  # Background bar for Dragon 2

        pygame.draw.rect(self.screen, RED, (50, 10, 2 * state["dragon1_health"], 20))  # Dragon 1 Health Bar
        pygame.draw.rect(self.screen, GREEN, (self.width - 250, 10, 2 * state["dragon2_health"], 20))  # Dragon 2 Health Bar
        
        pygame.display.flip()
        self.clock.tick(30)
    
    def close(self):
        pygame.quit()


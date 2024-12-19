import gym
from gym import spaces
import numpy as np
from actions import Actions

class DragonPitGame(gym.Env):
    """Main game environment for the dragon pit game."""
    
    def __init__(self, screen_height: int):
        """
        Constructor for the game environment.

        Args:
            screen_height (int): Height of the GUI display
        """
        super(DragonPitGame, self).__init__()

        self.height = screen_height

        self.action_space = spaces.MultiDiscrete([len(Actions), len(Actions)])

        # Define observation space here.
        self.observation_space = spaces.Box(low=np.array(0, 0, 0, 0),
                                            high=np.array(self.height, self.height, 100, 100),
                                            dtype=np.int32)
        
        # Initial positions and health.
        self.dragon1 = self.height // 2
        self.dragon2 = self.height // 2
        self.dragon1_health = 100
        self.dragon2_health = 100

        # Controls how much a dragon will move.
        self.step_size = self.height // 10
        
        self.done = False
        self.state = None
    

    def reset(self):
        """
        Resets the environment.
        """
        self.done = False
        self.state = [0, 0, 100, 100]

    def step(self, action: tuple) -> tuple[list, tuple[float, float], bool, dict]:
        """
        Executes one step in the environment and returns the new observation, reward, done and info.

        Args:
            action (tuple): A tuple containing actions of each dragon. 
            eg: (0, 2) means dragon 1 moves down(0) and dragon 2 spits fire(2). 

        Returns:
            observation (list)  :   New observation from the environment.
            reward  (tuple)     :   Reward for the action. Both dragon has its own rewards.
            done    (bool)      :   Whether game has ended.
            info    (dict)      :   Debugging info (as mandated by Gym).
        """

        dragon1_action, dragon2_action = action
        dragon1_reward, dragon2_reward = 0.0, 0.0

        Actions.validate_action(dragon1_action)
        Actions.validate_action(dragon2_action)


        # Track dragon 1 action and update.
        if dragon1_action == Actions.UP.value:
            self.dragon1 = min(self.height, self.dragon1 + self.step_size)
        elif dragon1_action == Actions.DOWN.value:
            self.dragon1 = max(0, self.dragon1 - self.step_size)


        # Track dragon 2 action and update.
        if dragon2_action == Actions.UP.value:
            self.dragonw = min(self.height, self.dragon2 + self.step_size)
        elif dragon2_action == Actions.DOWN.value:
            self.dragon2 = max(0, self.dragon2 - self.step_size)

        
        # Spit fire logic. If hit, decrease health by 10. Give reward for succesful hit and penalize for getting hit.
        if dragon1_action == Actions.SPIT_FIRE.value:
            if self.dragon2 == self.dragon1: # successful hit
                self.dragon2_health -= 10
                dragon1_reward += 10
                dragon2_reward -= 5

        if dragon2_action == Actions.SPIT_FIRE.value:
            if self.dragon2 == self.dragon1: # successful hit
                self.dragon1_health -= 10
                dragon2_reward += 10
                dragon1_reward -= 5

            
        # Logic for game has ended or not. 100 for winning. -100 for losing as rewards.

        if self.dragon1_health <=0 or self.dragon2_health <=0:
            if self.dragon1_health <= 0:
                dragon1_reward -= 100
                dragon2_reward += 100
            if self.dragon2_health <=0:
                dragon2_reward -= 100
                dragon1_reward += 100



        # Construct new observation
        observation = [self.dragon1, self.dragon2, self.dragon1_health, self.dragon2_health]

        return observation, (dragon1_reward, dragon2_reward), self.done, {}

    def render(self, mode='human'):
        """
        Rendering logic.

        Args:
            mode (str, optional): Rendering mode. Defaults to 'human'.
        """
        pass

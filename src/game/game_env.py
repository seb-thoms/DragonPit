import gym
from gym import spaces
import numpy as np

class DragonPitGame(gym.Env):
    """Main game environment for the dragon pit game."""
    
    def __init__(self):
        super(DragonPitGame, self).__init__()

        # Define action space here.
        # 3 actions for each dragon.
        # 0 - move up
        # 1 - move down
        # 2 - spit fire
        self.action_space = spaces.MultiDiscrete([3, 3])

        # Define observation space here.
        self.observation_space = spaces.Box(low=np.array(0, 0, 0, 0),
                                            high=np.array(1, 1, 100, 100),
                                            dtype=np.int32)
    

    def reset(self):
        pass

    def step(self, action):
        pass

    def render(self):
        pass

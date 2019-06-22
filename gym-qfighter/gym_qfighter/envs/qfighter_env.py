import numpy as np
import gym
from gym import error, spaces, utils
from gym.utils import seeding

class QFighterEnv(gym.Env):
  metadata = {'render.modes': ['human']}
  move = 0

  def __init__(self):
      self.action_space = spaces.Discrete(17)
      #self.observation_space = spaces.Box(0, 3, dtype=int32)

  def step(self, state, action):
      #-----Q-Fighter by Simon, Yu-Yen, Henry:2019-06-12-----
      # state[0]: distance level
      # state[1]: health_loss 
      # action:   Not used yet

      reward = 0.0
      """
      if state[1] == 0: 
         reward = 0.0
      elif state[1] == 1 :  
         reward = 1.3
      elif state[1] == 2 :  
         reward = 1.5
      elif state[1] == 3 :  
         reward = 1.8
      elif state[1] == 4 :  
         reward = 2.0
      """
      if state[1] == 0: 
         reward = 0.0
      else:
         reward = 1.0

      return reward

  def reset(self):
    ...

  def render(self, mode='human'):
    ...

  def close(self):
    ...


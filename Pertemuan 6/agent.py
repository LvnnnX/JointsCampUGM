import pandas as np
import numpy as np
import torch, random
from collections import deque
from game import SnakeGame, Direction, Point

#TODO: from mode
MAX_MEMORY = 100_000
BATCH_SIZE = 1000
LR = 0.001

class Agent:

    def __init__(self):
        self.n_games = 0
        self.epsilon = 1
        self.gamma = 0.9
        self.memory = deque(maxlen=MAX_MEMORY)
        self.model = None #TODO
        self.trainder = None #TODO

    def get_state(self, game):
        head = game.snake[0]

        point_l = Point(head.x - 20, head.y)
        point_r = Point(head.x + 20, head.y)
        point_u = Point(head.x, head.y-20)
        point_d = Point(head.x, head.y + 20)

    def remember(self, state, action, reward, next_state, done):
        pass

    def train_long_memory(self):
        pass

    def train_short_memory(self, state):
        pass

    def get_action(self, state):
        pass

def train():
    pass
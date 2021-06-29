import os

MAX_X = 120
MAX_Y = 40
FRAME_LENGTH = 0.1
PATH = os.path.dirname(os.path.abspath(__file__))
MESSAGES = open(PATH + "/messages.txt").read().splitlines()
ARTIFACTS = 30

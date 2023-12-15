from maze import Maze
import random
import pygame
from constants import *
from exception import UndefinedOptionError

def rendSingleMovement(screen: pygame.Surface, currentPoint: (int, int), option: str):
    if option not in POSSIBLE_OPTIONS:
        UndefinedOptionError(f"find '{option}' in the record")

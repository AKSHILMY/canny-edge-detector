from enum import Enum
import numpy as np

class Constants(Enum):
    SOBEL_X = [[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]
    SOBEL_Y = [[-1, -2, -1], [0, 0, 0], [1, 2, 1]]

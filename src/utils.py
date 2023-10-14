import numpy as np

def rgb2gray(img) :
    return np.dot(img[..., :3], [0.2989, 0.5870, 0.1140])
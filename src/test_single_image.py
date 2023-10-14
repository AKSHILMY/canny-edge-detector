from canny_edge_detector import CannyEdgeDetector
import imageio
from utils import rgb2gray
from scipy import ndimage
import numpy as np
import argparse
import os

parser = argparse.ArgumentParser(description='Canny Edge Detector')
parser.add_argument('--input', type=str, help='path to input image file')
parser.add_argument('--output', type=str, help='path to output image file')
args = parser.parse_args()

c = CannyEdgeDetector(config_file_path="config.yaml")

read_image = imageio.imread(args.input)
gray_input_img = rgb2gray(read_image)
blur_img = ndimage.gaussian_filter(gray_input_img, sigma = 1.0)
x_grad,y_grad = c.get_gradients(image=gray_input_img)
grad_magnitude = c.get_gradient_magnitude(x_grad,y_grad)
grad_direction = c.get_gradient_direction(x_grad,y_grad)
closest_dir = c.closest_dir_function(grad_direction)
thinned_output = c.non_maximal_suppressor(grad_magnitude, closest_dir)
output_img = c.hysteresis_thresholding(thinned_output)
output_img.shape
your_array = (output_img * 255).astype(np.uint8)
imageio.imwrite(args.output, your_array)


import numpy as np
from scipy import ndimage
from constants import Constants
import yaml

class CannyEdgeDetector():
    def __init__(self,config_file_path) -> None:
        self.load_configuration(config_file_path)

    def convolve(self, image, kernel):
        """
        TODO: Implement convolution function to convolve
        """
        pass
    
    def load_configuration(self, config_file_path):
        with open(config_file_path, 'r') as f:
            self.config = yaml.safe_load(f)

    def get_gradients(self, image, kernel:str = 'sobel', direction :str = 'xy'):
        kernel = self.config['kernel'][kernel]
        if direction == 'xy':
            # TODO : Utilize the manually defined convolve function
            grad_x = ndimage.convolve(image,np.array(kernel['x']))
            grad_y = ndimage.convolve(image,np.array(kernel['y']))
            return grad_x/np.max(grad_x),grad_y/np.max(grad_y)
        elif direction == 'x':
            # TODO : Utilize the manually defined convolve function
            grad_x = ndimage.convolve(image,np.array(kernel['x']))
            return grad_x/np.max(grad_x)
        elif direction == 'y':
            # TODO : Utilize the manually defined convolve function
            grad_y = ndimage.convolve(image,np.array(kernel['y']))
            return grad_y/np.max(grad_y)
        else:
            raise Exception(f"Direction '{direction}' not found")
    
    def get_gradient_magnitude(self, grad_x, grad_y):
        grad_magnitude = np.hypot(grad_x, grad_y)
        return grad_magnitude/np.max(grad_magnitude)
    
    def get_gradient_direction(self, grad_x, grad_y):
        return np.degrees(np.arctan2(grad_y, grad_x))
    
    def closest_dir_function(self,grad_dir):
        kernel = np.array(self.config['direction']['kernel'])
        closest_dir_arr = ndimage.convolve(grad_dir, kernel, mode='constant', cval=0.0)
        return closest_dir_arr

    def non_maximal_suppressor(self,grad_mag, closest_dir) :
        thinned_output = np.zeros(grad_mag.shape)
        for i in range(1, int(grad_mag.shape[0] - 1)) :
            for j in range(1, int(grad_mag.shape[1] - 1)) :
                
                if(closest_dir[i, j] == 0) :
                    if((grad_mag[i, j] > grad_mag[i, j+1]) and (grad_mag[i, j] > grad_mag[i, j-1])) :
                        thinned_output[i, j] = grad_mag[i, j]
                    else :
                        thinned_output[i, j] = 0
                
                elif(closest_dir[i, j] == 45) :
                    if((grad_mag[i, j] > grad_mag[i+1, j+1]) and (grad_mag[i, j] > grad_mag[i-1, j-1])) :
                        thinned_output[i, j] = grad_mag[i, j]
                    else :
                        thinned_output[i, j] = 0
                
                elif(closest_dir[i, j] == 90) :
                    if((grad_mag[i, j] > grad_mag[i+1, j]) and (grad_mag[i, j] > grad_mag[i-1, j])) :
                        thinned_output[i, j] = grad_mag[i, j]
                    else :
                        thinned_output[i, j] = 0
                
                else :
                    if((grad_mag[i, j] > grad_mag[i+1, j-1]) and (grad_mag[i, j] > grad_mag[i-1, j+1])) :
                        thinned_output[i, j] = grad_mag[i, j]
                    else :
                        thinned_output[i, j] = 0
                
        return thinned_output/np.max(thinned_output)   
         
    def DFS(self,img) :
        for i in range(1, int(img.shape[0] - 1)) :
            for j in range(1, int(img.shape[1] - 1)) :
                if(img[i, j] == 1) :
                    t_max = max(img[i-1, j-1], img[i-1, j], img[i-1, j+1], img[i, j-1],
                                img[i, j+1], img[i+1, j-1], img[i+1, j], img[i+1, j+1])
                    if(t_max == 2) :
                        img[i, j] = 2
                
                        
    def hysteresis_thresholding(self,img) :
        low_ratio = self.config['hysteresis']['low_threshold']
        high_ratio = self.config['hysteresis']['high_threshold']
        diff = np.max(img) - np.min(img)
        t_low = np.min(img) + low_ratio * diff
        t_high = np.min(img) + high_ratio * diff
        
        temp_img = np.copy(img)
        
        #Assign values to pixels
        for i in range(1, int(img.shape[0] - 1)) :
            for j in range(1, int(img.shape[1] - 1)) :
                #Strong pixels
                if(img[i, j] > t_high) :
                    temp_img[i, j] = 2
                #Weak pixels
                elif(img[i, j] < t_low) :
                    temp_img[i, j] = 0
                #Intermediate pixels
                else :
                    temp_img[i, j] = 1
        
        #Include weak pixels that are connected to chain of strong pixels 
        total_strong = np.sum(temp_img == 2)
        while(1) :
            self.DFS(temp_img)
            if(total_strong == np.sum(temp_img == 2)) :
                break
            total_strong = np.sum(temp_img == 2)
        
        #Remove weak pixels
        for i in range(1, int(temp_img.shape[0] - 1)) :
            for j in range(1, int(temp_img.shape[1] - 1)) :
                if(temp_img[i, j] == 1) :
                    temp_img[i, j] = 0
        
        temp_img = temp_img/np.max(temp_img)
        return temp_img    
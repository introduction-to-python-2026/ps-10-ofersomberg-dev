from PIL import Image
import numpy as np
from scipy.signal import convolve2d

def load_image(path):
    image = Image.open(path)
    image_array = np.array(image)
    return image_array

def edge_detection(image):
    grey = np.mean(image, axis=2)
    kernely = np.array([[1,2,1],[0,0,0],[-1,-2,-1]])
    kernelx = np.array([[-1,0,1],[-2,0,2],[-1,0,1]])
    edgey = consolve2d(grey, kernely)
    edgex = convolve2d(grey, kernelx)
    edgeMAG = np.sqrt(edgex**2 + edgey**2)
    return edgeMAG

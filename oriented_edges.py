import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
from gradient_orientations import gradient_orientations

def oriented_edges(img, sigma, threshold, direction, tolerance):
 
    blurred_img = cv.GaussianBlur(img, (0, 0), sigma)
    
    #gradient orientations
    gradient_orientation = gradient_orientations(blurred_img)
    
    
    #canny edges
    canny_edges = cv.Canny(blurred_img, threshold, 2 * threshold)
    
    #mask for orien. and tollerance
    valid_orientation_mask = np.logical_or(
        np.abs(gradient_orientation - direction) <= tolerance,
        np.abs(gradient_orientation - direction + 180) <= tolerance
    )
    
    #result edge_img
    edge_img = np.zeros_like(canny_edges)
    edge_img[np.logical_and(canny_edges > 0, valid_orientation_mask)] = 255
    


    return edge_img

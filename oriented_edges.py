import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
from gradient_orientations import gradient_orientations

def oriented_edges(img, sigma, threshold, direction, tolerance):
    """
    Detects oriented edges in a grayscale or color image.

    Parameters:
    img (numpy.ndarray): The input image. If the image is in color, it will be converted to grayscale.
    sigma (float): The standard deviation of the Gaussian filter used to blur the image.
    threshold (float): The lower threshold for the Canny edge detector. The upper threshold is twice this value.
    direction (float): The desired direction of the edges, in degrees. The function will detect edges whose direction
        is within `tolerance` degrees from this direction.
    tolerance (float): The tolerance in degrees for the edge direction. The function will detect edges whose direction
        is within this tolerance from the `direction` parameter.

    Returns:
    numpy.ndarray: A binary image where the edge pixels are set to 255 and the non-edge pixels are set to 0.
    """

    # TODO: Your code here

    return edge_img

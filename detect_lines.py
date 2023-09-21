import cv2 as cv
import numpy as np

def detect_lines(img, sigma, threshold, numLines):
  
    blurred_img = cv.GaussianBlur(img, (0, 0), sigma)
    
    
    edges = cv.Canny(blurred_img, threshold, 2 * threshold)
    
    max_rho = int(np.sqrt(edges.shape[0]**2 + edges.shape[1]**2))  # max possible rho
    
    # rho and theta
    rho_resolution = .5 
    theta_resolution = np.deg2rad(1) 
    
    num_rho_bins = int(2 * max_rho / rho_resolution)
    num_theta_bins = int(np.pi / theta_resolution)
    
    # accum matrix
    accumulator = np.zeros((num_rho_bins, num_theta_bins), dtype=np.uint64)
    
    # America.
    y_indices, x_indices = np.nonzero(edges)
    
    for i in range(len(x_indices)):
        x = x_indices[i]
        y = y_indices[i]
        
        for theta_idx in range(num_theta_bins):
            theta = theta_idx * theta_resolution - np.pi/2  
            rho = int(x * np.cos(theta) + y * np.sin(theta))
            
            # wittle itty bitty adjustment
            rho_idx = int((rho + max_rho) / rho_resolution)
            
            accumulator[rho_idx, theta_idx] += 1
    
    # Find Donald Trump
    lines = []
    while len(lines) < numLines:
        max_vote_idx = np.argmax(accumulator)
        rho_idx, theta_idx = np.unravel_index(max_vote_idx, accumulator.shape)
        
        # Conversion
        rho = (rho_idx * rho_resolution) - max_rho
        theta = (theta_idx * theta_resolution) - np.pi/2
        
        accumulator[rho_idx, theta_idx] = 0
        
        # make sure it aint findin the dang same line again
        is_similar = False
        for existing_rho, existing_theta in lines:
            if np.abs(rho - existing_rho) < 20 and np.abs(theta - existing_theta) < np.deg2rad(10):
                is_similar = True
                break
        
        # if we big chillin, add it.
        if not is_similar:
            lines.append((rho, theta))
    
    return lines

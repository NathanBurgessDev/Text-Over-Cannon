# # import cv2 as cv
# # img = cv.imread("balls.jpg")

# # cv.imshow("Display window", img)
# # k = cv.waitKey(0) # Wait for a keystroke in the window to close it

# this finds a single circle, using hough transforms
# import cv2 
# import numpy as np 
  
# # Read image. 
# img = cv2.imread('eyes.jpg', cv2.IMREAD_COLOR) 
  
# # Convert to grayscale. 
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
  
# # Blur using 3 * 3 kernel. 
# gray_blurred = cv2.blur(gray, (3, 3)) 
  
# # Apply Hough transform on the blurred image. 
# detected_circles = cv2.HoughCircles(gray_blurred,  
#                    cv2.HOUGH_GRADIENT, 1, 20, param1 = 50, 
#                param2 = 30, minRadius = 1, maxRadius = 40) 
  
# # Draw circles that are detected. 
# if detected_circles is not None: 
  
#     # Convert the circle parameters a, b and r to integers. 
#     detected_circles = np.uint16(np.around(detected_circles)) 
  
#     for pt in detected_circles[0, :]: 
#         a, b, r = pt[0], pt[1], pt[2] 
  
#         # Draw the circumference of the circle. 
#         cv2.circle(img, (a, b), r, (0, 255, 0), 2) 
  
#         # Draw a small circle (of radius 1) to show the center. 
#         cv2.circle(img, (a, b), 1, (0, 0, 255), 3) 
#         cv2.imshow("Detected Circle", img) 
#         cv2.waitKey(0) 


# this filters by color to find the circles of either blue  or green color

import cv2
import numpy as np

frame = cv2.imread("buffer.jpeg")

#TODO: create a while loop to take an iamge every 0.1 seconds
hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) 
    
# Threshold of blue in HSV space 
lower_blue = np.array([60, 35, 140]) 
upper_blue = np.array([180, 255, 255]) 

# preparing the mask to overlay 
mask = cv2.inRange(hsv, lower_blue, upper_blue) 
    
# The black region in the mask has the value of 0, 
# so when multiplied with original image removes all non-blue regions 
result = cv2.bitwise_and(frame, frame, mask = mask) 

cv2.imshow('frame', frame) 
cv2.imshow('mask', mask) 
# cv2.imshow('result', result) 


# erode to get rid of unneeded pixels
# kernel = np.ones((5, 5), np.uint8) 
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(7,7))

img_erosion = cv2.erode(mask, kernel, iterations=31) 
cv2.imshow('eroded', img_erosion) 

edged = cv2.Canny(img_erosion, 30, 200) 

contours, hierarchy = cv2.findContours(edged,  
    cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE) 


# # covert the tuple into a list
# contours = list(contours)

# print(type(contours))

# contour_tuples = []
# for idx, contour in enumerate(contours):
#     (x,y),radius = cv2.minEnclosingCircle(contour)
    
#     this_tuple =  (x, y)
#     contour_tuples.append(this_tuple)
#     # go from smallest x to highest x
#     # and get the pixel value from the original image at each of those values

#     while not contour_tuples:
#         # find the minimum tuple
#         xs, ys = contour_tuples
#         minx_index = xs.index(min(xs))
        
#         pixel_value = frame[contour_tuples[minx_index][1], contour_tuples[minx_index][0]]
#         del contour_tuples[minx_index]
        
#         # threshold to find if the pixel is blue
#         print(pixel_value)

#         # or if the pixel is green

       
# and append them to a list
cv2.waitKey(0) 
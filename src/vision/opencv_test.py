# this filters by color to find the circles of either blue  or green color
import cv2
import numpy as np

GREEN_BIT_VALUE = 0
BLUE_BIT_VALUE = 1

frame = cv2.imread("buffer_5.jpg")

#TODO: create a while loop to take an iamge every 0.1 seconds
hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) 

blurred = cv2.GaussianBlur(hsv,(7,7),0)
    
# Threshold of blue in HSV space 
lower_blue = np.array([60, 35, 150]) 
upper_blue = np.array([180, 255, 255]) 

# Threshold of green in HSV space
lower_green = np.array([50, 40, 20])
upper_green = np.array([70, 255, 255])

def main():
    # preparing the mask to overlay 
    blue_mask = cv2.inRange(blurred, lower_blue, upper_blue) 
    
    # preparing the mask to overlay 
    green_mask = cv2.inRange(blurred, lower_green, upper_green) 

    cv2.imshow('frame', frame) 
    cv2.imshow('blue mask', blue_mask) 


 

    green_contours = find_contours(green_mask)
    blue_contours = find_contours(blue_mask)
    print(f"green size: {len(green_contours)}")
    print(f"blue size: {len(blue_contours)}")
    
    cv2.imshow('green mask', green_mask) 

    # covert the tuple into a list
    blue_contours = list(blue_contours)
    green_contours = list(green_contours)

    blue_contour_tuples = find_contour_centers(blue_contours)
    green_contour_tuples = find_contour_centers(green_contours)

    bits = []
    
    combined_list = blue_contour_tuples + green_contour_tuples
    
    while combined_list:
        # find the minimum tuple
        xs, _ = zip(*combined_list)
        minx_index = xs.index(min(xs))
        
        is_blue = blue_mask[combined_list[minx_index][1], combined_list[minx_index][0]]
        is_green = green_mask[combined_list[minx_index][1], combined_list[minx_index][0]]
        
        if is_blue == 255:
            bits.append(BLUE_BIT_VALUE)
        elif is_green == 255:
            bits.append(GREEN_BIT_VALUE) 
        else:
            print("NOT BLUE OR GREEN")
           
        del combined_list[minx_index]     
                
    print(bits)
    cv2.waitKey(0) 
    
def find_contours(mask_image):    
    # erode to get rid of unneeded pixels
    # kernel = np.ones((5, 5), np.uint8) 
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(4,4))

    blue_img_erosion = cv2.erode(mask_image, kernel, iterations=32) 


    edged = cv2.Canny(blue_img_erosion, 30, 200) 
    
    cv2.imshow('eroded', edged) 

    contours, _ = cv2.findContours(edged,  
        cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE) 
    
    return contours

def find_contour_centers(contours): 
    contour_tuples = []
    for contour in contours:
        (x,y),_ = cv2.minEnclosingCircle(contour)
        print(f"{int(x)} {int(y)}")
        
        this_tuple =  (int(x), int(y))
        contour_tuples.append(this_tuple)
        # go from smallest x to highest x
        # and get the pixel value from the original image at each of those values  
    return contour_tuples    

if __name__ == '__main__':
    main()
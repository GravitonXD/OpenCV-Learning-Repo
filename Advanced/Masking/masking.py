# Masking allows to focus on a specific part of the image.
import cv2 as cv
import numpy as np

def main():
    # Load the img
    img = cv.imread("../../Basics/Reading Images and Video/sample_img/1_img.jpg")
    cv.imshow("Original", img)

    # Create a mask, a black image with same size as img
    mask = np.zeros(img.shape[:2], np.uint8)
    # Draw a circle in the mask
    mask_circle = cv.circle(mask, ((img.shape[1]//2)+50, img.shape[0]//2), 100, (255, 255, 255), -1)
    cv.imshow("Mask", mask_circle)
    
    # Apply the mask to the img
    masked_img = cv.bitwise_and(img, img, mask=mask_circle)
    cv.imshow("Masked Image", masked_img)
    
    # EXIT
    cv.waitKey(0)
    cv.destroyAllWindows()

# This is a python script
if __name__ == "__main__":
    main()
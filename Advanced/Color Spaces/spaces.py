# Python Script for Color Spaces
import cv2 as cv
# import matplotlib.pyplot as plt

# MAIN FUNCTION
def main():
    # Read the image
    img = cv.imread("..\..\Basics\Reading Images and Video\sample_img\\1_img.jpg")
    cv.imshow('Original Image', img)

    # Convert BGR to Grayscale
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    cv.imshow('Grayscale Image', gray)

    # Convert BGR to HSV
    # HSV: Hue Saturation Value
    hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    cv.imshow('HSV Image', hsv)

    # Convert BGR to LAB
    # LAB: Lightness A B
    lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
    cv.imshow('LAB Image', lab)

    # Display the image in matplotlib (displays in RGB color space)
    # Matplotlib displays the image in inverse
    #   plt.imshow(img)
    #   plt.show()

    # To display the image in RGB color space
    #   rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    #   cv.imshow('RGB Image (Inverse in OpenCV)', rgb) # Inverse of OpenCV
    #   plt.imshow(rgb)
    #   plt.show()
    
    # HSV to BGR
    hsv_bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
    cv.imshow('HSV to BGR', hsv_bgr)

    # LAB to BGR
    lab_bgr = cv.cvtColor(lab, cv.COLOR_LAB2BGR)
    cv.imshow('LAB to BGR', lab_bgr)
    

    cv.waitKey(0)
    cv.destroyAllWindows()

# This is a python script
if __name__ == "__main__":
    main()
# A python script to demonstrate splitting and merging of color channels in openCV
import cv2 as cv
import numpy as np

# MAIN FUNCTION
def main():
    # Load the original image
    img = cv.imread("..\..\Basics\Reading Images and Video\sample_img\\1_img.jpg")
    cv.imshow('Original Image', img)

    # Split the image into Blue, Green and Red color channels
    b, g, r = cv.split(img)
    # Display each channel, outputs a grayscale img (light=more, dark=less)
    cv.imshow('Blue Channel (Grayscale)', b)
    cv.imshow('Green Channel (Grayscale)', g)
    cv.imshow('Red Channel (Grayscale)', r)
    # To show the each channel in its respective color, use numpy
        # Create a blank canvas
    blank = np.zeros(img.shape[:2], dtype = "uint8")
    blue = cv.merge([b, blank, blank])
    green = cv.merge([blank, g, blank])
    red = cv.merge([blank, blank, r])
    cv.imshow('Blue', blue)
    cv.imshow('Green', green)
    cv.imshow('Red', red)

    # Merge the channels
    merged = cv.merge([b, g, r])
    cv.imshow('Merged Image (bgr)', merged)
    merged2 = cv.merge([r, g, b])
    cv.imshow('Merged Image (rgb)', merged2)

    cv.waitKey(0)
    cv.destroyAllWindows()


# This is a python script
if __name__ == "__main__":
    main()
# A python script that shows how to implement contours
import cv2 as cv
import numpy as np

# MAIN FUNCTION
def main():
    # Read the image
    img = cv.imread("..\Reading Images and Video\sample_img\\1_img.jpg")
    # Convert image to grayscale
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    # Blur the image
    blur = cv.GaussianBlur(gray, (5, 5), cv.BORDER_DEFAULT)
    # Grab the edges
    edges = cv.Canny(blur, 50, 150, apertureSize=3)

    # Find contours in the image
    # syntax: cv.findContours(img, mode, method, contours, hierarchy, offset=None)
    # img: image
    # mode: Retrieval mode (RETR_*)
    # method: Contour approximation method (CHAIN_APPROX_*)
    # contours: Output vector of contours
    # hierarchy: Output vector of contour hierarchy
    # offset: Optional offset of the first pixel in the scanned image
    contours1, hierarchy = cv.findContours(edges, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
    print(f"Total contours (1) found: {len(contours1)}")

    cv.imshow('Contours (1)', edges)

    # Alternatively, cv.threshold() can be used instead of edges
        # syntax: cv.threshold(src, thresh, maxval, type, dst=None)
        # src: input image
        # thresh: threshold value
        # maxval: maximum value
        # type: threshold type (THRESH_*)
        # dst: destination image
    thresh, threshImg = cv.threshold(edges, 127, 255, cv.THRESH_BINARY_INV)
    contours2, hierarchy = cv.findContours(threshImg, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
    print(f"Total contours (2) found: {len(contours2)}")

    cv.imshow('Contours (2)', threshImg)


    # Draw the contours
    blank = np.zeros((img.shape[0], img.shape[1], 3), np.uint8)
    # drawContours(img, contours, contourIdx, color, thickness, lineType, hierarchy, maxLevel, offset=None)
        # img: input image
        # contours: input contours
        # contourIdx: index of contour
        # color: color of contour
        # thickness: thickness of contour
        # lineType: line type
        # hierarchy: contour hierarchy
        # maxLevel: maximum level
        # offset: offset of contour
    cv.drawContours(blank, contours1, -1, (255, 0, 0), 1)
    # Put text on the image (contour 1 count)
    cv.putText(blank, f"Contour 1: {len(contours1)}", (10, 30), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
    cv.imshow('Drawn Contours', blank)

    cv.waitKey(0)
    cv.destroyAllWindows()


# This is a python script
if __name__ == '__main__':
    main()
import cv2 as cv
import numpy as np

# MAIN FUNCTION
def main():
    # color = (B, G, R)
    whiteColor = 255,255,255
    blackColor = 0,0,0
    redColor = 0,0,255
    blueColor = 255,0,0
    greenColor = 0,255,0

    # Create a blank canvas using numpy zeros()
    # syntax and parameters: np.zeros(shape, dtype=float, order='C')
    blank = np.zeros((500, 500, 3), dtype=np.uint8)

    # TASK 1: Paint the image a certain color
    # Sets the whole np array to a certain color
    blank[:] = whiteColor
    # Display the image

    # TASK 2: Drawing a Rectangle
    # Draw a rectangle using rectangle()
    # syntax and parameters: cv.rectangle(image, (x, y), (x+width, y+height), color, thickness=1, lineType=8, shift=0)
    # x, y: top left corner of the rectangle
    # x+width, y+height: bottom right corner of the rectangle
    # color: color of the rectangle
    # thickness: thickness of the
    # rectangle, can be filled using cv.FILLED or value = -1
    cv.rectangle(blank, (0, 0), (blank.shape[1]//2, blank.shape[0]//2), (blueColor), thickness=cv.FILLED)
    
    # TASK 3: Drawing a Circle
    # Draw a circle using circle()
    # syntax and parameters: cv.circle(image, (x, y), radius, color, thickness=1, lineType=8, shift=0)
    # x, y: center of the circle
    # radius: radius of the circle
    # color: color of the circle
    # thickness: thickness of the circle
    cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), blank.shape[0]//4, (redColor), thickness=cv.FILLED)

    # TASK 4: Drawing a Line
    # Draw a line using line()
    # syntax and parameters: cv.line(image, (x1, y1), (x2, y2), color, thickness=1, lineType=8, shift=0)
    # x1, y1: start point of the line
    # x2, y2: end point of the line
    # color: color of the line
    # thickness: thickness of the line
    cv.line(blank, (250,250), (500,500), (greenColor), thickness=2)

    # TASK 5: Writing Text
    # Write text using putText()
    # syntax and parameters: cv.putText(image, text, org, fontFace, fontScale, color, thickness=1, lineType=8, bottomLeftOrigin=False)
    # text: text to be written
    # org: location of the text
    # fontFace: font of the text
    # fontScale: size of the text
    # color: color of the text
    # thickness: thickness of the text
    # lineType: type of the text
    # bottomLeftOrigin: if True, the text is written starting from the bottom-left corner
    cv.putText(blank, "openCV Shapes", (10, 450), cv.FONT_HERSHEY_SIMPLEX, 1, (blackColor), thickness=2)

    # display the image
    cv.imshow('Sample Drawing', blank)

    cv.waitKey(0)


# This is a python script, so we need to call the main function
if __name__ == "__main__":
    main()
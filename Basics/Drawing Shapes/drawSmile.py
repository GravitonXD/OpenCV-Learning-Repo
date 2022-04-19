# This python script is an exercise based on the learnings from draw.py
# code by John Markton M. Olarte
import cv2 as cv
import numpy as np

WHITE_COLOR = 255,255,255
BLACK_COLOR = 0,0,0
YELLOW_COLOR = 0,255,255


def main():
    canvas = np.zeros((500, 500, 3), dtype=np.uint8)
    canvas[:] = WHITE_COLOR
    # Create a yellow circle
    
    cv.circle(canvas, (canvas.shape[1]//2, canvas.shape[0]//2), canvas.shape[0]//4, YELLOW_COLOR, cv.FILLED)
    # Circle Outline
    cv.circle(canvas, (canvas.shape[1]//2, canvas.shape[0]//2), canvas.shape[0]//4, BLACK_COLOR, thickness=2)

    # Create two black lines for the eyes
    cv.line(canvas, (225,250), (225,200), BLACK_COLOR, thickness=10)
    cv.line(canvas, (275,250), (275,200), BLACK_COLOR, thickness=10)

    # Create a white half-circle for the mouth using cv.ellipse()
    # syntax and parameters: cv.ellipse(image, center, axes, angle, startAngle, endAngle, color, thickness=1, lineType=8, shift=0)
    # center: center of the ellipse
    # axes: axes of the ellipse
    # angle: angle of the ellipse
    # startAngle: starting angle of the ellipse
    # endAngle: ending angle of the ellipse
    # color: color of the ellipse
    # thickness: thickness of the ellipse
    # lineType: type of the ellipse
    # shift: shift of the ellipse
    cv.ellipse(canvas, (250,175), (100,150), 0, 45, 135, BLACK_COLOR, thickness=10)
    
    # Add a text on the top and bottom of the canvas
    cv.putText(canvas, "Just Keep on Smiling!", (80, 75), cv.FONT_HERSHEY_SIMPLEX, 1, (BLACK_COLOR), thickness=2)
    cv.putText(canvas, "Just Keep on Smiling!", (80, 450), cv.FONT_HERSHEY_SIMPLEX, 1, (BLACK_COLOR), thickness=2)
    # Display the image
    cv.imshow('Smiley Face', canvas)

    cv.waitKey(0)

# This is a python script, so we need to call the main function
if __name__ == "__main__":
    main()
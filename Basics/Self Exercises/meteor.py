# This script is an exercise for moving shapes
# An implementation of the learnings from reading a video, and drawing of shapes.
# by JOHN MARKTON OLARTE

import cv2 as cv
import numpy as np
import random as rnd

WHITE_COLOR = 255,255,255
BLACK_COLOR = 0,0,0
GRAY_COLOR = 128,128,128
BLUE_COLOR = 255,0,0
YELLOW_COLOR = 0,255,255
RED_COLOR = 0,0,255

def meteorite_color(speed):
    if 1 <= speed <= 3:
        return BLUE_COLOR
    elif 4 <= speed <= 6:
        return YELLOW_COLOR
    elif 7 <= speed <= 9:
        return RED_COLOR
    else:
        return GRAY_COLOR

def main():
    # Create a blank animation_canvas
    animation_canvas = np.zeros((300, 300, 3), dtype="uint8")
    speed_iter_canvas = np.zeros((50, 300, 3), dtype="uint8")

    # initialized position of the x & y coordinates, iteration#, and speed of the moving ball
    position_x = animation_canvas.shape[1]//2
    position_y = 0
    speed = rnd.randint(1,10)
    iterations = 1
    
    # Initialize the color of the meteorite based on its speed

    # Draw a white circle on the animation_canvas that will move in y based on the speed variable
    while True:
         # display the speed and iteration
        cv.putText(speed_iter_canvas, f"Speed: {speed} || Iterations: {iterations}", (20, 20), cv.FONT_HERSHEY_SIMPLEX, 0.5, (RED_COLOR), 1)
        cv.putText(speed_iter_canvas, "Press 'p' to pause", (20, 40), cv.FONT_HERSHEY_SIMPLEX, 0.5, (RED_COLOR), 1)
        cv.imshow("Speed & Iteration Counter", speed_iter_canvas)

        if position_y > animation_canvas.shape[0]:
            # increment iteration count
            iterations += 1
            # reset position of the y coordinate
            position_y = 0
            # reset both canvasses
            animation_canvas = np.zeros((300, 300, 3), dtype="uint8")
            speed_iter_canvas = np.zeros((50, 300, 3), dtype="uint8")
            # change speed, make sure it is not the same as the previous speed
            new_speed = rnd.randint(1,10)
            speed = new_speed if new_speed != speed else speed
        
        # draw a white circle on the animation_canvas
        cv.circle(animation_canvas, (position_x, position_y), 10, (WHITE_COLOR), cv.FILLED)
        # show the circle in the animation_canvas
        cv.imshow('Meteorite', animation_canvas)

        # increment the y coordinate
        position_y += speed
        # to simulate the movement of the circle, add a black circle on top of the previous white circle.
        cv.circle(animation_canvas, (position_x, position_y-speed), 10, (BLACK_COLOR), cv.FILLED)
        # simulate a lightening effect on the meteorite based on the speed
        circle_blur = cv.circle(animation_canvas, (position_x, position_y-speed), 10, (meteorite_color(speed)), cv.FILLED)
        cv.GaussianBlur(circle_blur, (0,0), 10, circle_blur)

        # Press 'p' to pause the animation
        if cv.waitKey(20) & 0xFF == ord('p'):
            break

    cv.waitKey(0)
    cv.destroyAllWindows()

# This is a python script.
if __name__ == "__main__":
    main()
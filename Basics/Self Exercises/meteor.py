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

def draw_star(canvas):
    x = rnd.randint(0, canvas.shape[1])
    y = rnd.randint(0, canvas.shape[0])
    rad = rnd.randint(1, 3)

    # Draw a star on the animation_canvas
    cv.circle(canvas, (x, y), rad, (WHITE_COLOR), cv.FILLED)
    # show the circle in the animation_canvas
    cv.imshow('Meteoroid', canvas)

def create_canvas(width, height):
    return np.zeros((height, width, 3), dtype="uint8")

def meteoroid_color(speed):
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
    animation_canvas = create_canvas(300, 300)
    speed_iter_canvas = create_canvas(300, 50)

    # initialized position of the x & y coordinates, iteration#, and speed of the moving ball
    position_x = animation_canvas.shape[1]//2
    position_y = 0
    speed = rnd.randint(1,10)
    iterations = 1

    # Draw a white circle on the animation_canvas that will move in y based on the speed variable
    while True:
        # Draw stars on the animation_canvas
        draw_star(animation_canvas)

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
            animation_canvas = create_canvas(300, 300)
            speed_iter_canvas = create_canvas(300, 50)
            # change speed, make sure it is not the same as the previous speed
            new_speed = rnd.randint(1,10)
            speed = new_speed if new_speed != speed else speed
        
        # draw a white circle on the animation_canvas
        cv.circle(animation_canvas, (position_x, position_y), 10, (WHITE_COLOR), cv.FILLED)
        # show the circle in the animation_canvas
        cv.imshow('Meteoroid', animation_canvas)

        # increment the y coordinate
        position_y += speed
        # to simulate the movement of the circle, add a black circle on top of the previous white circle.
        cv.circle(animation_canvas, (position_x, position_y-speed), 10, (BLACK_COLOR), cv.FILLED)
        # simulate a lightening effect on the meteoroid based on the speed
        circle_blur = cv.circle(animation_canvas, (position_x, position_y-speed), 10, (meteoroid_color(speed)), cv.FILLED)
        cv.GaussianBlur(circle_blur, (0,0), 10, circle_blur)

        # Press 'p' to pause the animation
        if cv.waitKey(20) & 0xFF == ord('p'):
            break

    cv.waitKey(0)
    cv.destroyAllWindows()

# This is a python script.
if __name__ == "__main__":
    main()
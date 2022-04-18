# Reading an image using openCV
# This program displays the images in the sample image directory one-by-one
from posixpath import dirname
import cv2 as cv
from cv2 import scaleAdd

# RESCALE IMAGE FUNCTION
def rescale_img(frame, scale=0.75):
    # Rescale the image to a scale of its original size
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    # Resize the image using resize()
    # syntax and parameters: cv.resize(image, dimensions, interpolation)
    # interpolation: cv.INTER_AREA, cv.INTER_LINEAR, cv.INTER_CUBIC, cv.INTER_NEAREST
    # cv.INTER_AREA: Resize the image to fit to the dimensions exactly
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


# MAIN FUNCTION
def main():
    to_display = [] # List to store images to display


    # Display images in the sample images folder one-by-one
    for img_num in range(1, 3):
        # Read an image using imread()
        # syntax and parameters: cv.imread(path, flags)
        path = f"sample_img/{img_num}_img.jpg" # Make sure images are in .jpg format
        img = cv.imread(path)
        to_display.append(img)

    for img_num in range(len(to_display)):
        # To show the image use: imshow()
        # syntax and parameters: cv.imshow(window_name, image)
        # rescale the image to a scale of its original size
        cv.imshow(f'Sample Image {img_num + 1}: Cat', rescale_img(to_display[img_num], scale=0.5))

        # wait for any key to be pressed, then the next image in to_display will be displayed
        cv.waitKey(0)

# This is a python script, so we need to call the main function
if __name__ == "__main__":
    main()
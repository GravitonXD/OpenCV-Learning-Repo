# Reading an image using openCV
# This program displays the images in the sample image directory one-by-one
import cv2 as cv

# Main Function
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
        cv.imshow(f'Sample Image {img_num + 1}: Cat', to_display[img_num])

        # wait for any key to be pressed, then the next image in to_display will be displayed
        cv.waitKey(0)

# This is a python script, so we need to call the main function
if __name__ == "__main__":
    main()
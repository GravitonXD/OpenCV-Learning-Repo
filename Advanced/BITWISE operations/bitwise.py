# This python script shows the different application of bitwise operation in openCV.
import cv2 as cv
import numpy as np

def main():
    # Create two blank images
    img1 = np.zeros((200, 200, 3), np.uint8)
    img2 = np.zeros((200, 200, 3), np.uint8)

    # Draw a circle in img1 and a rectangle in img2
    cv.circle(img1, (100, 100), 40, (255, 255, 255), -1)
    cv.rectangle(img2, (190, 190), (100,100), (255, 255, 255), -1)

    # Show the images
    cv.imshow("img1", img1)
    cv.imshow("img2", img2)

    # Bitwise AND
    # The bitwise AND operation is used to find the intersection of two images.
    # The result is a new image where the pixels are set to 1 if both the corresponding pixels in the two images are 1.
    # The pixels are set to 0 otherwise.
    # The result is a binary image.
    img_and = cv.bitwise_and(img1, img2)
    cv.imshow("AND", img_and)

    # Bitwise OR
    # The bitwise OR operation is used to find the union of two images.
    # The result is a new image where the pixels are set to 1 if either the corresponding pixels in the two images are 1.
    # The pixels are set to 0 otherwise.
    # The result is a binary image.
    img_or = cv.bitwise_or(img1, img2)
    cv.imshow("OR", img_or)

    # Bitwise XOR
    # The bitwise XOR operation is used to find the symmetric difference of two images.
    # The result is a new image where the pixels are set to 1 if either the corresponding pixels in the two images are 1.
    # The pixels are set to 0 otherwise.
    # The result is a binary image.
    img_xor = cv.bitwise_xor(img1, img2)
    cv.imshow("XOR", img_xor)

    # Bitwise NOT
    # The bitwise NOT operation is used to invert the image.
    # The result is a new image where the pixels are set to 0 if the corresponding pixels in the original image are 1.
    # The pixels are set to 1 otherwise.
    # The result is a binary image.
    img_not = cv.bitwise_not(img1)
    cv.imshow("NOT of img1", img_not)

    # EXIT
    cv.waitKey(0)
    cv.destroyAllWindows()

# This is a python script
if __name__ == "__main__":
    main()
# Python Script for Image Transformations
import cv2 as cv
import numpy as np

# 1. Translating an Image
    # -x shift to the left
    # -y shift up
    # +x shift to the right
    # +y shift down
def translate_image(img, x, y):
    # Create a translation matrix
    transMat = np.float32([[1, 0, x], [0, 1, y]])
    # Indicate the dimensions of the image
    dimensions = (img.shape[1], img.shape[0])

    # Apply the translation to the image using warpAffine
        # syntax and parameters: cv.warpAffine(src, M, dsize, dst, flags, borderMode, borderValue)
        # src: source image
        # M: 2D transformation matrix
        # dsize: destination image dimensions
        # dst: destination image
        # flags: flags
        # borderMode: border mode
        # borderValue: border value
    return cv.warpAffine(img, transMat, dimensions)


# 2. Rotating an Image
    # -angle --> rotates image clockwise
    # +angle --> rotates image anti-clockwise
def rotate_image(img, angle, rotationPoint=None):
    # Get a tuple of the image dimensions
    (height, width) = img.shape[:2]

    # If no rotation point is provided, then set the rotation point to the center of the image
    if rotationPoint is None:
        rotationPoint = (width/2, height/2)
    
    # Create a rotation matrix
    rotationMat = cv.getRotationMatrix2D(rotationPoint, angle, 1.0)
    dimensions = (width, height)

    # Apply the rotation to the image using warpAffine
    return cv.warpAffine(img, rotationMat, dimensions, flags=cv.INTER_LINEAR)

# MAIN FUNCTION
def main():
    img = cv.imread("..\Reading Images and Video\sample_img\\1_img.jpg")
    cv.imshow('Original Image', img)

    # Translate the image
    translatedImg = translate_image(img, 100, 50)
    cv.imshow('Translated Image', translatedImg)
    
    # Rotate the image
    rotatedImg = rotate_image(img, 35)
    cv.imshow('Rotated Image', rotatedImg)

    # Resize the image (larger image)
    resizedImg = cv.resize(img, (0,0), fx=1.5, fy=1.5, interpolation=cv.INTER_CUBIC)
    cv.imshow('Resized Image', resizedImg)

    # Flipping the Image
        # Using flip() function
        # Syntax: cv.flip(src, flipCode)
        # src: source image
        # flipCode: 0 --> FLIP_VERTICAL
        #           1 --> FLIP_HORIZONTAL
        #           -1 --> FLIP_BOTH
    flippedImg = cv.flip(img, 2)
    cv.imshow('Flipped Image', flippedImg)

    # Cropping the Image
        # using array splicing
    croppedImg = img[0:200, 0:200]
    cv.imshow('Cropped Image', croppedImg)

    # Exit Windows
    cv.waitKey(0)
    cv.destroyAllWindows()

if __name__ == "__main__":
    main()
# Blurring Techniques in openCV
# Blurring is used to reduce noise.
import cv2 as cv

# MAIN FUNCTION
def main():
    # Load the original image
    img = cv.imread("..\..\Basics\Reading Images and Video\sample_img\\1_img.jpg")
    cv.imshow("Original Image", img)

    # Blur Averaging
    # Averaging is the simplest blurring technique. It is used to reduce noise by averaging the pixels in a 3x3 neighborhood.
    average = cv.blur(img, (3, 3)) # the higher the kernel size the more blurry the image becomes
    cv.imshow("Average Blur", average)

    # Gaussian Blur
    # Gaussian blurring is a more advanced technique. It is used to reduce noise by convolving the image with a Gaussian kernel.
    gaussian = cv.GaussianBlur(img, (3, 3), 0) # the higher the kernel size the more blurry the image becomes
    cv.imshow("Gaussian Blur", gaussian)

    # Median Blur
    # Median blurring is another more advanced technique. It is used to reduce noise by replacing each pixel with the median value of a 3x3 neighborhood.
    # More useful in images with salt and pepper noise.
    median = cv.medianBlur(img, 3) # the higher the kernel size the more blurry the image becomes
    cv.imshow("Median Blur", median)

    # Bilateral Blur
    # Bilateral blurring is yet another more advanced technique. It is used to reduce noise by replacing each pixel with the median value of a 3x3 neighborhood.
    # Most effective blurring method, as it retains edges better than other methods.
        # syntax: cv.bilateralFilter(src, d, sigmaColor, sigmaSpace)
        # d: diameter of each pixel neighborhood that is used during filtering.
        # sigmaColor: filter sigma in the color space. A larger value of the parameter means that farther colors within the pixel neighborhood (see sigmaSpace) will be mixed together, resulting in larger areas of semi-equal color.
        # sigmaSpace: filter sigma in the coordinate space. A larger value of the parameter means that farther pixels will influence each other as long as their colors are close enough (see sigmaColor).
    bilateral = cv.bilateralFilter(img, 9, 75, 75) # the higher the diameter the more blurry the image becomes
    cv.imshow("Bilateral Blur", bilateral)

    cv.waitKey(0)
    cv.destroyAllWindows()


# This is a python script
if __name__ == "__main__":
    main()
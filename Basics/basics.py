# Basic and Essential OpenCV Functions
import cv2 as cv

def main():
    img = cv.imread("Reading Images and Video\sample_img\\1_img.jpg")
    cv.imshow('Original Image', img)

    # 1. Converting to Grayscale
        # using cv.cvtColor()
        # syntax and parameters: cv.cvtColor(src, dst, code)
        # src: source image
        # dst: destination image
        # code: conversion code
        # conversion codes: cv.COLOR_BGR2GRAY, cv.COLOR_RGB2GRAY
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    cv.imshow('Gray Image', gray)

    # 2. Blurring an Image
        # using cv.GaussianBlur()
        # syntax and parameters: cv.GaussianBlur(src, dst, ksize, sigmaX, sigmaY)
        # src: source image
        # dst: destination image
        # ksize: kernel size (tuple) and must be an odd number; to increase bluriness
        # sigmaX: sigma for the x-axis
        # sigmaY: sigma for the y-axis
    blur = cv.GaussianBlur(img, (5, 5), cv.BORDER_DEFAULT)
    cv.imshow('Blurred Image', blur)

    # 3. Edge Detection
        # using cv.Canny()
        # syntax and parameters: cv.Canny(src, dst, threshold1, threshold2)
        # src: source image
        # dst: destination image
        # threshold1: first threshold for the hysteresis procedure
        # threshold2: second threshold for the hysteresis procedure
    edge = cv.Canny(img, 100, 200)
    cv.imshow('Edge Image', edge)

    # 4. Dilating the Image
        # using cv.dilate()
        # syntax and parameters: cv.dilate(src, dst, kernel, iterations)
        # src: source image
        # dst: destination image
        # kernel: kernel for dilation
        # iterations: number of iterations for dilation
    dilate = cv.dilate(edge, (3,3), iterations=1)
    cv.imshow('Dilated Image', dilate)

    # 5. Eroding the Image
        # using cv.erode()
        # syntax and parameters: cv.erode(src, dst, kernel, iterations)
        # src: source image
        # dst: destination image
        # kernel: kernel for erosion
        # iterations: number of iterations for erosion
    erode = cv.erode(dilate, (3,3), iterations=1)
    cv.imshow('Eroded Image', erode)

    # 6. Resizing the Image
        # using cv.resize()
        # syntax and parameters: cv.resize(src, dst, fx, fy, interpolation)
        # src: source image
        # dst: destination image
        # fx: scale factor along the horizontal axis
        # fy: scale factor along the vertical axis
        # interpolation: interpolation code
    resized = cv.resize(img, (0,0), fx=0.5, fy=0.5, interpolation=cv.INTER_AREA)
    cv.imshow('Resized Image', resized)

    # 7. Cropping the Image
    crop = img[100:400, 100:400]
    cv.imshow('Cropped Image', crop)

    # exit the program
    cv.waitKey(0)
    cv.destroyAllWindows()

# This is a python script, so we need to call the main function
if __name__ == "__main__":
    main()
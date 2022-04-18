# This python script opens the webcam of the user and displays it in a window
import cv2 as cv

# CHANGE VIDEO RESOLUTION
def changeRes(capture, width, height):
    # Change the resolution of the video
    # syntax and parameters: cap.set(propId, value)
    # propId: cv.CAP_PROP_FRAME_WIDTH, cv.CAP_PROP_FRAME_HEIGHT
    # value: the new resolution
    capture.set(cv.CAP_PROP_FRAME_WIDTH, width)
    capture.set(cv.CAP_PROP_FRAME_HEIGHT, height)

# RESCALE VIDEO FRAME FUNCTION
def rescale_vid(frame, scale=0.75):
    # Rescale the frame to a scale of its original size
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    # Resize the video frame using resize()
    # syntax and parameters: cv.resize(image, dimensions, interpolation)
    # interpolation: cv.INTER_AREA, cv.INTER_LINEAR, cv.INTER_CUBIC, cv.INTER_NEAREST
    # cv.INTER_AREA: Resize the image to fit to the dimensions exactly
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

# MAIN FUNCTION
def main():
    # Read Videos
    # using cv.VideoCapture()
    # syntax and parameters: cv.VideoCapture(path)
    # path can be a file path or a camera number
    # if path is a camera number, it will be 0, 1, 2, etc.
    webCam = cv.VideoCapture(0) # 0 is the default camera
    # Check if the webcam is opened
    if not webCam.isOpened():
        print("Error opening video stream or file")
        exit()
    
    # change the resolution of the video to 640x480
    changeRes(webCam, 640, 480)
    
    # To display a video, each frame should be displayed for a certain amount of time
    while True:
        # Read a frame from the video
        isTrue, frame = webCam.read()

        # Rescale the video frame to a scale(0.5) of its original size
        frame_resized1 = rescale_vid(frame, scale=0.5)
        # Rescale the video frame to a scale(0.75) of its original size
        frame_resized2 = rescale_vid(frame)

        # Display the frame
        cv.imshow('Webcam', frame)
        # Display the frame resized at scale = 0.5
        cv.imshow('Webcam Resized (0.5)', frame_resized1)
        # Display the frame resized at scale = 0.75
        cv.imshow('Webcam Resized (0.75)', frame_resized2)
        


        
        # To break the loop, press 'q'
        if cv.waitKey(20) & 0xFF == ord('q'):
            break
    
    # When everything done, release the capture
    webCam.release()
    # Destroy all the windows
    cv.destroyAllWindows()

# This is a python script, so we need to call the main function
if __name__ == "__main__":
    main()
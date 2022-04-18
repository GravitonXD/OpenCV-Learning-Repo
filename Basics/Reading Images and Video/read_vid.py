# This python script opens the webcam of the user and displays it in a window
import cv2 as cv

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
    
    # To display a video, each frame should be displayed for a certain amount of time
    while True:
        # Read a frame from the video
        isTrue, frame = webCam.read()

        # Display the frame
        cv.imshow('Webcam', frame)
        
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
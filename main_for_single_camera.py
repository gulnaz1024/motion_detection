import cv2

def frame_preprocessing(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Apply background subtraction
    fgmask = mog.apply(gray)

    # Apply morphological operations to reduce noise and fill gaps
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2, 2))
    fgmask2 = cv2.erode(fgmask, kernel, iterations=1)
    fgmask3 = cv2.dilate(fgmask2, kernel, iterations=1)

    return fgmask3

def detect_cam_motion(frame):
    fgmask = frame_preprocessing(frame)  
    contours, hierarchy = cv2.findContours(fgmask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    cam_motion_detected = False

    for contour in contours:
        # Ignore small contours
        if cv2.contourArea(contour) < 800:
            continue

        # Draw bounding box around contour
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
       
        # For loop after loop draws all the contours one by one that belong to the same frame. Therefore, you should add the rendered frame to the video after FULL rendering, otherwise you will get frame not with all contours at once, but a lot of frames with single contours on the video. And since you get more frames than there should be video is lagging.
        cam_motion_detected = True

    if cam_motion_detected:
        cv2.putText(frame, "Motion Detected", (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)
        out.write(frame)
        cam_motion_detected = False

    if has_frame and cam_switcher % 2 == 1:        
        if cam_recording_switcher % 2 == 1:              
            cv2.putText(frame, "Recording in progress", (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)
            out.write(frame)
        else:
            cv2.imshow('Laptop Cam', frame)
    else:
        cv2.imshow('Laptop Cam', cam_off)

cam_capture = cv2.VideoCapture(0)
cam_frame_width = int(cam_capture.get(3))
cam_frame_height = int(cam_capture.get(4))
cam_switcher = 1
cam_recording_switcher = 0
cam_off = cv2.imread('img/laptop-off.jpg')
out = cv2.VideoWriter('Laptop_camera.mp4', cv2.VideoWriter_fourcc(*'XVID'), 28, (cam_frame_width, cam_frame_height))

# Create the MOG2 background subtractor object
mog = cv2.createBackgroundSubtractorMOG2()

while True:
    # Capture frame-by-frame
    has_frame, frame = cam_capture.read()

    # Camera (Switcher key - 1, Record key - R)
    detect_cam_motion(frame)

    key = cv2.waitKey(1)
    if key == ord('1'):
        cam_switcher += 1
    elif key == ord('R') or key == ord('r'):
        cam_recording_switcher += 1
    elif key == ord('Q') or key == ord('q'):
        break    

# When everything is done, release the capture
cam_capture.release()
out.release()
cv2.destroyAllWindows()

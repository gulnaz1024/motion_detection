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

def detect_laptop_cam_motion(frame_laptop_cam):
    fgmask_laptop_cam = frame_preprocessing(frame_laptop_cam)  
    contours_laptop_cam, hierarchy = cv2.findContours(fgmask_laptop_cam, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    laptop_cam_motion_detected = False

    for contour in contours_laptop_cam:
        # Ignore small contours
        if cv2.contourArea(contour) < 500:
            continue

        # Draw bounding box around contour
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(frame_laptop_cam, (x, y), (x+w, y+h), (0, 255, 0), 2)
       
        # For loop after loop draws all the contours one by one that belong to the same frame. Therefore, you should add the rendered frame to the video after FULL rendering, otherwise you will get frame not with all contours at once, but a lot of frames with single contours on the video. And since you get more frames than there should be video is lagging.
        laptop_cam_motion_detected = True

    if laptop_cam_motion_detected:
        cv2.putText(frame_laptop_cam, "Motion Detected", (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)
        out_laptop_cam.write(frame_laptop_cam)
        laptop_cam_motion_detected = False

    if has_frame_laptop_cam and laptop_cam_switcher % 2 == 1:        
        if laptop_cam_recording_switcher % 2 == 1:              
            cv2.putText(frame_laptop_cam, "Recording in progress", (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)       
            cv2.imshow('Laptop Cam', frame_laptop_cam)
            out_laptop_cam.write(frame_laptop_cam)
        else:
            cv2.imshow('Laptop Cam', frame_laptop_cam)
    else:
        cv2.imshow('Laptop Cam', laptop_cam_off)

def detect_USB_cam_motion(frame_USB_cam):
    fgmask_USB_cam = frame_preprocessing(frame_USB_cam)  
    contours_USB_cam, hierarchy = cv2.findContours(fgmask_USB_cam, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    USB_cam_motion_detected = False

    for contour in contours_USB_cam:
        # Ignore small contours
        if cv2.contourArea(contour) < 500:
            continue
                
        # Draw bounding box around contour
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(frame_USB_cam, (x, y), (x+w, y+h), (0, 255, 0), 2)
        
        # For loop after loop draws all the contours one by one that belong to the same frame. Therefore, you should add the rendered frame to the video after FULL rendering, otherwise you will get frame not with all contours at once, but a lot of frames with single contours on the video. And since you get more frames than there should be video is lagging.
        USB_cam_motion_detected = True
    
    if USB_cam_motion_detected:
        cv2.putText(frame_USB_cam, "Motion Detected", (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)
        out_USB_cam.write(frame_USB_cam) 
        USB_cam_motion_detected = False

    if has_frame_USB_cam and USB_cam_switcher % 2 == 1:        
        if USB_cam_recording_switcher % 2 == 1:
            cv2.putText(frame_USB_cam, "Recording in progress", (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)   
            cv2.imshow('USB Cam', frame_USB_cam)         
            out_USB_cam.write(frame_USB_cam)          
        else:
            cv2.imshow('USB Cam', frame_USB_cam)
    else:
        cv2.imshow('USB Cam', USB_cam_off)

laptop_cam_capture = cv2.VideoCapture(1)
laptop_cam_frame_width = int(laptop_cam_capture.get(3))
laptop_cam_frame_height = int(laptop_cam_capture.get(4))
laptop_cam_switcher = 1
laptop_cam_recording_switcher = 0
laptop_cam_off = cv2.imread('img/laptop-off.jpg')
out_laptop_cam = cv2.VideoWriter('Laptop_camera.mp4', cv2.VideoWriter_fourcc(*'XVID'), 28, (laptop_cam_frame_width, laptop_cam_frame_height))

USB_cam_capture = cv2.VideoCapture(0)
USB_cam_frame_width = int(laptop_cam_capture.get(3))
USB_cam_frame_height = int(laptop_cam_capture.get(4))
USB_cam_switcher = 1
USB_cam_recording_switcher = 0
USB_cam_off = cv2.imread('img/usb-off.jpg')
out_USB_cam = cv2.VideoWriter('USB_camera.mp4', cv2.VideoWriter_fourcc(*'XVID'), 25, (USB_cam_frame_width, USB_cam_frame_height))

# Create the MOG2 background subtractor object
mog = cv2.createBackgroundSubtractorMOG2()

while True:
    # Capture frame-by-frame
    has_frame_laptop_cam, frame_laptop_cam = laptop_cam_capture.read()
    has_frame_USB_cam, frame_USB_cam = USB_cam_capture.read()  

    # Laptop Camera (Switcher key - 1, Record key - L)
    detect_laptop_cam_motion(frame_laptop_cam)

    # USB Camera (Switcher key - 2, Record key - R) 
    detect_USB_cam_motion(frame_USB_cam)

    key = cv2.waitKey(1)
    if key == ord('1'):
        laptop_cam_switcher += 1
    elif key == ord('2'):
        USB_cam_switcher += 1
    elif key == ord('L') or key == ord('l'):
        laptop_cam_recording_switcher += 1
    elif key == ord('U') or key == ord('u'):
        USB_cam_recording_switcher += 1
    elif key == ord('Q') or key == ord('q'):
        break    

# When everything is done, release the capture
USB_cam_capture.release()
laptop_cam_capture.release()
out_laptop_cam.release()
out_USB_cam.release()
cv2.destroyAllWindows()
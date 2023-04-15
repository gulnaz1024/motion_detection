import cv2

built_in_cam_capture = cv2.VideoCapture(1)
USB_cam_capture = cv2.VideoCapture(0)

built_in_cam_switcher = 1
USB_cam_switcher = 1

built_in_cam_off = cv2.imread('built-in.jpg')
USB_cam_off = cv2.imread('usb.jpg')

while True:
    # Capture frame-by-frame
    has_frame_built_in_cam, frame_built_in_cam = built_in_cam_capture.read()
    has_frame_USB_cam, frame_USB_cam = USB_cam_capture.read()    

    # Built-in Camera (Switcher key - 1) 
    if has_frame_built_in_cam and built_in_cam_switcher % 2 == 1:
        cv2.imshow('Built-in Cam', frame_built_in_cam)
    else:
        cv2.imshow('Built-in Cam', built_in_cam_off)

    # USB Camera (Switcher key - 2) 
    if has_frame_USB_cam and USB_cam_switcher % 2 == 1:
        cv2.imshow('USB Cam', frame_USB_cam)
    else:
        cv2.imshow('USB Cam', USB_cam_off)

    key = cv2.waitKey(1)
    if key == ord('1'):
        built_in_cam_switcher += 1
    elif key == ord('2'):
        USB_cam_switcher += 1
    elif key == ord('R') or key == ord('r'):
        print("RECORD STARTED")
    elif key == ord('q'):
        break    

# When everything is done, release the capture
USB_cam_capture.release()
built_in_cam_capture.release()
cv2.destroyAllWindows()
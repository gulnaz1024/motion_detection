import cv2

laptop_cam_capture = cv2.VideoCapture(1)
laptop_cam_frame_width = int(laptop_cam_capture.get(3))
laptop_cam_frame_height = int(laptop_cam_capture.get(4))
laptop_cam_switcher = 1
laptop_cam_recording_switcher = 0
laptop_cam_off = cv2.imread('built-in.jpg')
out_laptop_cam = cv2.VideoWriter('Laptop_camera.mp4', cv2.VideoWriter_fourcc(*'XVID'), 28, (laptop_cam_frame_width, laptop_cam_frame_height))

USB_cam_capture = cv2.VideoCapture(0)
USB_cam_frame_width = int(laptop_cam_capture.get(3))
USB_cam_frame_height = int(laptop_cam_capture.get(4))
USB_cam_switcher = 1
USB_cam_recording_switcher = 0
USB_cam_off = cv2.imread('usb.jpg')
out_USB_cam = cv2.VideoWriter('USB_camera.mp4', cv2.VideoWriter_fourcc(*'XVID'), 25, (USB_cam_frame_width, USB_cam_frame_height))

while True:
    # Capture frame-by-frame
    has_frame_laptop_cam, frame_laptop_cam = laptop_cam_capture.read()
    has_frame_USB_cam, frame_USB_cam = USB_cam_capture.read()    

    # Laptop Camera (Switcher key - 1, Record key - L) 
    if has_frame_laptop_cam and laptop_cam_switcher % 2 == 1:
        cv2.imshow('Laptop Cam', frame_laptop_cam)
        if laptop_cam_recording_switcher % 2 == 1:         
            out_laptop_cam.write(frame_laptop_cam)
    else:
        cv2.imshow('Laptop Cam', laptop_cam_off)

    # USB Camera (Switcher key - 2, Record key - R) 
    if has_frame_USB_cam and USB_cam_switcher % 2 == 1:
        cv2.imshow('USB Cam', frame_USB_cam)
        if USB_cam_recording_switcher % 2 == 1:            
            out_USB_cam.write(frame_USB_cam)          
    else:
        cv2.imshow('USB Cam', USB_cam_off)

    key = cv2.waitKey(1)
    if key == ord('1'):
        laptop_cam_switcher += 1
    elif key == ord('2'):
        USB_cam_switcher += 1
    elif key == ord('L') or key == ord('l'):
        laptop_cam_recording_switcher += 1
    elif key == ord('U') or key == ord('u'):
        USB_cam_recording_switcher += 1
    elif key == ord('q'):
        break    

# When everything is done, release the capture
USB_cam_capture.release()
laptop_cam_capture.release()
out_laptop_cam.release()
out_USB_cam.release()
cv2.destroyAllWindows()
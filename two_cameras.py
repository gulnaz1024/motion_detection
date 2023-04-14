import cv2

USB_cam_capture = cv2.VideoCapture(0)
built_in_cam_capture = cv2.VideoCapture(1)

while True:
    # Capture frame-by-frame
    has_frame_USB_cam, frame_USB_cam = USB_cam_capture.read()
    has_frame_built_in_cam, frame_built_in_cam = built_in_cam_capture.read()

    if has_frame_USB_cam:
    # Display the resulting frame
        cv2.imshow('USB Cam', frame_USB_cam)

    if has_frame_built_in_cam:
    # Display the resulting frame
        cv2.imshow('Built-in Cam', frame_built_in_cam)
        
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

# When everything is done, release the capture
USB_cam_capture.release()
built_in_cam_capture.release()
cv2.destroyAllWindows()
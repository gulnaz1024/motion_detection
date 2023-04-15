import cv2

cap = cv2.VideoCapture(0)

# Default resolutions of the frame are obtained.
# Convert the resolutions from float to integer.
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

# Define the codec and create Videowriter object.
# out_avi = cv2.VideoWriter('race_car_out.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 20, (frame_width,frame_height))


out_mp4 = cv2.VideoWriter('test_single_camera.mp4',cv2.VideoWriter_fourcc(*'XVID'), 70, (frame_width, frame_height))


while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        # out_avi.write(frame)
        out_mp4.write(frame)        

        cv2.imshow('Video', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release everything if job is finished
cap.release()
# out_avi.release()
out_mp4.release()
cv2.destroyAllWindows()
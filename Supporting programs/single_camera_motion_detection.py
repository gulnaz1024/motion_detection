import cv2

cap = cv2.VideoCapture(0)

# Create the MOG2 background subtractor object
mog = cv2.createBackgroundSubtractorMOG2()

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Apply background subtraction
    fgmask = mog.apply(gray)

    # Apply morphological operations to reduce noise and fill gaps
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2, 2))
    fgmask2 = cv2.erode(fgmask, kernel, iterations=1)
    fgmask3 = cv2.dilate(fgmask2, kernel, iterations=1)

    contours, hierarchy = cv2.findContours(fgmask3, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        # Ignore small contours
        if cv2.contourArea(contour) < 500:
            continue
        
        # Draw bounding box around contour
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(frame, "Motion Detected", (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
    
    # Another way is just draw contours of detected object
    # cv2.drawContours(frame, contours, -1, (0, 255, 0), 2)
    
    # Display the foreground mask
    cv2.imshow('Video Stream', frame)
    # cv2.imshow('Video Stream2', gray)
    # cv2.imshow('Foreground Mask', fgmask)
    # cv2.imshow('Foreground Mask2', fgmask3)
    if cv2.waitKey(1) == ord('q'):
        break
        
cap.release()
cv2.destroyAllWindows()
# Motion detection on security cameras 🚶 🚴 🚗
by Gimaletdinova Gulnaz (MAT-20)

## 💬 About
Detects motion on any cameras, without connecting additional sensors, by using computer vision.  When motion is detected on any camera, it automatically starts recording on that camera. It is also possible to enable/disable the recording by pressing the button (each camera has its own recording button). The cameras can be turned on/off by pressing a button (each camera has its own power button).

<p align="center">
  <img src="img/demo.gif" width="650" />
</p>

## 🏃 Getting Started

Run the file ***get_fps_of_camera.py*** and check the FPS of your cameras to put these settings in the function ***cv2.VideoWriter***, which define the codec and create Videowriter object.

In my case, the settings were as follows:
```
Laptop camera fps: 28
USB camera fps:    25
```
If you use only one camera run ***main_for_single_camera.py***

## 📃References

- Accessing the Camera: https://youtu.be/Z846tkgl9-U?t=3137
- Using Multiple Cameras with OpenCV: https://youtu.be/jGYNFssXiAQ
- Change camera mode on key pressed: https://youtu.be/Z846tkgl9-U?t=3529
- Read and write images: https://pythonexamples.org/python-opencv-cv2-imwrite-save-image/
- Record video: https://youtu.be/Z846tkgl9-U?t=3309
- Get FPS of cameras: https://learnopencv.com/how-to-find-frame-rate-or-frames-per-second-fps-in-opencv-python-cpp/
- Motion detection 1: https://hackthedeveloper.com/motion-detection-opencv-python/
- Motion detection 2: https://gist.github.com/pknowledge/623515e8ab35f1771ca2186630a13d14
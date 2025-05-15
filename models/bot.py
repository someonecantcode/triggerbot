import cv2
import numpy as np
import pyautogui
import time
from mss import mss
import keyboard

# Adjusted screen region around the crosshair
monitor_size = 100
crosshair_x = 2250
crosshair_y = 1519

monitor = {
    "top": crosshair_y - monitor_size // 2,
    "left": crosshair_x - monitor_size // 2,
    "width": monitor_size,
    "height": monitor_size
}

center_point = (monitor['width'] // 2, monitor['height'] // 2)
sct = mss()

# Kernel for dilating the mask to make contours more solid
kernel = np.ones((5, 5), np.uint8)

print("Universal color triggerbot running at crosshair. Press 'q' to quit.")

def detect_target(frame):
    # Convert image to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Threshold to separate shapes from background
    _, thresh = cv2.threshold(gray, 50, 255, cv2.THRESH_BINARY)

    # Dilate to strengthen shapes
    dilated = cv2.dilate(thresh, kernel, iterations=3)

    # Find contours
    contours, _ = cv2.findContours(dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for c in contours:
        area = cv2.contourArea(c)
        print(area)
        print(cv2.pointPolygonTest(c, center_point, False))
        if area < 50:
            continue
        if cv2.pointPolygonTest(c, center_point, False) > 0:
            return True
    return False


while True:
    if keyboard.is_pressed('q'):
        print("Exited.")
        break

    img = np.array(sct.grab(monitor))
    frame = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)
    cv2.imshow("Frame", frame)
 
    if detect_target(frame):
        pyautogui.click()

    time.sleep(0.5)
    
      # Delay after click check

    # Optional debug view
    # cv2.imshow("Frame", frame)
    # if cv2.waitKey(1) & 0xFF == ord('q'):
    #     break

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
    "height": 2*monitor_size
}

sct = mss()


center_point = (monitor['width'] // 2, monitor['height'] // 2)


def detect_target(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    edges = cv2.Canny(blurred, 50, 150)

    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for c in contours:
        area = cv2.contourArea(c)
        print(area)
        if not (500 < area < 2000):
            continue

        x, y, w, h = cv2.boundingRect(c)
        aspect_ratio = w / float(h)
        if not (0.75 < aspect_ratio < 1.3):
            continue

        dist = cv2.pointPolygonTest(c, center_point, True)
        print(dist)
        if dist > 2:  # Center is well within the contour
            return True, edges
    return False, edges



cv2.namedWindow("Captured Region", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Captured Region", 600, 2*600)
while True:
    if keyboard.is_pressed('q'):
        print("Exited.")
        break

    img = np.array(sct.grab(monitor))
    frame = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)

    detected, dilated = detect_target(frame)

    cv2.imshow("Captured Region", dilated)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


    time.sleep(0.5)
    if detect_target(frame):
        print("fired")
    #     #   pyautogui.click()

cv2.destroyAllWindows()


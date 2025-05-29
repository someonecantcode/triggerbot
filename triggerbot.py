from ultralytics import YOLO
import cv2
import numpy as np
import pyautogui
import torch
from mss import mss
import keyboard

CUDA = torch.cuda.is_available()
device = torch.device("cuda" if CUDA else "cpu")
model = YOLO('models/best.pt', task='detect')
model.to(device=device)

monitor_size = 90
crosshair_x = 2250
crosshair_y = 1519


monitor = {
    "top": crosshair_y - monitor_size // 2,
    "left": crosshair_x - monitor_size // 2,
    "width": monitor_size,
    "height":monitor_size
}
center_point = (monitor['width'] // 2, monitor['height'] // 2)
sct = mss()



def detectCharacter(results):
    for r in results:
        for box in r.boxes:
           # cls_id = int(box.cls[0])
            # if cls_id != 9: # Class id for person
            x1, y1, x2, y2 = box.xyxy[0].tolist()
            # print(x1)
            # print(x2)
            # print(y1)
            # print(y2)
            # print()
            cx, cy = center_point
            if x1 <= cx <= x2 and y1 <= cy <= y2:
                return True
        
                
    return False

# cv2.namedWindow("Captured Region", cv2.WINDOW_NORMAL)
# cv2.resizeWindow("Captured Region", 600, 600)    
print("triggerbot active") 
while True:
    if keyboard.is_pressed('f1'):
        print("Exited.")
        break

    img = np.array(sct.grab(monitor))
    frame = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)
    result = model(source=frame, conf=0.5, verbose=False)
    
    if detectCharacter(result) == True:
        pyautogui.click()

    # cv2.imshow("Captured Region", result[0].plot())
    # if cv2.waitKey(1) & 0xFF == ord('q'):
    #     break

# cv2.destroyAllWindows()
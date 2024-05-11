import pyautogui
import numpy as np
import cv2

def takescreenshot(location):
    
    screenshot = pyautogui.screenshot(region=(location[0][0],location[0][1],location[0][2],location[0][3]))
    return screenshot

def compare2(img1pil, img2pil):
    array1 = np.array(img1pil)
    array2 = np.array(img2pil)

    array1 = cv2.cvtColor(array1, cv2.COLOR_RGB2BGR)
    array2 = cv2.cvtColor(array2, cv2.COLOR_RGB2BGR)

    img1 = cv2.cvtColor(array1, cv2.COLOR_BGR2GRAY)
    img2 = cv2.cvtColor(array2, cv2.COLOR_BGR2GRAY)

    error = mse(img1,img2)
    print(f"SSIM: {error}")
    return True if error < 5 else False

def mse(img1, img2):
   h, w = img1.shape
   diff = cv2.subtract(img1, img2)
   err = np.sum(diff**2)
   mse = err/(float(h*w))
   return mse
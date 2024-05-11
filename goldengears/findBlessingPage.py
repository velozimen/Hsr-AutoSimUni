import pytesseract
from PIL import Image, ImageEnhance, ImageFilter
import pytesseract
import pyautogui
import time


def preprocess_image(image):
    # Convert the image to grayscale
    image = image.convert('L')
    # Enhance the image contrast
    enhancer = ImageEnhance.Contrast(image)
    image = enhancer.enhance(2)
    # Apply sharpening
    image = image.filter(ImageFilter.SHARPEN)
    return image

def readNum(x1,y1,x2,y2):
    screenshot = pyautogui.screenshot(region=(x1, y1, x2-x1, y2-y1))
    screenshot = preprocess_image(screenshot)
    screenshot.save('goldengears\images\preprocessed_area2.png')
    
    #screenshot = Image.open('goldengears\outras imagens\Screenshot_1.png')


    output = (pytesseract.image_to_string(screenshot, config='--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789.'))
    numstr = ''
    for i in output:
        if i.isdigit():
            numstr += i
    num = int(numstr)
    return num
def start():
    x1, y1, x2, y2 = 124, 132, 169, 165  # 
    extracted_number = readNum(x1, y1, x2, y2)
    return(extracted_number)
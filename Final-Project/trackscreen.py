import time
from PIL import ImageGrab  # screenshot
import pyautogui as pg
import pytesseract
from pytesseract import Output
pytesseract.pytesseract.tesseract_cmd = (r"C:\Program Files\Tesseract-OCR\tesseract.exe") # needed for Windows as OS


while True:
    time.sleep(1)
    # screen =  ImageGrab.grab(bbox=(886,1073,1286,1173))  # screenshot
    mouse_pos = pg.position()
    screen = ImageGrab.grab(bbox=(mouse_pos[0],mouse_pos[1],mouse_pos[0]+400,mouse_pos[1]+200))
    cap = screen.convert('L')   # make grayscale

    # screen.show()
    data=pytesseract.image_to_boxes(cap,output_type=Output.DICT)
    try:
        print(''.join(data['char']))
    except Exception as e:
        # print(e)
        pass
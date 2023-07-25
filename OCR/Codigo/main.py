# Optical Character Recognition
import easyocr #character recognition
import cv2 #show / visualize image
from matplotlib import pyplot as plt 
import numpy as np 
import keyboard
import pyautogui
import os
from googletrans import Translator
import pyautogui
from tkinter import *
import time
from win32api import GetSystemMetrics


WIDTH = GetSystemMetrics(0)
HEIGHT = GetSystemMetrics(1)
LINEWIDTH = 1
TRANSCOLOUR = 'gray'

def translate_words(translater,result):
    translated_words = []
    for word in result:
        translated_word = translater.translate(word[2],dest='en')
        # word_position = word[0]
        row = [word[0],word[1],translated_word.text]
        translated_words.append(row)
    return translated_words

def create_canvas(canvas,translated_words):
    canvas.pack()
    canvas.create_rectangle(0, 0, WIDTH, HEIGHT, fill=TRANSCOLOUR, outline=TRANSCOLOUR)
    for detection in translated_words:
        # canvas.create_text(detection[0]+2,detection[1]+2,fill="black",font="Arial 12 bold", text=text)
        valueX = detection[0]+25
        valueY = detection[1]+5
        canvas.create_text(valueX+1,valueY+1,fill="black",font="Arial 12", text=detection[2])
        canvas.create_text(valueX,valueY,fill="yellow",font="Arial 12", text=detection[2])

def create_tk(tk):
    # tk.title()
    tk.bind('<Visibility>', putOnTop)
    tk.focus()
    tk.lift()
    tk.wm_attributes("-topmost", True)
    tk.wm_attributes("-transparentcolor", TRANSCOLOUR)
    tk.attributes('-fullscreen', True)

def putOnTop(event):
    event.widget.unbind('<Visibility>')
    event.widget.update()
    event.widget.lift()
    event.widget.bind('<Visibility>', putOnTop)


def display_words_overlay(translated_words):
    tk = Tk()
    create_tk(tk)
    canvas = Canvas(tk, width=WIDTH, height=HEIGHT, highlightthickness=0)
    create_canvas(canvas,translated_words)
    running = 1
    while running == 1:
        try:
            tk.update()
            time.sleep(0.01)
        except Exception as e:
            running = 0
            print("error %r" % (e))

def onKeyPressed(translater):
    print('Screenshot capturada')
    captureScreenshot()
    result = ocrDetection()
    translated_words = translate_words(translater,result)
    # printWordsOnScreen(translated_words,image_path)
    display_words_overlay(translated_words)

def captureScreenshot():
    sshot = pyautogui.screenshot()
    sshot = cv2.cvtColor(np.array(sshot),cv2.COLOR_RGB2BGR)
    cv2.imwrite('imagetoread.png',sshot) #the screenshot is saved on the same folder as the code, as the name is the same, it overwrites it

def ocrDetection():
    # Read in image
    reader = easyocr.Reader(['ja','en'],recog_network='japanese_g2',gpu=False)
    # Path to the image file
    current_directory = os.getcwd()
    image_path = current_directory+'\imagetoread.png'
    # Use pytesseract to get the OCR data and bounding box information
    result = reader.readtext(image_path, detail=1)
    print('read finished')
    results = []
    # Iterate over each detected text block
    for detection in result:
        text = detection[1]
        row = [detection[0][0][0],detection[0][0][1],text]
        results.append(row)
    return(results)

def main():
    translater = Translator() 
    print('En espera a que se presione F6...\n')
    print('Presione Esc para terminar.')
    keyboard.on_press_key("F6", lambda _: onKeyPressed(translater))
    keyboard.wait("esc")

main()
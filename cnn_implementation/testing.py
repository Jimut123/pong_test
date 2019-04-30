from keras.models import load_model
import numpy as np
import cv2
import time
import pyscreenshot as ImageGrab
import pyautogui


#loading the model
model = load_model('pong.h5')
    
def main():

    for i in list(range(8))[::-1]:
        print(i+1)
        time.sleep(1)

    while(True):
        
            # 640x480 windowed mode
            screen=ImageGrab.grab(bbox=(0,0,800,700))
            screen = cv2.cvtColor(np.float32(screen), cv2.COLOR_BGR2GRAY)
            screen = cv2.resize(screen,(64,64))
            screen = screen[np.newaxis,:,:,np.newaxis]
            screen = np.array(screen)
            
            # model prediction
            y_prob = model.predict(screen)
            prediction = y_prob.argmax(axis=-1)
            
            
            if prediction == 1:
            # up
                 pyautogui.keyUp('down')
                 pyautogui.keyDown('up')
                 print('Up')
            elif prediction == 0:
                 pyautogui.keyUp('down')
                 pyautogui.keyUp('up')
                 print('Nothing')
                 # do nothing
            elif prediction == 2:
                 pyautogui.keyUp('up')
                 #time.sleep(.5)
                 pyautogui.keyDown('down')
                 print('Down')
                 # down
                 

        
main()       

from keras.models import load_model
import numpy as np
import cv2
import time
import pyscreenshot as ImageGrab
import pyautogui
import time
# only up and down, no standing!
#loading the model https://drive.google.com/open?id=1nHKctOD369Et3LIQHch4T9v0mxQ1ojhh
model = load_model('Pong_Fri May  3 08_57_29 2019.h5')
    
def main():

    for i in list(range(5))[::-1]:
        print(i+1)
        time.sleep(1)

    while(True):
        
            # 640x480 windowed mode
            screen=ImageGrab.grab(bbox=(390,290,990,695))
            screen = cv2.cvtColor(np.float32(screen), cv2.COLOR_BGR2GRAY)
            screen = cv2.resize(screen,(64,64))
            #cv2.imshow('screen',screen)
            #cv2.waitKey(0)
            screen = screen[np.newaxis,:,:,np.newaxis]
            screen = np.array(screen)
            
            # model prediction
            y_prob = model.predict(screen)
            prediction = y_prob.argmax(axis=-1)
            
            
            if prediction == 0:
               pyautogui.keyUp('down')
               start = time.time()
               while time.time() - start <= 0.0001:	#0.06 or 0.04
                    pyautogui.keyDown('up')
                    print('Up')
            elif prediction == 1:
               pyautogui.keyUp('up')
               start = time.time()
               while time.time() - start <= 0.0001:
                    pyautogui.keyDown('down')
                    print('Down')
                 

        
main()       

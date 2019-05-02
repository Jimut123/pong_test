import cv2
import pyscreenshot as ImageGrab
import keyboard
import os
import time
import numpy as np


with open('actions.csv', 'w') as csv:

        x = 0
        c = 0
        d = 0
        t = 0
        if not os.path.exists(r'./images'):
            os.mkdir(r'./images')


        for i in list(range(8))[::-1]:
            print(i+1)
            time.sleep(1)

    
        while(True):

            # 640x480 windowed mode
            screen=ImageGrab.grab(bbox=(390,290,990,695))
            screen = cv2.cvtColor(np.float32(screen), cv2.COLOR_BGR2GRAY)
            #cv2.imshow('screen',screen)
            #cv2.waitKey(0)
            screen = cv2.resize(screen, (64,64))
            # resize to something a bit more acceptable for a CNN
            #keys = key_check()
            if keyboard.is_pressed('up arrow'):
                if c < 10000:#10000 denotes the no of images for up action
                    cv2.imwrite('./images/frame_{0}.jpg'.format(x), screen)
                    csv.write('1\n')
                    print('up')
                    x += 1
                    c += 1
            elif keyboard.is_pressed('down arrow'):
                if d < 10000:#10000 denotes the no of images for down action
                    cv2.imwrite('./images/frame_{0}.jpg'.format(x), screen)
                    csv.write('2\n')
                    print('down')
                    x += 1
                    d += 1
            else:
                if t < 10000:#10000 denotes the no of images for nothing action
                    cv2.imwrite('./images/frame_{0}.jpg'.format(x), screen)
                    csv.write('0\n')
                    print('nothing')
                    x += 1
                    t += 1

            print("C = ",c,"/10000","T = ",t,"/10000","D = ",d,"/10000")
            if c == 10000 and t == 10000 and d==10000:
                csv.close()
                cv2.destroyAllWindows()
                break                
        






import cv2
from darkflow.net.build import TFNet
import numpy as np
import time
from tkinter import *
import serial




class gui():

    def __init__(self, master):

        master.wm_title('EYE TRACKER APPLICATION version 2.0')

        labelText1 = Label(master, text='Application info:')
        labelText2 = Label(master, text='Deep learning algorithm used-- Tiny YOLO 2000')
        labelText3 = Label(master, text = 'Model speciality-- Real time object detection with High Frame rate. (Rises upto 40FPS)')
        labelText4 = Label(master, text = 'model threshold-- 0.1')
        labelText5 = Label(master, text = 'tensorflow GPU with 0.8 percentage usage')
        labelText6 = Label(master, text='Application kernel-- ubuntu, debian, raspbian (raspberry pi)')
        runButton = Button(master, text = 'track gaze', command=self.run)

        labelText1.pack()
        labelText2.pack()
        labelText3.pack()
        labelText4.pack()
        labelText5.pack()
        labelText6.pack()
        runButton.pack()

        master.geometry('900x200')
        mainloop()


    def run(self):

        ser = serial.Serial('/dev/ttyACM0', 9600)

        labelList = ['straight_gaze', 'right_gaze', 'left_gaze']
        signalList = []
        noDetectCount = 0


        options = {
            'model': 'cfg/tiny-yolo-voc-4c.cfg',
            'load': 2625,
            'threshold': 0.1,
            'gpu': 0.8
        }

        tfnet = TFNet(options)
        colors = [tuple(255 * np.random.rand(3)) for _ in range(10)]

        capture = cv2.VideoCapture(1)   #make it 0 if not working
        #capture.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
        #capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

        capture.set(cv2.CAP_PROP_FRAME_WIDTH, 250)
        capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 250)

        while True:
            stime = time.time()
            ret, frame = capture.read()
            if ret:
                results = tfnet.return_predict(frame)

                if results == []:

                    noDetectCount = noDetectCount + 1

                    signal = b'1'

                    ser.write(signal)

                    signalList.append(signal)



                else:

                    if results[0]['label'] == labelList[0]:

                        signal = b'2'

                    elif results[0]['label'] == labelList[1]:

                        signal = b'3'

                    else:

                        signal = b'4'

                    signalList.append(signal)

                    ser.write(signal)






                for color, result in zip(colors, results):
                    tl = (result['topleft']['x'], result['topleft']['y'])
                    br = (result['bottomright']['x'], result['bottomright']['y'])
                    label = result['label']
                    confidence = result['confidence']
                    text = '{}: {:.0f}%'.format(label, confidence * 100)
                    frame = cv2.rectangle(frame, tl, br, color, 5)
                    frame = cv2.putText(
                        frame, text, tl, cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 2)
                cv2.imshow('frame', frame)
                print('FPS {:.1f}'.format(1 / (time.time() - stime)))
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        capture.release()
        cv2.destroyAllWindows()



master = Tk()

gui(master)


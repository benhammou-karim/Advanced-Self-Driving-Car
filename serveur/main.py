"""
A Python program that controls a car with an LED and a distance sensor.
Usage:
    python main.py
Author: Imad AHDDAD et Karim BENHAMMOU
"""
from led import Led
from detector import Detector
from car import Car
from motor import Motor
from lineSensor import LineSensor
from detectVide import DetectorEmpty
import atexit
import os
import cv2
from flask import Flask, request, jsonify, Response
# Flask Constructor
app = Flask(__name__)

# led
myLed = Led(ledGpio=18)
# detector
myDetector = Detector(trigGpio=23, echoGpio=24)
# right motor
motor_right = Motor(enableGpio=25, input1Gpio=8, input2Gpio=7)
# left motor
motor_left = Motor(enableGpio=21, input1Gpio=16, input2Gpio=20)
# line sensor
myLineSensor = LineSensor(outGpioRight=22,outGpioLeft=26)
# empty detector
myBlankDetector = DetectorEmpty(trigGpio=17, echoGpio=27)
# car
myCar = Car(led=myLed, detector=myDetector, motor_left=motor_left, motor_right=motor_right,detectorEmpty=myBlankDetector, lineSensor=myLineSensor)
# starts car's thread
myCar.start()

classNames = []
classFile = "/home/pi/Desktop/Various_Innovations/Object_Detection_Files/coco.names"
# retourner les noms des objets contenus dans le fichier assets/coco.names et les stocker dans la list classNames
with open(classFile,"rt") as f:
    classNames = f.read().rstrip("\n").split("\n")
# le fichier qui contient la configuration
configPath = "/home/pi/Desktop/Various_Innovations/Object_Detection_Files/ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt"
# le fichier qui contient le modéle pré-entrainné
weightsPath = "/home/pi/Desktop/Various_Innovations/Object_Detection_Files/frozen_inference_graph.pb"
# création du modéle DNN
net = cv2.dnn_DetectionModel(weightsPath,configPath)  #La dnn_DetectionModel fonction retourne un objet de modèle de détection d'objet DNN.
net.setInputSize(320,320)
net.setInputScale(1.0/ 127.5)
net.setInputMean((127.5, 127.5, 127.5))
net.setInputSwapRB(True)

@app.route('/apiCar/forward', methods=['GET'])
def forwardCar():
    """
        This method makes the car go forward
    """
    if(myCar.isRun):
        myCar.forward()
        myCar.motorDirection = 1
        # response from the server
        return jsonify("car is in forward mode")
    else:
        # response from the server
        return jsonify("run the car first")

@app.route('/apiCar/backward', methods=['GET'])
def backwardCar():
    """
        This method makes the car go backward
    """
    if(myCar.isRun):
        myCar.backward()
        myCar.motorDirection = -1
        # response from the server
        return jsonify("car is in backward mode")
    else:
        # response from the server
        return jsonify("run the car first")

@app.route('/apiCar/stop', methods=['GET'])
def stopCar():
    """
        This method stops the car
    """
    if(myCar.isRun):
        myCar.stopCar()
        myCar.motorDirection = 0
        # response from the server
        return jsonify("car stoped")
    else:
        # response from the server
        return jsonify("run the car first")

@app.route('/apiCar/turnRight', methods=['GET'])
def trunRight():
    """
        This method turns the car to right
    """
    myCar.turnRight()
    myCar.motorDirection = 2
    # response from the server
    return jsonify("car is turned to right")

@app.route('/apiCar/turnLeft', methods=['GET'])
def trunLeft():
    """
        This method turns the car to left
    """
    myCar.turnLetf()
    myCar.motorDirection = 3
    # response from the server
    return jsonify("car is turned to left")

@app.route('/apiCar/speedUp', methods=['GET'])
def speedUpCar():
    """
        This method speeds up the car
    """
    if(myCar.isRun):
        myCar.speedUpCar()
        # response from the server
        return jsonify("car is in speed up mode")
    else:
        # response from the server
        return jsonify("run the car first")

@app.route('/apiCar/slowDown', methods=['GET'])
def slowDownCar():
    """
        This method slows down the car
    """
    if(myCar.isRun):
        myCar.slowDownCar()
        # response from the server
        return jsonify("car is in slow down mode")
    else:
        # response from the server
        return jsonify("run the car first")

@app.route('/apiCar/medium', methods=['GET'])
def setToMedium():
    """
        This method makes the car's speed to medium
    """
    if(myCar.isRun):
        myCar.mediumUpCar()
        # response from the server
        return jsonify("car is in medium mode")
    else:
        # response from the server
        return jsonify("run the car first")

@app.route('/apiCar/shutDown', methods=['GET'])
def shutDown():
    """
        this methods shutDown the car
    """ 
    if(myCar.isRun):
        myCar.stop()
        # response from the server
        return jsonify("car is shutted down")
    else:
        # response from the server
        return jsonify("run the car first")

@app.route('/apiCar/run', methods=['GET'])
def runCar():
    """
        this methods start the car
    """ 
    myCar.startCar()
    # response from the server
    return jsonify("car is started")

# la methode qui detecte les objets et trace les regtangles autour des objets detectés 
def getObjects(img, thres, nms, draw=True, objects=[]):
    classIds, confs, bbox = net.detect(img,confThreshold=thres,nmsThreshold=nms)
    # classIds : les identifiants de classe des objets détectés.
    # confs : les confiances de la détection des objets détectés.
    # bbox : les coordonnées des boîtes englobantes des objets détectés.
    if len(objects) == 0: objects = classNames
    objectInfo =[]
    if len(classIds) != 0:
        for classId, confidence,box in zip(classIds.flatten(),confs.flatten(),bbox):
            className = classNames[classId - 1]
            if className in objects:
                objectInfo.append([box,className])
                if (draw):
                    cv2.rectangle(img,box,color=(0,255,0),thickness=2)
                    cv2.putText(img,classNames[classId-1].upper(),(box[0]+10,box[1]+30),
                    cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)
                    cv2.putText(img,str(round(confidence*100,2)),(box[0]+200,box[1]+30),
                    cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)

    return img,objectInfo


def gen_frames():
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    while True:
        success, frame = cap.read()
        result, objectInfo = getObjects(frame,0.45,0.2)
        # afficher l'image dans la fenêtre graphique output
        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
    
@app.route('/apiCar/video_feed')
def video_feed():
    return Response(gen_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

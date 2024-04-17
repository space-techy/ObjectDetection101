from ultralytics import YOLO
import cv2
import os

img_path = os.path.abspath("/ObjectDetect/OBJECTDETECTION101/Images/test2.jpg")

model = YOLO("../yolo-models/yolov8n.pt")
results = model(img_path, show = True)
cv2.waitKey(0)
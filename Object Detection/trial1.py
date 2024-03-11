from ultralytics import YOLO
import cv2

model = YOLO("yolov8n.pt")
results = model("Images/test1.jpg", show = True)
cv2.waitKey(0)
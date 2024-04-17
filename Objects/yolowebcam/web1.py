from ultralytics import YOLO
import cvzone
import cv2


model = YOLO("../yolo-models/yolov8n.pt")
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 420)


while True:
    success, img = cap.read()
    results = model(img)
    for r in results:
        boxes = r.boxes
        for box in  boxes:
            x1,y1,x2,y2 = box.xyxy[0]
            x1,y1,x2,y2 = int(x1),int(y1),int(x2),int(y2)
            cv2.rectangle(img, (x1,y1), (x2,y2), (255,0,255),3)
    cv2.imshow("Image", img)
    cv2.waitKey(1)
import tkinter as tk
from tkinter import filedialog
from ultralytics import YOLO
import cv2
import os

def process_image():
    if use_camera.get():
        capture_video()
    else:
        img_path = selected_file.get()
        model = YOLO("../yolo-models/yolov8n.pt")
        results = model(img_path, show=True)
        cv2.waitKey(0)

def browse_file():
    file_path = filedialog.askopenfilename()
    selected_file.set(file_path)

def toggle_camera():
    if use_camera.get():
        browse_button.config(state=tk.DISABLED)
    else:
        browse_button.config(state=tk.NORMAL)

def capture_video():
    cap = cv2.VideoCapture(0)
    model = YOLO("../yolo-models/yolov8n.pt")
    while True:
        ret, frame = cap.read()
        results = model(frame, show=True)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

# Create a Tkinter window
window = tk.Tk()
window.title("Object Detection")

# Create a label for file selection
file_label = tk.Label(window, text="Select an image:")
file_label.pack()

# Create a variable to hold the selected file path
selected_file = tk.StringVar()

# Create a button to browse for a file
browse_button = tk.Button(window, text="Browse", command=browse_file)
browse_button.pack()

# Create a checkbox to toggle camera mode
use_camera = tk.BooleanVar()
camera_checkbox = tk.Checkbutton(window, text="Use Camera", variable=use_camera, command=toggle_camera)
camera_checkbox.pack()

# Create a button to process the selected image
process_button = tk.Button(window, text="Process Image", command=process_image)
process_button.pack()


def objectImage():
    # Start the Tkinter event loop
    window.mainloop()

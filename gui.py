import cv2
import mediapipe as mp
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.graphics import Color, Rectangle
from Objects.yolowebcam.web1 import webcam
from Objects.ObjectDetection.trial1 import objectImage
from controller import Controller



class ObjectSystem(App):
    def build(self):
        root = BoxLayout(orientation='vertical', spacing=10, padding=20)

        # Set the background color to white
        with root.canvas.before:
            Color(1, 1, 1, 1)  # White color
            self.rect = Rectangle(size=root.size, pos=root.pos)

        # Bind the size and position of the rectangle to the root layout
        def update_rect(instance, value):
            self.rect.pos = instance.pos
            self.rect.size = instance.size

        root.bind(pos=update_rect, size=update_rect)

        # Object Detection button
        button1 = Button(text='Object Detection', background_color=(0.5, 0.7, 0.3, 1), size_hint=(0.6, 0.15), pos_hint={'center_x': 0.5, 'center_y': 0.7})
        button1.bind(on_press=self.object_detection)
        root.add_widget(button1)

        # Object Classification button
        button2 = Button(text='Object Classification', background_color=(0.5, 0.7, 0.3, 1), size_hint=(0.6, 0.15), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        button2.bind(on_press=self.object_classification)
        root.add_widget(button2)

        # Cursor Control button
        button3 = Button(text='Cursor Control', background_color=(0.5, 0.7, 0.3, 1), size_hint=(0.6, 0.15), pos_hint={'center_x': 0.5, 'center_y': 0.3})
        button3.bind(on_press=self.cursor_control)
        root.add_widget(button3)

        return root

    def object_detection(self, instance):
        webcam()

    def object_classification(self, instance):
        objectImage()

    def cursor_control(self, instance):
        WINDOW_WIDTH = 720
        WINDOW_HEIGHT = 720
        cap = cv2.VideoCapture(0)
        mpHands = mp.solutions.hands
        hands = mpHands.Hands()
        mpDraw = mp.solutions.drawing_utils
        while True:
            success, img = cap.read()
            img = cv2.flip(img, 1)
            img = cv2.resize(img, (WINDOW_WIDTH, WINDOW_HEIGHT))
            imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            results = hands.process(imgRGB)

            if results.multi_hand_landmarks:
                Controller.hand_Landmarks = results.multi_hand_landmarks[0]
                mpDraw.draw_landmarks(img, Controller.hand_Landmarks, mpHands.HAND_CONNECTIONS)
                
                Controller.update_fingers_status()
                Controller.cursor_moving()
                Controller.detect_scrolling()
                Controller.detect_zoomming()
                Controller.detect_clicking()
                Controller.detect_dragging()

            cv2.imshow('Hand Tracker', img)
            if cv2.waitKey(5) & 0xff == 27:
                break

if __name__ == '__main__':
    ObjectSystem().run()
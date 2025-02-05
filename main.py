import cv2
import cvzone
import threading
import tkinter as tk
from tkinter import Label, Button
from ultralytics import YOLO
import pytesseract
import numpy as np
from fuzzywuzzy import process #I have installed for brandmatching
from PIL import Image, ImageTk

#It will also get automatic download if not present by running the python script
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Loading my Yolo Model, gets automatic download if not present by running the python script
model = YOLO("./Yolo-Weights/yolov8l.pt")


bottle_parts = ["Cap", "Neck", "Body", "Label", "Base", "Deformity"]

known_brands = ["Aquafina", "Bisleri", "Kinley", "Evian", "Nestle", "Himalayan", "Smartwater", "Dasani", "Voss", "Perrier", "Dukes", "Railneer"]

cap = None
running = False


def process_video():
    global cap, running

    cap = cv2.VideoCapture(0)
    cap.set(3, 1280)
    cap.set(4, 720)

    while running:
        success, img = cap.read()
        if not success:
            break
        results = model(img, stream=True)

        for r in results:
            for box in r.boxes:
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                w, h = x2 - x1, y2 - y1
                conf = round(box.conf[0].item(), 2)
                cls = int(box.cls[0]) if len(box.cls) > 0 else -1
                if cls == 39:
                    cvzone.cornerRect(img, (x1, y1, w, h), colorR=(255, 0, 0))

                   
                    part_height = h // 6
                    for i, part in enumerate(bottle_parts):
                        y_part = y1 + i * part_height
                        cvzone.putTextRect(img, part, (x1 + 5, y_part + 10), scale=1, thickness=2, colorR=(0, 255, 0))

    
                    label_y1 = y1 + (h // 2) - part_height
                    label_y2 = label_y1 + part_height
                    label_roi = img[label_y1:label_y2, x1:x2]

                    gray_label = cv2.cvtColor(label_roi, cv2.COLOR_BGR2GRAY)
                    gray_label = cv2.GaussianBlur(gray_label, (5,5), 0)
                    gray_label = cv2.threshold(gray_label, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

                    extracted_text = pytesseract.image_to_string(gray_label, config="--psm 6").strip()
                    if extracted_text:
                        best_match, score = process.extractOne(extracted_text, known_brands)
                        if score > 70:
                            cvzone.putTextRect(img, f'Brand: {best_match}', (x1, label_y1 - 10), scale=1.5, thickness=2, colorR=(0, 165, 255))

       
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(img)
        img = ImageTk.PhotoImage(img)


        video_label.config(image=img)
        video_label.image = img

    cap.release()


def start_video():
    global running
    if not running:
        running = True
        threading.Thread(target=process_video, daemon=True).start()


def stop_video():
    global running
    running = False

root = tk.Tk()
root.title("Bottle Detection")
root.geometry("1300x750")

video_label = Label(root)
video_label.pack()

start_button = Button(root, text="Start", command=start_video, font=("Arial", 14), bg="green", fg="white")
start_button.pack(pady=10)

stop_button = Button(root, text="Stop", command=stop_video, font=("Arial", 14), bg="red", fg="white")
stop_button.pack(pady=10)

root.mainloop()

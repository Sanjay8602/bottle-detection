Bottle Detection System
This project is a Bottle Detection System that uses a pre-trained YOLOv8 model to detect and label various parts of a bottle in real-time from a webcam feed. The system is capable of detecting bottles, recognizing text on the bottle label using OCR (Optical Character Recognition), and matching the detected brand with a list of known brands.

Key Features:
Real-time bottle detection using YOLOv8.
Labeling parts of the bottle: Cap, Neck, Body, Label, Base, and Deformity.
Brand recognition using Tesseract OCR and fuzzy matching with a predefined list of known bottle brands.
User-friendly GUI built using Tkinter.
Technologies Used:
YOLOv8 (Ultralytics) for object detection.
Tesseract OCR for Optical Character Recognition.
FuzzyWuzzy for text matching and recognition.
OpenCV for video processing and displaying images.
Tkinter for GUI creation.
Installation Instructions
Install Python: Ensure you have Python 3.7+ installed on your system.

Install Required Packages: You need to install several Python packages. You can do this by running the following command:

bash
Copy
Edit
pip install opencv-python cvzone ultralytics pytesseract fuzzywuzzy pillow
You may also need to install the tesseract executable. For Windows users, you can download it from here. After installation, make sure to add the path to the executable in the code:

python
Copy
Edit
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
Download YOLO Model Weights: Download the YOLOv8 model weights from here or use the one you have. Make sure to place it in the project directory under ./Yolo-Weights/yolov8l.pt.

Download or Clone the Project: You can either download or clone this repository to your local machine.

bash
Copy
Edit
git clone <repository_url>
Running the Project
Start the GUI Application: To run the application, simply run the Python script:

bash
Copy
Edit
python bottle_detection.py
Using the GUI:

When you launch the program, a window with a "Start" button will appear.
Click "Start" to begin video capture and bottle detection.
The webcam feed will display, and the program will start detecting bottles and label them with their respective parts.
The OCR will extract text from the bottle label, and the system will try to match it to known bottle brands.
The "Stop" button will halt the video feed and processing.
Dependencies: Ensure you have all dependencies installed as mentioned above. If any additional issues arise, please consult the respective documentation for troubleshooting.


Used Model:
Ultralytics YOLO: For providing the pre-trained YOLOv8 model for object detection.
Tesseract OCR: For the OCR engine to extract text from the bottle labels.
FuzzyWuzzy: For the fuzzy matching algorithm to match OCR output with known brands.

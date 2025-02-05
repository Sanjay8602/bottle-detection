Bottle Detection System
Welcome to the Bottle Detection System! This project uses a webcam to detect bottles, label different parts of the bottle (like the cap, neck, body, and label), and even recognize the brand name on the bottle through text extracted from the label. It’s powered by AI and Optical Character Recognition (OCR), making it capable of identifying and labeling bottles in real-time! (but it is not that perfect)


Bottle Detection: The system identifies bottles in the video feed from webcam.
Part Labeling: It labels different parts of the bottle, such as the cap, neck, body, label, and base.
Brand Recognition: Using OCR, it extracts text from the label and tries to match it to a list of known bottle brands like Aquafina, Bisleri, and more.
Technologies Used:
YOLOv8: This is the AI model used to detect bottles in the video feed.
Tesseract OCR: This tool reads the text on the bottle label.
FuzzyWuzzy: It matches the text from the label to known bottle brands.
OpenCV: Used to handle the video feed and display images.
Tkinter: This is the graphical interface (GUI) that you interact with.
Getting Started
To run this system, you’ll need to set up a few things on your computer. 

1. Install Python
First, make sure you have Python 3.7+ installed on your computer. If not, you can download it from python.org.

2. Install Dependencies
You’ll need to install some Python packages. Open your command line or terminal and run this command:

bash
Copy
Edit
pip install -r requirements.txt
3. Install Tesseract OCR
Tesseract is the tool that reads the text on the bottle labels. If you're on Windows, you can download it from this link. After installing it, make sure you point the program to the correct path in the code. For example:

python
Copy
Edit
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
If you're on macOS or Linux, you can install Tesseract via a package manager (brew install tesseract on macOS, or apt-get install tesseract on Ubuntu).

4. Download YOLO Model Weights
You also need to download a pre-trained YOLOv8 model for detecting bottles. You can get it from here. Download the yolov8l.pt file and place it in a folder called Yolo-Weights inside your project directory.

Running the Project
Once everything is set up, follow these steps:

1. Launch the Program
To run the system, simply run the Python script. Open a terminal, navigate to the folder containing the project, and type:

bash
Copy
Edit
python bottle_detection.py

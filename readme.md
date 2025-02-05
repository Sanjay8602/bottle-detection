#Bottle Detection System
Welcome to the Bottle Detection System! This project uses a webcam to detect bottles, label different parts of the bottle (like the cap, neck, body, and label), and even recognize the brand name on the bottle through text extracted from the label. It’s powered by AI and Optical Character Recognition (OCR), making it capable of identifying and labeling bottles in real-time! (but it is not that perfect)


Bottle Detection: The system identifies bottles in the video feed from webcam.

Part Labeling: It labels different parts of the bottle, such as the cap, neck, body, label, and base.

Brand Recognition: Using OCR, it extracts text from the label and tries to match it to a list of known bottle brands like Aquafina, Bisleri, and more.

##Technologies Used:
1. YOLOv8: This is the AI model used to detect bottles in the video feed.
2. Tesseract OCR: This tool reads the text on the bottle label.
3. FuzzyWuzzy: It matches the text from the label to known bottle brands.
4. OpenCV: Used to handle the video feed and display images.
5. Tkinter: This is the graphical interface (GUI) that you interact with.

##Getting Started
1. Clone Repo:
```commandline 
git clone https://github.com/Sanjay8602/bottle-detection.git
```
2. Install Dependencies:
```commandline 
pip install -r requirements.txt
```
3. Running the app on streamlit Locally: 
```commandline 
python main.py
```

3. Install Tesseract OCR
Tesseract is the tool that reads the text on the bottle labels. If you're on Windows, you can download it from this link. After installing it, make sure you point the program to the correct path in the code.

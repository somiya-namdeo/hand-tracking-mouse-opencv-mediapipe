# Virtual Mouse using Hand Tracking

## 1. Introduction

This project implements a real-time virtual mouse system using computer vision techniques. It allows users to control the mouse cursor and perform actions such as clicking and scrolling using hand gestures captured through a webcam, eliminating the need for a physical mouse.

---

## 2. Problem Statement

Traditional input devices such as a mouse and keyboard require physical interaction, which may not be suitable in all environments. In situations requiring touchless interaction (such as healthcare settings, public systems, or accessibility scenarios), an alternative interaction method is needed.

This project provides a contactless human-computer interaction system using hand gesture recognition.

---

## 3. Objectives

- To design a touchless cursor control system  
- To implement real-time hand tracking using computer vision  
- To recognize gestures for mouse actions (click, scroll)  
- To improve usability through smoothing and stability  

---

## 4. Features

- Cursor movement using index finger tracking  
- Left-click using thumb and index finger pinch  
- Right-click using thumb and middle finger gesture  
- Scroll functionality using index and middle finger  
- Smooth cursor movement to reduce jitter  
- Real-time performance with FPS display  

---

## 5. Tech Stack

- Python  
- OpenCV (video capture and image processing)  
- MediaPipe (hand landmark detection)  
- PyAutoGUI (mouse control automation)  
- NumPy and Math (gesture calculations)  

---

## 6. System Requirements

- Python 3.10 or 3.11  
- Webcam  
- Operating System: Windows / Linux / macOS  

---

## 7. Installation

### Clone the Repository

```bash
git clone https://github.com/somiya-namdeo/hand-tracking-mouse-opencv-mediapipe.git
cd hand-tracking-mouse-opencv-mediapipe
```
# Create Virtual Enviornment
```bash
python -m venv venv
venv\Scripts\activate   # For Windows
```
# Install Dependencies
```bash
pip install -r requirements.txt
8. Usage
```

# Run the application:
```bash
python main.py
```
Press ESC to exit the application.

## 9.Controls

| Gesture                | Description                          | Action        |
|-----------------------|--------------------------------------|--------------|
| Index Finger          | Move index finger in air             | Move Cursor  |
| Thumb + Index Finger  | Bring thumb and index finger close   | Left Click   |
| Thumb + Middle Finger | Bring thumb and middle finger close  | Right Click  |
| Index + Middle Finger | Move both fingers up/down together   | Scroll       |

# 10. Methodology

The system uses MediaPipe Hands to detect 21 hand landmarks in real time. The position of the index finger is mapped from camera coordinates to screen coordinates to control cursor movement.

Gesture recognition is implemented using:

Euclidean distance between finger landmarks
Relative positioning of fingers

A smoothing algorithm is applied to reduce cursor jitter and improve user experience.

 # 11. Results
Accurate real-time hand tracking
Smooth cursor movement
Reliable gesture-based interaction
Responsive system performance

# 12. Use Cases
Touchless human-computer interaction
Assistive technology for physically challenged users
Smart environments and IoT systems
Interactive applications and AI interfaces

# 13. Future Scope
Drag-and-drop functionality
Double-click gesture
Multi-hand support
Gesture-based system controls (volume, brightness)
GUI-based customization

# 14. Project Structure
hand-tracking-mouse-opencv-mediapipe/
│
├── main.py
├── requirements.txt
├── README.md
└── venv/

# 15. Acknowledgements
MediaPipe by Google
OpenCV Community

# Author 
Somiya Namdeo
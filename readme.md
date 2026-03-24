# 🖱️ Virtual Mouse using Hand Tracking

A real-time **gesture-controlled virtual mouse system** built using **Computer Vision and AI**, enabling users to control their system cursor without physical contact using just hand gestures captured via a webcam.

---

## 🚀 Features

* 🖐️ **Cursor Movement** — Control mouse pointer using index finger
* 👆 **Click Action** — Perform left click using thumb + index pinch
* ✌️ **Scroll Control** — Scroll up/down using index + middle finger gesture
* 🎯 **Smooth Tracking** — Reduced jitter using motion smoothing
* ⚡ **Real-Time Performance** — Fast and responsive gesture detection

---

## 🛠️ Tech Stack

* **Python**
* **OpenCV** – Video capture and image processing
* **MediaPipe (Tasks API)** – Hand landmark detection
* **PyAutoGUI** – Mouse automation
* **NumPy & Math** – Distance and coordinate calculations

---

## 📦 Installation

### 1️⃣ Clone Repository

```bash
git clone https://github.com/somiya-namdeo/hand-tracking-mouse-opencv-mediapipe.git
cd virtual-mouse
```

### 2️⃣ Create Virtual Environment (Recommended)

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

> If `requirements.txt` is not available:

```bash
pip install opencv-python mediapipe pyautogui numpy
```

---

## ⚠️ Important Note

👉 **MediaPipe is NOT fully compatible with Python 3.12**

✔️ Use:

```bash
Python 3.10 or 3.11
```

---

## 📥 Download Required Model

Download the MediaPipe model file:

```
hand_landmarker.task
```

Place it inside the project directory:

```
virtual-mouse/
```

---

## ▶️ Usage

Run the application:

```bash
python main.py
```

Press **ESC** to exit.

---

## 🎮 Controls

| Gesture           | Action      |
| ----------------- | ----------- |
| ☝️ Index Finger   | Move Cursor |
| 🤏 Thumb + Index  | Left Click  |
| ✌️ Index + Middle | Scroll      |

---

## 📁 Project Structure

```
virtual-mouse/
│
├── main.py
├── hand_landmarker.task
├── requirements.txt
└── README.md
```

---

## 💡 Use Cases

* Touchless Human-Computer Interaction
* Assistive Technology for Accessibility
* Smart Home / IoT Control
* Interactive AI Systems
* Post-pandemic contactless interfaces

---

## 🔮 Future Improvements

* Right-click and double-click gestures
* Drag-and-drop functionality
* Multi-hand support
* Gesture-based volume/brightness control
* GUI for customization

---

## 🙌 Acknowledgements

* Google **MediaPipe**
* OpenCV Community

---

## ⭐ If you found this useful, consider giving it a star!

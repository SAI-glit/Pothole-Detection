# 🕳️ Pothole Detection System

A web application that detects potholes in road images using **YOLOv8** and **Flask**.

Upload a road image → YOLOv8 model runs inference → bounding boxes drawn around potholes → pothole count displayed on screen.

---

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| Python | Core language |
| YOLOv8 (Ultralytics) | Object detection model |
| Flask | Web framework |
| OpenCV | Image processing & drawing bounding boxes |
| HTML/CSS | Frontend UI with glassmorphism design |

---

## ⚙️ Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/SAI-glit/pothole-detection.git
cd pothole-detection
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Download model weights
Download `best.pt` from the link below and place it in the **root folder** of the project:

🔗 [Download best.pt](https://drive.google.com/file/d/16ysT5eL1n5dasKiG-djOlmJhMMdR7dRC/view?usp=drive_link)

Your folder should look like this:
```
pothole-detection/
├── best.pt          ← place here
├── app.py
├── requirements.txt
└── ...
```

### 4. Run the app
```bash
python app.py
```

Open your browser and go to: **http://127.0.0.1:5000**

---

## 🚀 How It Works

1. User uploads a road image through the web interface
2. Flask receives the image and passes it to the YOLOv8 model
3. Model detects potholes and returns bounding box coordinates
4. OpenCV draws green bounding boxes and labels on the image
5. Processed image and pothole count are displayed to the user

---

## 📁 Project Structure

```
pothole-detection/
├── app.py                  # Main Flask app + YOLOv8 inference logic
├── test_flask.py           # Automated test script for the Flask API
├── requirements.txt        # Python dependencies
├── .gitignore              # Files excluded from Git
├── templates/
│   └── index.html          # Frontend HTML template
└── static/
    └── style.css           # Animated glassmorphism UI styles
```

---

## 🧪 Testing

With the app running, you can run the automated test:
```bash
python test_flask.py
```
This sends a dummy image to the Flask API and checks the response.

---

## 📌 Notes

- Model weights (`best.pt`) are not included in this repo due to file size — download from the link above
- Trained on road/pothole dataset using YOLOv8n architecture
- Built as a 2nd year AI/ML project

---

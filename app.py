import os
import cv2
from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
from ultralytics import YOLO

app = Flask(__name__)

# Configuration
UPLOAD_FOLDER = 'static/uploads'
MODEL_PATH = 'best.pt'

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

model = None
try:
    model = YOLO(MODEL_PATH)
except Exception as e:
    print(f"Warning: Model not found. Place '{MODEL_PATH}' in the root directory. Error: {e}")

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)

        if file:
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)

            img = cv2.imread(filepath)

            if model is None:
                return f"Error: YOLO model not loaded. Place '{MODEL_PATH}' in the root directory.", 500

            # Run YOLOv8 inference
            results = model(img)

            pothole_count = 0

            # Draw bounding boxes on detected potholes
            for result in results:
                boxes = result.boxes
                for box in boxes:
                    pothole_count += 1
                    x1, y1, x2, y2 = map(int, box.xyxy[0])
                    cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 4)
                    cv2.putText(img, 'Pothole', (x1, y1 - 10),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

            # Save processed image
            output_filename = 'result_' + filename
            output_filepath = os.path.join(app.config['UPLOAD_FOLDER'], output_filename)
            cv2.imwrite(output_filepath, img)

            return render_template('index.html',
                                   original_image=filename,
                                   result_image=output_filename,
                                   pothole_count=pothole_count)

    return render_template('index.html', original_image=None, result_image=None, pothole_count=None)

if __name__ == '__main__':
    app.run(debug=True)

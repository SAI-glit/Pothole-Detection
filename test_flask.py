import requests
import numpy as np
import cv2

# Create a small dummy test image
with open('test_image.jpg', 'wb') as f:
    img = np.zeros((100, 100, 3), dtype=np.uint8)
    cv2.rectangle(img, (10, 10), (50, 50), (255, 0, 0), -1)
    ret, buf = cv2.imencode(".jpg", img)
    f.write(buf)

url = 'http://127.0.0.1:5000/'
files = {'file': open('test_image.jpg', 'rb')}

response = requests.post(url, files=files)
print("Status Code:", response.status_code)

if response.status_code == 500:
    print(response.text)
else:
    print("Success. Response length:", len(response.text))
    if 'Traceback' in response.text or 'Error' in response.text:
        print("Error text found in HTML response.")
    else:
        print("No errors detected.")

from flask import Flask, Response, render_template_string, redirect
from picamera2 import Picamera2
import cv2
import time

# Initialize Flask
app = Flask(__name__)

# Initialize the camera
picam2 = Picamera2()
picam2.preview_configuration.main.size = (640, 480) 
picam2.preview_configuration.main.format = "RGB888" 
picam2.configure("preview")
picam2.start()

def generate_frames():
    while True:
        frame = picam2.capture_array()
        _, buffer = cv2.imencode('.jpg', frame)  # Convert to JPEG format
        frame_bytes = buffer.tobytes()
        yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')
        time.sleep(0.05)  # Frame rate? 

# Route to start video stream
@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

# "design" the webpage
@app.route('/')
def index():
    return """<html>
                <head><title>Raspberry Pi Video Stream</title></head>
                <body>
                    <h1>Raspberry Pi Video Stream</h1>
                    <img src="/video_feed" width="640" height="480">
                </body>
              </html>"""

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
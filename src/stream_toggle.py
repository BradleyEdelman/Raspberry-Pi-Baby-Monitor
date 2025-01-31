from flask import Flask, Response, render_template_string
from picamera2 import Picamera2
import cv2
import time

# Initialize Flask app
app = Flask(__name__)

# Initialize the camera (moved initialization inside routes to prevent multiple initializations)
picam2 = None

# Camera streaming control variables
camera_streaming = False

# Camera thread function
def generate_frames():
    while camera_streaming:
        frame = picam2.capture_array()
        _, buffer = cv2.imencode('.jpg', frame)  # Convert  to JPEG format
        frame_bytes = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')
        time.sleep(0.05)  # Adjust frame rate

# Route to start or stop the stream
@app.route('/toggle_stream')
def toggle_stream():
    global camera_streaming, picam2
    
    if camera_streaming:
        # Start the stream only if it's currently stopped
        if picam2 and picam2.is_running():
            return "Stream is already running"
        else:
            picam2 = Picamera2()
            picam2.preview_configuration.main.size = (640, 480)  # resolution
            picam2.preview_configuration.main.format = "RGB888"  # format
            picam2.configure("preview")
            picam2.start()
            return "Stream started"
    else:
        # Stop the stream only if it's currently started
        if not picam2 or not picam2.is_running():
            return "Stream is already stopped"
        else:
            picam2.stop()

# Route to start video stream
@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

# "design" the main page (w/ buttons)
@app.route('/')
def index():
    return render_template_string(""" 
        <html>
            <head><title>Raspberry Pi Video Stream</title></head>
            <body>
                <h1>Raspberry Pi Video Stream</h1>
                <img src="/video_feed" width="640" height="480">
                <h3>Camera Stream Control</h3>
                <button onclick="window.location.href='/toggle_stream'">Start/Stop Stream</button>
            </body>
        </html>
    """)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

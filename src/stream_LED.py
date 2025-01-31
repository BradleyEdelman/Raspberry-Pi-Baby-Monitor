from flask import Flask, Response, render_template_string
from picamera2 import Picamera2
import cv2
import time
import threading

# Initialize Flask app
app = Flask(__name__)

# Initialize the camera
picam2 = Picamera2()
picam2.preview_configuration.main.size = (640, 480)  # resolution
picam2.preview_configuration.main.format = "RGB888"  # format
picam2.configure("preview")

# Camera streaming control variables
camera_streaming = False
led_state = "auto"  # "auto", "on", "off"

# Camera thread function
def generate_frames():
    while camera_streaming:
        frame = picam2.capture_array()
        _, buffer = cv2.imencode('.jpg', frame)  # Convert  to JPEG format
        frame_bytes = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')
        time.sleep(0.05)  # Adjust frame rate

# Route to start video stream
@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

# Route to control LED state
@app.route('/set_led/<state>')
def set_led(state):
    global led_state
    if state in ["auto", "on", "off"]:
        led_state = state
        # TO DO: Control LED here
        return f"LED state set to {state}"
    return "Invalid LED state"

# Route to start or stop the stream
@app.route('/toggle_stream')
def toggle_stream():
    global camera_streaming
    if camera_streaming:
        camera_streaming = False
        picam2.stop()
        return "Stream stopped"
    else:
        camera_streaming = True
        picam2.start()
        return "Stream started"

# "design" the main page (w/ buttons)
@app.route('/')
def index():
    return render_template_string("""
        <html>
            <head><title>Raspberry Pi Video Stream</title></head>
            <body>
                <h1>Raspberry Pi Video Stream</h1>
                <img src="/video_feed" width="640" height="480">
                
                <h3>LED Control</h3>
                <button onclick="window.location.href='/set_led/auto'">Auto LED</button>
                <button onclick="window.location.href='/set_led/on'">LED On</button>
                <button onclick="window.location.href='/set_led/off'">LED Off</button>

                <h3>Camera Stream Control</h3>
                <button onclick="window.location.href='/toggle_stream'">Start/Stop Stream</button>
            </body>
        </html>
    """)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

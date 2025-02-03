from flask import Flask, Response, render_template_string, redirect
from picamera2 import Picamera2
import cv2
import time

# Initialize Flask
app = Flask(__name__)

# Turn on camera streaming
camera_streaming = True

# Initialize the camera
picam2 = Picamera2()
picam2.preview_configuration.main.size = (640, 480) 
picam2.preview_configuration.main.format = "RGB888" 
picam2.configure("preview")
picam2.start()

# Initialize LED state
led_state = "auto"  # Options: "auto", "on", "off"

def generate_frames():
    while camera_streaming:
        frame = picam2.capture_array()
        _, buffer = cv2.imencode('.jpg', frame)  # Convert to JPEG format
        frame_bytes = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')
        time.sleep(0.05)  # Frame rate? 

# Route to start or stop the stream
@app.route('/toggle_stream')
def toggle_stream():
    global camera_streaming
    camera_streaming = not camera_streaming
    return redirect('/') # Send back to main page

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
    return redirect('/') # Send back to main page

# "design" the webpage
@app.route('/')
@app.route('/')
def index():
    return render_template_string("""
        <html>
            <head>
                <title>Raspberry Pi Video Stream</title>
                <style>
                    .led-button {
                        padding: 10px 20px;
                        font-size: 16px;
                        border: none;
                        cursor: pointer;
                        margin: 5px;
                    }
                    .active { background-color: green; color: white; }
                    .inactive { background-color: lightgray; color: black; }
                </style>
            </head>
            <body>
                <h1>Raspberry Pi Video Stream</h1>
                <img src="/video_feed" width="640" height="480">
                
                <h3>LED Control</h3>
                <button class="led-button {% if led_state == 'auto' %}active{% else %}inactive{% endif %}" 
                        onclick="window.location.href='/set_led/auto'">Auto LED</button>
                
                <button class="led-button {% if led_state == 'on' %}active{% else %}inactive{% endif %}" 
                        onclick="window.location.href='/set_led/on'">LED On</button>
                
                <button class="led-button {% if led_state == 'off' %}active{% else %}inactive{% endif %}" 
                        onclick="window.location.href='/set_led/off'">LED Off</button>

                <h3>Camera Stream Control</h3>
                <button onclick="window.location.href='/toggle_stream'">Start/Stop Stream</button>
            </body>
        </html>
    """, led_state=led_state)  # <-- Pass `led_state` explicitly


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)

from flask import Flask, Response, render_template_string
from picamera2 import Picamera2
import cv2
import time

# Initialize Flask app
app = Flask(__name__)

# Camera streaming control variables
camera_streaming = True

# Initialize the camera
picam2 = Picamera2()
picam2.preview_configuration.main.size = (640, 480)  # resolution
picam2.preview_configuration.main.format = "RGB888"  # format
picam2.configure("preview")
picam2.start()

def generate_frames():
    while camera_streaming:
        frame = picam2.capture_array()
        _, buffer = cv2.imencode('.jpg', frame)  # Convert to JPEG format
        frame_bytes = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')
        time.sleep(0.05)  # Adjust frame rate here

# Route to start or stop the stream
@app.route('/toggle_stream')
def toggle_stream():
    global camera_streaming
    camera_streaming = not camera_streaming
    return "Stream " + ("started" if camera_streaming else "stopped")

# Route to start video stream
@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

# "design" the main page (w/ buttons)
@app.route('/')
def index():
    return render_template_string("""
        <html>
            <head>
                <title>Raspberry Pi Video Stream</title>
                <script>
                    function toggleStream() {
                        fetch('/toggle_stream', {
                            method: 'GET',
                        })
                        .then(response => response.text())
                        .then(text => {
                            alert(text);  // Display the response from the server (Stream started/stopped)
                        })
                        .catch(error => {
                            console.error('Error:', error);
                        });
                    }
                </script>
            </head>
            <body>
                <h1>Raspberry Pi Video Stream</h1>
                <img src="/video_feed" width="640" height="480">
                <h3>Camera Stream Control</h3>
                <button onclick="toggleStream()">Start/Stop Stream</button>
            </body>
        </html>
    """)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)

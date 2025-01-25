from flask import Flask, render_template, Response
import subprocess
import time

app = Flask(__name__)

def gen_frames():
    while True:
        # Capture a still image using libcamera-jpeg
        # Using subprocess to call libcamera-jpeg and save it as 'frame.jpg'
        subprocess.run(["libcamera-jpeg", "-o", "frame.jpg"])

        # Read the saved image
        with open("frame.jpg", "rb") as f:
            frame = f.read()

        # Yield each frame to the client (this is the streaming part)
        yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video')
def video():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

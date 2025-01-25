from flask import Flask, render_template, Response
import subprocess
import time

app = Flask(__name__)

def gen_frames():
    # Start libcamera-vid in MJPEG mode and pipe it into ffmpeg
    process = subprocess.Popen(
        ["libcamera-vid", "--nopreview", "--width", "640", "--height", "480", "--framerate", "30", "--codec", "mjpeg", "--output", "-"],
        stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )

    # We use ffmpeg to convert MJPEG output to a stream
    ffmpeg_process = subprocess.Popen(
        ["ffmpeg", "-f", "mjpeg", "-i", "-", "-f", "mjpeg", "pipe:1"],
        stdin=process.stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )
    
    while True:
        # Read frame by frame from ffmpeg output
        frame = ffmpeg_process.stdout.read(1024)
        if not frame:
            break  # Stop if no frame is captured
        
        # Yield the frame to the client (this is the streaming part)
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

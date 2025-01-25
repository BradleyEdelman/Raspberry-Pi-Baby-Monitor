from flask import Flask, render_template, Response
import subprocess
import time

app = Flask(__name__)

def gen_frames():
    # Start ffmpeg process
    ffmpeg_process = subprocess.Popen(
        ["ffmpeg", "-i", "video_input", "-f", "mjpeg", "-"],
        stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )

    while True:
        frame = ffmpeg_process.stdout.read(1024)  # Read in chunks of 1024 bytes
        
        if not frame:
            break  # Stop if no frame is captured
        
        # Check for errors in the stderr stream and print them
        error = ffmpeg_process.stderr.read(1024)
        if error:
            print(f"Error: {error.decode('utf-8')}")
            break
        
        # Yield each frame to the client
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

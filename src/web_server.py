from flask import Flask, render_template, Response
import subprocess
import io

app = Flask(__name__)

def gen_video():
    # Use libcamera-vid to capture video and pipe it to ffmpeg for MJPEG streaming
    command = [
        "libcamera-vid",
        "-t", "0",  # infinite time, continuous stream
        "--inline",  # inline MJPEG frames
        "--bitrate", "2000000",  # set bitrate for quality
        "-o", "-",  # output to stdout (pipe)
    ]
    
    # Start the process
    proc = subprocess.Popen(command, stdout=subprocess.PIPE)
    
    while True:
        # Read each frame (MJPEG)
        frame = proc.stdout.read(1024)
        
        # If the frame is empty, we break
        if not frame:
            break
        
        # Yield each frame to the client
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video')
def video():
    return Response(gen_video(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

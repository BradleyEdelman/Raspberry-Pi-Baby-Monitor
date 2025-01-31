from flask import Flask, render_template, Response
import subprocess

app = Flask(__name__)

def gen_video():
    print("Starting video stream...")
    command = [
        "libcamera-vid",
        "-t", "0",  # infinite time, continuous stream
        "--inline",  # inline MJPEG frames
        "--bitrate", "2000000",  # set bitrate for quality
        "-o", "-",  # output to stdout (pipe)
    ]
    
    proc = subprocess.Popen(command, stdout=subprocess.PIPE)
    
    print("Process started, reading frames...")
    while True:
        frame = proc.stdout.read(1024)
        if frame:
            print("Sending frame...")
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
        else:
            print("No frame received, stopping.")
            break


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video')
def video():
    return Response(gen_video(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

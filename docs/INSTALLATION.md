# Installation instructions for the baby monitor

## Step 1: Install system-level dependencies and stream video on network

1. **Create a project directory**
   - Create a "baby monitor" projects directory, as follows:

   ```bash
   mkdir -p /home/<username>/projects
   mkdir -p /home/<username>/projects/baby_monitor
   ```

2. **Clone the repository**
   - Clone this github repository:

   ```bash
   cd /home/<username>/projects/baby_monitor
   git clone https://github.com/BradleyEdelman/Raspberry-Pi-Baby-Monitor.git
   ```

3. **Install system-level dependencies**

1. **Install dependecies**
   - I had various issues installing and access certain libraries from a virtual environment, so I recommend using system level installations.
   - Navigate to the repository folder and run the install.sh script. This will install system-level dependencies for libcamera, picamera2, GStreamer, OpenCV, and Flask, as well as other python libraries necessary to stream the video.

   ```bash
   cd /home/<username>/Raspberry-Pi-Baby-Monitor
   chmod +x install.sh
   ./install.sh
   ```

   - Run the script of your choosing based on the desired functionality:
   
   ```bash
   python3 stream.py
   ```

6. **View live stream**
   - Using a web browser on a device connected to the same Wi-Fi network, visit the live stream page:

   http://<your_pi_ip>:5000


## Step 5: Stream off network (ngrok)

TBD
sudo wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-arm.zip
sudo apt install unzip


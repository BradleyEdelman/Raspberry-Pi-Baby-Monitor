# Installation instructions for the baby monitor

## Step 1: Install system-level dependencies and stream video on network

1. **Install dependecies**
   - I had various issues installing and access certain libraries from a virtual environment, so I recommend using system level installations.
   - SSH into the Raspberry Pi and type the following commands to install dependecies for libcamera, picamera2, GStreamer, OpenCV, and Flask:

   ```bash
   sudo apt install python3-pip
   sudo apt-get update
   sudo apt-get install -y libcamera-dev
   sudo apt-get install -y gstreamer1.0-tools
   sudo apt-get install -y gstreamer1.0-plugins-base
   sudo apt-get install -y gstreamer1.0-plugins-good
   sudo apt-get install -y python3-opencv
   sudo apt-get install -y python3-flask
   ```

2. **Create a project directory**
   - Create a "baby monitor" projects directory, as follows:

   ```bash
   mkdir -p /home/<username>/projects
   mkdir -p /home/<username>/projects/baby_monitor
   ```

5. **Clone the repository**
   - Clone this github repository:

   ```bash
   cd /home/<username>/projects/baby_monitor
   git clone https://github.com/BradleyEdelman/Raspberry-Pi-Baby-Monitor.git
   cd /home/<username>/Raspberry-Pi-Baby-Monitor/src
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


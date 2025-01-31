# Installation Guide for Raspberry Pi Baby Monitor

This guide walks through the steps to set up the Raspberry Pi, install the necessary software, and prepare it for use with the Baby Monitor.

## Prerequisites

- Raspberry Pi 4 (or other compatible Raspberry Pi model)
- Raspberry Pi OS (Lite version is recommended for minimal setup)
- SD card (8GB or larger recommended)
- Micro-USB power supply
- Monitor or TV for initial setup (optional)
- Keyboard and mouse (optional, for setup without SSH)



## Step 1: Flashing the SD Card with Raspberry Pi OS

1. **Download the Raspberry Pi Imager**:  
   Visit the [Raspberry Pi Imager page](https://www.raspberrypi.org/software/) and download the imager for your operating system.

2. **Install the Raspberry Pi OS**:  
   - Insert your SD card into your computer.
   - Open the Raspberry Pi Imager and select Raspberry Pi OS from the list of available operating systems (recommend 64 bit).
   - Choose the SD card and click **Write** to begin the flashing process.

3. **Edit Settings Before Flashing**:  
   - In the Raspberry Pi Imager, before starting the flashing process, click on the **settings** icon (gear icon) on the bottom right of the imager window.
   - Enable **SSH** to allow remote access.
   - Set your **username** and **password** for the Pi (remember them!).
   - Configure your **Wi-Fi** settings:  
     - Enter your **Wi-Fi network name (SSID)** and **password**.
     - Set the correct **country code** to ensure proper Wi-Fi operation.

4. **Complete the Flashing**:  
   After you have set everything up, proceed with flashing the SD card. Once the flashing process is complete, remove the SD card from your computer.



## Step 2: Set Up SSH Access (for headless setup)
1. **Find the Pi’s IP Address**:  
   - Make sure your client (e.g. desktop/laptop) is on the same Wi-Fi network as the Raspberry Pi host.
   - Use a network scanner like `nmap` (download for windows) to find the IP address assigned to the Raspberry Pi.
   - If the Raspberry Pi is connected to a monitor (e.g. for initial setup), the device should tell you its IP address once fully booted
   - If no monitor is connected, open powershell on the client and type in the following line to identify devices on the local network

   ```bash
   nmap -sn 192.168.1.0/24
   ```

2. **SSH into the Raspberry Pi**:  
   - Once you've identified the IP address, open a command prompt or power shell on your computer and run the following command to SSH into your Raspberry Pi:

   ```bash
   ssh <username>@<your_pi_ip_address>
   ```

   - Enter the password that you specified during the flashing process


## Step 3: Test camera (optional)

1. **Update the System**:  
   - SSH into the host and run the following commands to ensure your system is up-to-date:
   
   ```bash
   sudo apt update
   sudo apt upgrade
   sudo reboot
   ```

2. **Test the Camera**
   - Ensure the camera module is properly connected to the Raspberry Pi via the camera slot (CSI connector).
   - Check for physical issues like loose ribbons or incorrect orientation.
   - Install `libcamera` tools:
   
   ```bash
   sudo apt install libcamera-apps
   ```

   - Capture a test image/video (10 sec)

   ```bash
   libcamera-jpeg -o test.jpg
   ```

   ```bash
   libcamera-vid -t 10000 -o test.h264
   ```

3. **Transfer image/video to client (headless setup)**
   - After capturing the test image (`test.jpg`) or video (`test.h264`), transfer them to your computer using the `scp` (secure copy) command
   - Open a new terminal or PowerShell and type the following commands (/remote/path/to/file/ should be something like "/home/<username>/"):

   ```bash
   scp username@host:</remote/path/to/file/>test.jpg </local/path/to/destination/>test.jpg .
   scp username@host:</remote/path/to/file/>test.h264 </local/path/to/destination/>test.h264 .
   ```

   - You will get prompted for the Raspberry Pi password again.
   - View test image and video on the client



## Step 4: Install system-level dependencies and stream video on network

1. **Install dependecies**
   - I had issues using picamera2 in a virtual environment so I recommend using the system environment
   - SSH into the Raspberry Pi and type the following commands to install dependecies for libcamera, picamera2, GStreamer, OpenCV, and Flask

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

5. **Clone the repository, install dependencies, and link OpenCV**
   - Clone this github repository and run the stream.py file

   ```bash
   cd /home/<username>/projects/baby_monitor
   git clone https://github.com/BradleyEdelman/Raspberry-Pi-Baby-Monitor.git
   python3 stream.py
   ```


## Step 5: Stream off network


sudo wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-arm.zip
sudo apt install unzip

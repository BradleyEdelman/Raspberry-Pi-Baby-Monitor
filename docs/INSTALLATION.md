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
   - Open the Raspberry Pi Imager and select Raspberry Pi OS (Lite) from the list of available operating systems (recommend 32 bit).
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
After flashing, you'll need to enable SSH on your Raspberry Pi:
1. **Create the `ssh` file**:  
   - If you haven't already enabled SSH in the imager settings, you need to create an empty file named `ssh` (without any file extension) in the boot partition of the SD card.  
   - Insert the SD card into your computer and create the `ssh` file in the root of the boot partition.

2. **Insert the SD card into the Raspberry Pi**:  
   - Once SSH is enabled, insert the SD card into your Raspberry Pi.

3. **Connect the Raspberry Pi to a Network**:  
   - If you configured Wi-Fi during the flashing process, the Pi should connect automatically.
   - If not, or if you're troubleshooting, connect the Pi to the network via an Ethernet cable.

4. **Find the Pi’s IP Address**:  
   - Make sure your client (e.g. desktop/laptop) is on the same Wi-Fi network as the Raspberry Pi host.
   - Use a network scanner like `nmap` (download for windows) to find the IP address assigned to the Raspberry Pi.
   - If the Raspberry Pi is connected to a monitor (e.g. for initial setup), the device should tell you its IP address once fully booted
   - If no monitor is conneted, open powershell on the client and type in the following line to identify devices on the local network

   ```bash
   nmap -sn 192.168.1.0/24
   ```

5. **SSH into the Raspberry Pi**:  
   - Once you've identified the IP address, open a command prompt or power shell on your computer and run the following command to SSH into your Raspberry Pi:

   ```bash
   ssh <username>@<your_pi_ip_address>
   ```

   - Enter the password that you specied during the flashing process

6. **Setup Wi-Fi, if needed**:
   - If your Raspberry Pi did not automatically connect to Wi-Fi and/or if you performed the initial setup with the device connected to a router via ethernet cable (like me), you can now create the `wpa_supplicant.conf` file
   - In power shell, type the following to open the new file:

   ```bash
   cat /etc/wpa_supplicant/wpa
   ```
   - Then type the following, and finally hit ctrl+X to save and exit.

   ```bash
   country=CH
   ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
   update_config=1
   network={
       ssid="your_wifi_network"
       psk="your_wifi_password"
   }
   ```

   - Finally, reboot the device:

   ```bash
   sudo reboot
   ```

   - If you had previously connected to the Raspberry Pi via an ethernet cable, unplug it and run the nmap command again to find the IP address (or find it on a connected screen). Note that it may be different than before.



## Step 3: Install and Enable Camera

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
   - Open a new terminal or PowerShell and type the following commands:

   ```bash
   scp <username>@<pi_ip_address>:<full localpath>/test.jpg .
   scp <username>@<pi_ip_address>:<full localpath>/test.h264 .
   ```

   - You will get prompted for the Raspberry Pi password again.
   - View test image and video on the client



## Step 4: Setup project environment on Raspberry Pi

1. **Install pip and venv**
   - SSH into the Raspberry Pi and type the following commands:

   ```bash
   sudo apt install python3-pip
   sudo apt install python3-venv
   ```

1. **Create a project directory**
   - Create a "baby monitor" projects directory, as follows:

   ```bash
   mkdir -p /home/<username>/projects
   mkdir -p /home/<username>/projects/baby_monitor
   ```

2. **Setup virtual environment for project and install dependencies**
   - Navigate to the project directory, and create and activate a virtual environment

   ```bash
   cd /home/<username>/projects/baby_monitor
   python3 -m venv venv
   source venv/bin/ativate
   ```

3. **Clone the repository and install dependencies**
   - While inside the virtual environment clone this github repository and install the requirements

   ```bash
   git clone https://github.com/BradleyEdelman/Raspberry-Pi-Baby-Monitor.git
   cd Raspberry-Pi-Baby-Monitor
   pip install -r requirements.txt
   ```



## Step 5: Run Project and Enjoy!


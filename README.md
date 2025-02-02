# Raspberry Pi Baby Monitor
**v1.0.0**

## Overview
This project describes a cost-effective and customizable baby monitor using a Raspberry Pi. Cost effectiveness is a relative term, depending on which store-bought option you are looking at :), but I was able to source the parts for ~160 CHF (including shipping in and to CH). I also dont currently have access to a soldering iron, so the parts I sourced are completely plug-and-play. For now, I'm building into the monitor support for live video streaming (url), infrared night vision, and hopefully dynamic control of an IR LED based on ambient light detection. In the future, I think it would be fun to expand this to include real-time behavioral classification (edge AI), and to stream to an open-source app with push notifications. I'm sure the baby will be too big for these features to be useful by the time I get them up and running, but why not dream!

## Features (as desired)
- **Live Video Streaming**: View the video feed from a web browser on a computer or smart phone.
- **Night Vision Support**: Use an IR camera module and IR LED for low-light environments (sleep time).
<!-- - **Dynamic Lighting**: Turn on/off IR LED turns manually or connect it to a light sensor for automatic adjustments. -->

## Parts List
| Component                                      | Description
|----------------------------------------------- |-----------------------------------------------------------------------------------|
| Raspberry Pi 4 (4GB) Starter Kit               | Includes power supply, case, and SD card                 
| Raspberry Pi NoIR v2.1 Camera Module           | 8MP infrared camera module                              
| Adafruit TSL2591 Light Sensor                  | High-dynamic range light sensor                          
| Adafruit High Power IR LED Emitter             | For infrared night vision                                
| JST PH 3-Pin to Female Socket Cable (200mm)    | For connecting the IR LED emitter                        
| JST PH 4-Pin to Female Socket Cable (200mm)    | For connecting the light sensor                          

## File Tree
```
RaspberryPiBabyMonitor/
│
├── src/
│ ├── stream.py
│ └── stream_toggle.py
│
├── docs/
│ ├── INSTALLATION.md
│ ├── SETUP.md
│ └── TROUBLESHOOTING.md
│
├── requirements.txt
├── setup.py
├── .gitignore
├── README.md
└── LICENSE
```

## Getting Started
1. **Assemble the hardware**:
   - Connect the camera module to the Raspberry Pi.
   <!-- - Attach the IR LED and light sensor using the respective JST connectors. -->
   
2. **Set up the software**:
   - Follow the detailed instructions in [SETUP.md](docs/SETUP.md#step-1-flashing-the-sd-card-with-raspberry-pi-os) to flash Raspberry Pi OS, set up SSH and network configuration, and connect the hardware
   - Clone this repository and install the required dependencies by following [INSTALLATION.md](docs/INSTALLATION.md#step-4-setup-project-environment-on-raspberry-pi).

3. **Run the application**:
   - Execute the desired version of `stream.py` to start the video feed and additional features.
   - Use a web browser on a computer or smart phone to view the stream by visiting `http://<raspberry_pi_ip>:5000`.

   - Here's an explanation of the different stream.py versions:


## Harware Rquirements and Functionality
   stream.py (Basic video streaming)
   - Raspberry Pi 4
   - Raspberry Pi Camera Module (NoIR v2.1 or regular)
   - Wi-Fi connection

   stream_toggle.py (+ toggle stream on/off)
   - Raspberry Pi 4
   - Raspberry Pi Camera Module (NoIR v2.1 or regular)
   - Wi-Fi connection

   <!-- stream_LED.py (+ manual on/off LED control)
   - Raspberry Pi 4
   - Raspberry Pi Camera Module (NoIR v2.1 or regular)
   - Wi-Fi connection
   - Adafruit High Power IR LED Emitter -->


<!-- ## Usage
- Visit `http://<raspberry_pi_ip>:<port>` in a browser to view the live stream.
- The IR LED will automatically turn on when the light sensor detects low ambient light. -->

## Future Plans
- Automatic LED adjustments.
- Edge AI models for real-time monitoring.
- Extend support for mobile apps.




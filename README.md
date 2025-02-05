# Raspberry Pi Baby Monitor
**v1.0.0**

## Overview
This project describes a cost-effective and customizable baby monitor using a Raspberry Pi. Cost effectiveness is a relative term, depending on which store-bought option you are looking at :), but I was able to source the parts for ~160 CHF (including shipping in and to CH). I also dont currently have access to a soldering iron, so the parts I sourced are completely plug-and-play. For now, I'm building into the monitor support for live video streaming (url), infrared night vision, and hopefully dynamic control of an IR LED based on ambient light detection. In the future, I think it would be fun to expand this to include real-time behavioral classification (edge AI), and to stream to an open-source app with push notifications. I'm sure the baby will be too big for these features to be useful by the time I get them up and running, but why not dream!

## Features (as desired)
- **Live Video Streaming**: View the video feed from a web browser on a computer or smart phone.
- **Night Vision Support**: Use an IR camera module and IR LED for low-light environments (sleep time).
- **Dynamic Lighting**: Turn on/off IR LED turns manually or connect it to a light sensor for automatic adjustments.

## Parts List
| Component                                            | Description
|----------------------------------------------- |-----------------------------------------------------------------------------------|
| Raspberry Pi 4 (4GB) Starter Kit                     | Includes power supply, case, and SD card                 
| Raspberry Pi NoIR v2.1 Camera Module                 | 8MP infrared camera module                              
| Adafruit TSL2591 Light Sensor                        | High-dynamic range light sensor                          
| Adafruit High Power IR LED Emitter                   | For infrared light vision                                
| STEMMA JST PH 2mm 3-Pin to Female Socket Cable       | For connecting the IR LED emitter                        
| JST PH 3-Pin to Female Socket Cable (200mm)          | For connecting the light sensor                          

## File Tree
```
RaspberryPiBabyMonitor/
│
├── src/
│ ├── stream.py
│ ├── stream_toggle.py
│ └── stream_LED.py
│
├── docs/
│ ├── images/
│ ├── SETUP_HARDWARE.md
│ ├── SETUP_SOFTWARE.md
│ └── TROUBLESHOOTING.md
│
├── requirements.txt
├── setup.py
├── .gitignore
├── README.md
└── LICENSE
```

## Getting Started
1. **Assemble the hardware [SETUP_HARDWARE.md](docs/SETUP.md#step-1-flashing-the-sd-card-with-raspberry-pi-os)**:
   - Connect the camera module to the Raspberry Pi (_Steps 1-4_).
   - Attach the IR LED and light sensor using the respective JST connectors, if desired (_Step 5_)
   
2. **Set up the software [SETUP_SOFTWARE.md](docs/SETUP.md#step-1-flashing-the-sd-card-with-raspberry-pi-os)**:
   - Flash Raspberry Pi OS and create a project directory via SSH
   - Clone this repository and install the required dependencies

3. **Run the application**:
   - Execute the desired version of `stream.py` (see next section) to start the video feed and additional features.
   - Use a web browser on a computer or smart phone to view the stream by visiting `http://<raspberry_pi_ip>:5000`.


## Harware Rquirements and Functionality
   stream.py (Basic video streaming)
   - Raspberry Pi 4
   - Raspberry Pi Camera Module (NoIR v2.1 or regular)
   - Wi-Fi connection

   stream_toggle.py (+ toggle stream on/off)
   - Raspberry Pi 4
   - Raspberry Pi Camera Module (NoIR v2.1 or regular)
   - Wi-Fi connection

   stream_LED.py (+ manual on/off LED control)
   - Raspberry Pi 4
   - Raspberry Pi Camera Module (NoIR v2.1 or regular)
   - Wi-Fi connection
   - Adafruit High Power IR LED Emitter

## Future Plans
- Automatic LED adjustments.
- Edge AI models for real-time monitoring.
- Extend support for mobile apps.
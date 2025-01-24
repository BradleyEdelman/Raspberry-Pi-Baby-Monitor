# Raspberry Pi Baby Monitor

## Overview
This project describes a cost-effective and customizable baby monitor using a Raspberry Pi. Cost effectiveness is a relative term, depending on which store-bought option you are looking at :), but I was able to source the parts for ~160 CHF (including shipping in and to CH). I also dont currently have access to a soldering iron, so the parts I sourced are completely plug-and-play. For now, I'm building into the monitor support for live video streaming (url), infrared night vision, and hopefully dynamic control of an IR LED based on ambient light detection. In the future, I think it would be fun to expand this to include audio streaming and real-time behavioral classification (edge AI), and to stream to an open-source app with push notifications. I'm sure the baby will be too big for these features to be useful by the time I get them up and running, but why not dream!

## Features
- **Live Video Streaming**: View the video feed from a web browser or compatible apps on a cell phone.
- **Night Vision Support**: Equipped with an IR camera module and IR LED for low-light environments (sleep time).
- **Dynamic Lighting**: IR LED turns on/off based on ambient light using a light sensor.

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
│ ├── video_stream.py
│ ├── web_server.py
│ └── light_sensor.py
│
├── docs/
│ ├── INSTALLATION.md
│ └── TROUBLESHOOTING.md
│
├── templates/
│ └── index.html
│
├── tests/
│ ├── test_video_stream.py
│ ├── test_led_control.py
│ └── test_light_sensor.py
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
   - Attach the IR LED emitter and light sensor using the respective JST connectors.
   
2. **Set up the software**:
   - Follow the detailed instructions in [Step 1 and Step 2 of the INSTALLATION.md](INSTALLATION.md#step-1-flashing-the-sd-card-with-raspberry-pi-os) to flash Raspberry Pi OS and set up SSH and network configuration.
   - Clone this repository and install the required dependencies by following [Step 4 of the INSTALLATION.md](INSTALLATION.md#step-4-setup-project-environment-on-raspberry-pi).

3. **Run the application**:
   - Execute `web_server.py` to start the video feed.
   - Use a web browser to view the stream by visiting `http://<raspberry_pi_ip>:<port>`.

## Usage
- Visit `http://<raspberry_pi_ip>:<port>` in a browser to view the live stream.
- The IR LED will automatically turn on when the light sensor detects low ambient light.

## Future Plans
- Add audio streaming via a microphone.
- Integrate edge AI models for real-time monitoring.
- Extend support for mobile apps.




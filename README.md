# Raspberry Pi Baby Monitor

## Overview
This project provides a cost-effective and customizable baby monitor solution using a Raspberry Pi. Cost effectiveness is a relative term, depending on which store-bought option you are looking at, but I was able to source the parts for ~160 CHF (including shipping in and to CH). I also dont currently have access to a soldering iron, so the parts I sources are completely plug-and-play. For now, the monitor supports live video streaming, infrared night vision, and dynamic control of an IR LED based on ambient light. In the future, I think it would be fun to expand this to include audio streaming and real-time behavioral classification (edge AI). I'm sure the baby will be too big for these features to be useful by the time I get them up and running, but why not!

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
├── src/
│ ├── video_stream.py
│ ├── led_control.py
│ ├── light_sensor.py
│ └── setup.py
├── docs/
│ ├── INSTALLATION.md
│ ├── TROUBLESHOOTING.md
│ └── EXPANSION.md
├── tests/
│ ├── test_video_stream.py
│ ├── test_led_control.py
│ └── test_light_sensor.py
├── README.md
└── LICENSE
```

## Getting Started
1. **Assemble the hardware**:
   - Connect the camera module to the Raspberry Pi.
   - Attach the IR LED emitter and light sensor using the respective JST connectors.
2. **Set up the software**:
   - Flash Raspberry Pi OS Lite onto the SD card.
   - Enable SSH and configure the network connection.
   - Clone this repository and install dependencies.
3. **Run the application**:
   - Execute `video_stream.py` to start the video feed.
   - Use a web browser to view the stream.

## Usage
- Visit `http://<raspberry_pi_ip>:<port>` in a browser to view the live stream.
- The IR LED will automatically turn on when the light sensor detects low ambient light.

## Future Plans
- Add audio streaming via a microphone.
- Integrate edge AI models for real-time monitoring.
- Extend support for mobile apps.




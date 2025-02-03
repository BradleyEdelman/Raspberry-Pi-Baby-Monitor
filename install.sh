#!/bin/bash

echo "Updating package list..."
sudo apt-get update

echo "Installing system dependencies..."
sudo apt install -y python3-pip
sudo apt-get install -y libcamera-dev
sudo apt-get install -y gstreamer1.0-tools
sudo apt-get install -y gstreamer1.0-plugins-base
sudo apt-get install -y gstreamer1.0-plugins-good
sudo apt-get install -y python3-opencv
sudo apt-get install -y python3-flask
sudo apt-get install -y python3-rpi.gpio

echo "Installing python dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

echo "Installation complete!"

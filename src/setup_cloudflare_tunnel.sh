#!/bin/bash

echo "Installing Cloudflar"
sudo apt-get install curl lsb-release
curl -L https://pkg.cloudflare.com/cloudflare-main.gpg | sudo tee /usr/share/keyrings/cloudflare-archive-keyring.gpg >/dev/null
echo "deb [signed-by=/usr/share/keyrings/cloudflare-archive-keyring.gpg] https://pkg.cloudflare.com/cloudflared $(lsb_release -cs) main" | sudo tee  /etc/apt/sources.list.d/cloudflared.list
sudo apt-get update
sudo apt-get install -y cloudflared





echo "Logging into Cloudflare. Follow the instructions to authenticate..."
cloudflared tunnel login

echo "Creating a new tunnel..."
cloudflared tunnel create bje-stream-tunnel

TUNNEL_UUID=$(cloudflared tunnel list | grep bje-stream-tunnel | awk '{print $1}')

echo "Configuring tunnel..."
mkdir -p ~/.cloudflared
cat <<EOT > ~/.cloudflared/config.yml
tunnel: $TUNNEL_UUID
credentials-file: /home/bedelman/.cloudflared/$TUNNEL_UUID.json

ingress:
  - hostname: bje-stream.cloudflareTunnel.com
    service: http://localhost:5000
  - service: http_status:404
EOT

echo "Setting up Cloudflare service..."
sudo cloudflared service install

echo "Starting Cloudflare tunnel..."
cloudflared tunnel run my-stream-tunnel &

echo "Starting video stream..."
python3 /home/bedelman/projects/baby_monitor/Raspberry-Pi-Baby-Monitor/src/stream_toggle.py &

# Setting Up Cloudflare Tunnel for Raspberry Pi Video Streaming

This guide will help you set up a **Cloudflare Tunnel** to make your Raspberry Pi **video stream accessible over the internet** without exposing your local network. 

---

## **Step 1: Create a Cloudflare Account**
1. Go to **[Cloudflare](https://dash.cloudflare.com/)** and sign up.

2. To make things easier, I also purchased myown domain name for ~$4 for 12 months. If you dont want to pay, you can also stream to a new website everytime you start, but I wanted a permanent location for sharing purposes. Allegedly, CloudFlare also offers free domains, but I couldnt figure this out. If you purchase a domain name with CloudFlare, I would do it now as you will need it to be connected to your account for later steps. I also found another [blog](https://dev.to/omarcloud20/a-free-cloudflare-tunnel-running-on-a-raspberry-pi-1jid) that setup a free domain on Freenom, but I got impatient :).


## **Step 2: Install and Build Dependencies**
SSH into your Raspberry Pi and install Cloudflare's tunnel service:

```bash
sudo apt-get install curl lsb-release
curl -L https://pkg.cloudflare.com/cloudflare-main.gpg | sudo tee /usr/share/keyrings/cloudflare-archive-keyring.gpg >/dev/null
echo "deb [signed-by=/usr/share/keyrings/cloudflare-archive-keyring.gpg] https://pkg.cloudflare.com/cloudflared $(lsb_release -cs) main" | sudo tee  /etc/apt/sources.list.d/cloudflared.list
sudo apt-get update
sudo apt-get install -y cloudflared
```


## **Step 3: Authenticate and Create a Tunnel

1. Log in to CloudFlare
```bash
cloudflared tunnel login
```

If using a headless setup like me, this will print out a login link. You should copy and paste this link on your client and login (if you havent done so already). This will take you to a screen like below where you should select your domain that you previously created.

Once connected, you should receive a message in your Raspberry Pi that ~/.cloudflared/cert.pem file has been created. This should also create a ~/.cloudflared/config.yml file that you will modify in the next step.

2. Create a new tunnel

```bash
cloudflared tunnel create your-tunnel-name
```

This will generate a unique tunnel ID (UUID) that you can view by running the following:

```bash
cloudflared tunnel list
```


## **Step 4: Configure the Tunnel and DNS**

1. Edit the CloudFlare Tunnel configuration:
```bash
nano ~/.cloudflared/config.yml
```

2. Make sure that your config.yml file looks like that below. Be sure to replace "your-tunnel-id", "username", and "domain-name" with those you have created/set up.

```json
tunnel: your-tunnel-id
credentials-file: /home/username/.cloudflared/your-tunnel-id.json

ingress:
  - hostname: domain-name
    service: http://localhost:5000
    originRequest:
      connectTimeout: 30s
      noTLSVerify: true
      keepAliveTimeout: 60s
  - service: http_status:404
```

3. Route the tunnel to your domain's DNS
```bash
cloudflared tunnel route dns tunnel-name domain-name
```

## **Step 5: Start the Tunnel and Stream**

```bash
cloudflared tunnel run your-tunnel-name & python3 stream_toggle.py &
```

You should now be able to see the stream on both your local Wi-Fi-connected devices at "http://<your_pi_ip>:5000" and non-local devices at "domain-name"

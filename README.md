# video_streaming-using-RTMP
Tools & software needed
FFmpeg, NGINX, Python, opencv

# Flow
Streaming(RTMP) using FFmpeg --> Nginx server --> Video(RTMP) on vlc media player  

# Working (server in WSL)

Instalation of NGINX Server
1. Update pakages
```bash 
sudo apt update && sudo apt upgrade -y
```

2. Install nginx server
```bash
sudo apt install nginx -y
```

3. Start nginx server
```bash
sudo systemctl start nginx
```

4. Enable NGINX to Start on Boot (Optional)
```bash
sudo systemctl enable nginx
```

5. Check NGINX Status
```bash
sudo systemctl status nginx
note-- Press q to exit the status view.
```

6. Configure Firewall (if needed)
```bash
sudo ufw allow 'Nginx Full'
note-- ufw is not installed, install it using:
sudo apt install ufw -y
```

7. Stop or Restart NGINX
```bash
sudo systemctl stop nginx

sudo systemctl restart nginx 
``` 

# To watch video stream
To watch video we need media player which support RTMP. Here we use VLC
Paste RTMP url in vlc media player(more options --> new stream)

 rtmp://Your_SERVER_IP_address/live  

# Steps to follow
__1.__ **start server**

__2.__ **run python script for streaming**

__3.__ **play in vlc**
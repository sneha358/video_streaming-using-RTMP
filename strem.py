import cv2
import subprocess

# RTMP Server URL (Replace with your Windows RTMP URL)
RTMP_URL = "rtmp://Your_SERVER_IP_address/live"

# Capture video from the default webcam
cap = cv2.VideoCapture(0)

# Get video properties
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(cap.get(cv2.CAP_PROP_FPS) or 30)

# FFmpeg command to stream
command = [
    "ffmpeg",
    "-f", "rawvideo",
    "-pix_fmt", "bgr24",
    "-s", f"{width}x{height}",
    "-r", str(fps),
    "-i", "-",
    "-c:v", "libx264",
    "-preset", "ultrafast",
    "-tune", "zerolatency",
    "-b:v", "2500k",
    "-f", "flv",
    RTMP_URL
]

# Start FFmpeg process
process = subprocess.Popen(command, stdin=subprocess.PIPE)

while cap.isOpened(): 
    ret, frame = cap.read()
    if not ret:
        break

    # Write frame to FFmpeg
    process.stdin.write(frame.tobytes())

# Cleanup
cap.release()
process.stdin.close()
process.wait()

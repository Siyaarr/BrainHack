from pupil_labs.realtime_api.simple import discover_one_device
import socket
import time

# Look for devices. Returns as soon as it has found the first device.
print("Looking for the next best device...")
device = discover_one_device(max_search_duration_seconds=10)
if device is None:
    print("No device found.")
    raise SystemExit(-1)




# device.streaming_start()  # optional, if not called, stream is started on-demand

firstImage = device.receive_gaze_datum()[0]

try:
    while True:
        firstImageOfFrame = device.receive_gaze_datum()[0]
        time.sleep(0.5)
        secondImageOfFrame = device.receive_gaze_datum()[0]
        
        
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            
        if firstImage -120 <firstImageOfFrame < firstImage + 120 and firstImage -120 <secondImageOfFrame < firstImage + 120:
            print("middle")
            
        elif firstImageOfFrame < firstImage -120 and secondImageOfFrame < firstImage -120:
            print("left")
            sock.sendto(bytes("-50;50", "utf-8"), ("192.168.255.95", 3000))
            time.sleep(1)
            sock.sendto(bytes("0;0", "utf-8"), ("192.168.255.95", 3000))

        elif firstImageOfFrame > firstImage + 120 and secondImageOfFrame > firstImage + 120:
            print("right")
            sock.sendto(bytes("50;-50", "utf-8"), ("192.168.255.95", 3000))
            time.sleep(1)
            sock.sendto(bytes("0;0", "utf-8"), ("192.168.255.95", 3000))
        
except KeyboardInterrupt:
    pass
finally:
    print("Stopping...")
    # device.streaming_stop()  # optional, if not called, stream is stopped on close
    device.close()  # explicitly stop auto-update
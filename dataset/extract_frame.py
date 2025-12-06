import cv2
import os

VIDEO_PATH = "D:/Genshin Alert Project/data_rework/Electrohammer.mp4"    
OUTPUT_DIR = "D:/Genshin Alert Project/data_rework/frames__electro_hammer"
FRAME_INTERVAL = 5           
MOTION_THRESHOLD = 25  

os.makedirs(OUTPUT_DIR, exist_ok=True)

cap = cv2.VideoCapture(VIDEO_PATH)

if not cap.isOpened():
    print("Cannot find/opened video")
    exit()

ret, prev_frame = cap.read()
if not ret:
    print("Cannot find first frame!")
    exit()

prev_gray = cv2.cvtColor(prev_frame, cv2.COLOR_BGR2GRAY)

frame_count = 0
saved_count = 0

print("Execute...")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame_count += 1

   
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

   
    diff = cv2.absdiff(prev_gray, gray)
    _, thresh = cv2.threshold(diff, 30, 255, cv2.THRESH_BINARY)
    motion = cv2.countNonZero(thresh)

   
    if motion > MOTION_THRESHOLD and frame_count % FRAME_INTERVAL == 0:
        filename = f"{OUTPUT_DIR}/frame_{saved_count:06d}.jpg"
        cv2.imwrite(filename, frame)
        saved_count += 1

    prev_gray = gray

cap.release()

print(f"Done. Saved {saved_count} image(s) to '{OUTPUT_DIR}'.")

import time
import mss
import cv2
import numpy as np
import pyttsx3
import threading
from ultralytics import YOLO

# configuration
MODEL_PATH = "D:/Enemy Alert Project/dataset/alert_window/best.pt"
GAME_REGION = {'top': 0, 'left': 0, 'width': 1920, 'height': 1080}
CONFIDENCE_THRESHOLD = 0.5
COOLDOWN_SECONDS = 2.0

# warning list
ALERT_MESSAGES = {
    "Enemy_Cryo_Abyss_Mage": "Cryo Abyss Mage detected",
    "Enemy_Cryogunner_Legionnaire": "Cryoguuner detected",
    "Enemy_Electro_Abyss_Mage": "Electro Abyss Mage detected",
    "Enemy_Fatui_Anemoboxer_Vanguard": "Fatui Anemoboxer Vanguard detected",
    "Enemy_Fatui_Cryo_Cicin_Mage": "Fatui Cryo Cicin detected",
    "Enemy_Fatui_Electro_Cicin_Mage": "Fatui Electro Cicin detected",
    "Enemy_Fatui_Electrohammer_Vanguard": "Fatui Electrohammer Vanguard detected",
    "Enemy_Fatui_Geochanter_Bracer": "Fatui Geochanter Bracer detected",
    "Enemy_Fatui_Hydrogunner_Legionnaire": "Fatui Hydrogunner Legionaire detected",
    "Enemy_Fatui_Pyro_Agent": "Fatui Pyro Agent detected",
    "Enemy_Fatui_Pyroslinger_Bracer": "Fatui Pyroslinger Bracer detected",
    "Enemy_Hydro_Abyss_Mage": "Hydro Abyss Mage detected",
    "Enemy_Mirror_Maiden": "Mirror Maiden detected",
    "Enemy_Mitachurl": "Mitachurl detected",
    "Enemy_Pyro_Abyss_Mage": "Pyro Abyss Mage detected",
    "Enemy_Rifthound": "Rifthound detected",
    "Enemy_Ruin_Drake": "Ruin Drake detected",
    "Enemy_Ruin_Grader": "Ruin Grader detected",
    "Enemy_Ruin_Guard": "Ruin Guard detected",
    "Enemy_Ruin_Hunter": "ruin Hunter detected",
    "Enemy_Lawachurl": "Lawachurl detected",
}

engine = pyttsx3.init()
engine.setProperty('rate', 160)
engine.setProperty('volume', 1.0)
last_alert_time = {}

def play_voice(text):
    def run():
        try:
            eng = pyttsx3.init()
            eng.say(text)
            eng.runAndWait()
        except:
            pass
    threading.Thread(target=run, daemon=True).start()

def main():
    print(f"Loading model...")
    model = YOLO(MODEL_PATH)
    print("Start scanning. Press 'Q' in monitor to exit")

    sct = mss.mss()

    while True:
        # screenshot
        screenshot = sct.grab(GAME_REGION)
        img_np = np.array(screenshot)
        img_bgr = cv2.cvtColor(img_np, cv2.COLOR_BGRA2BGR)

      
        results = model.predict(
            img_bgr,
            conf=0.55,      # conf cao hơn để giảm báo sai
            iou=0.6,        # giảm overlap sai
            device=0,       # bắt GPU
            max_det=50,     # tránh detect bậy
            verbose=False
        )

        
        current_time = time.time()
        
        # find similar frame
        found_monsters = set() 
        
        for result in results:
            for box in result.boxes:
                cls_id = int(box.cls[0])
                class_name = model.names[cls_id]
                found_monsters.add(class_name)

        # activate warning
        for monster in found_monsters:
            if monster in ALERT_MESSAGES:
                # check cd
                last_time = last_alert_time.get(monster, 0)
                if current_time - last_time > COOLDOWN_SECONDS:
                    message = ALERT_MESSAGES[monster]
                    
                    # print the warning process
                    print(f"{monster} detected -> Warning activated...")
                    
                    play_voice(message)
                    last_alert_time[monster] = current_time

        # supervise window
        preview_img = cv2.resize(img_bgr, (640, 360))
        cv2.imshow('Hidden Monitor (Press Q to exit)', preview_img)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
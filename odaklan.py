import os
import random
import cv2
from ultralytics import YOLO
import vlc

klasor = os.path.dirname(os.path.abspath(__file__))

videolar = [
    os.path.join(klasor, "bırak.mp4"),
    os.path.join(klasor, "bırakk.mp4"),
    os.path.join(klasor, "okul.mp4"),
    os.path.join(klasor, "telfon.mp4"),
]

model = YOLO(os.path.join(klasor, "yolov8n.pt"))

player = vlc.MediaPlayer()
video_baslatildi = False

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Hata: Kamera açılamadı!")
    exit()

print("Arka planda çalışıyor... Kapatmak için bu pencerede Ctrl+C bas.")

try:
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Kameradan görüntü alınamadı!")
            break

        results = model(frame, verbose=False)
        telefon_var_mi = False

        for r in results:
            for box in r.boxes:
                if model.names[int(box.cls[0])] == "cell phone":
                    telefon_var_mi = True

        if video_baslatildi and player.get_state() in (vlc.State.Ended, vlc.State.Stopped, vlc.State.Error):
            player.stop()
            video_baslatildi = False

        if telefon_var_mi and not video_baslatildi:
            secilen = random.choice(videolar)
            player.set_media(vlc.Media(secilen))
            player.play()
            player.set_fullscreen(True)
            video_baslatildi = True

except KeyboardInterrupt:
    pass

player.stop()
cap.release()
# 📵 PhoneGuard

Kamerayla telefonunu gören ve seni uyaran odaklanma asistanı. Kamera arka planda sessizce çalışır, telefon göründüğü anda ekran uyarı videosuyla kaplanır.

## Nasıl Çalışır?

1. Web kamerası arka planda açık kalır (ekranda görüntü gösterilmez).
2. YOLOv8 modeli kameradaki görüntüde telefon (`cell phone`) arar.
3. Telefon görülünce 4 uyarı videosundan biri rastgele seçilir ve **tam ekran** oynatılır.
4. Telefon kaybolsa bile video **bitene kadar** oynar, bitince kapanır.
5. Telefon tekrar görülürse yeni bir video rastgele açılır.

## Kullanılan Teknolojiler

- Python
- [Ultralytics YOLOv8](https://github.com/ultralytics/ultralytics) (nesne tespiti)
- OpenCV (kamera)
- python-vlc (video oynatma)

## Kurulum

1. [VLC Media Player](https://www.videolan.org/) bilgisayarına kurulu olmalı.
2. Gerekli kütüphaneleri yükle:

```bash
pip install ultralytics opencv-python python-vlc
```

3. Repoyu indir:

```bash
git clone https://github.com/KULLANICI_ADIN/PhoneGuard.git
cd PhoneGuard
```

## Klasör Yapısı

```
PhoneGuard/
├── main.py
├── yolov8n.pt
├── bırak.mp4
├── bırakk.mp4
├── okul.mp4
└── telfon.mp4
```

Videolar ve `yolov8n.pt` kodla **aynı klasörde** olmalı.

## Çalıştırma

```bash
python main.py
```

Programı kapatmak için terminalde `Ctrl + C` bas.

## Özelleştirme

Kendi videolarını kullanmak için koddaki `videolar` listesini düzenle:

```python
videolar = [
    os.path.join(klasor, "video1.mp4"),
    os.path.join(klasor, "video2.mp4"),
]
```

## Notlar

- Kamera izni verilmiş olmalı.
- Aydınlık ortamda tespit daha iyi çalışır.
- Model telefonu bazen kaçırabilir, bu YOLOv8n (küçük model) olduğu için normal.

## Lisans

MIT

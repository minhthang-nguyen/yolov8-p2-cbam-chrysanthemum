import cv2
from ultralytics import YOLO

model = YOLO(r"/kaggle/working/yolov8.pt")

results = model.train(data="/kaggle/working/data.yaml", epochs=200, imgsz=640, patience=50)

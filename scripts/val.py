from ultralytics import YOLO
import argparse

p = argparse.ArgumentParser()
p.add_argument("--weights", required=True)
p.add_argument("--data", required=True)
p.add_argument("--imgsz", type=int, default=640)
p.add_argument("--device", default=None)
a = p.parse_args()

YOLO(a.weights).val(data=a.data, imgsz=a.imgsz, device=a.device)

from ultralytics import YOLO
import argparse

p = argparse.ArgumentParser()
p.add_argument("--data", required=True)
p.add_argument("--model", default="models/yolov8n_p2_cbam.yaml")
p.add_argument("--epochs", type=int, default=100)
p.add_argument("--imgsz", type=int, default=640)
p.add_argument("--batch", type=int, default=16)
p.add_argument("--device", default=None)
a = p.parse_args()

YOLO(a.model).train(
    data=a.data,
    epochs=a.epochs,
    imgsz=a.imgsz,
    batch=a.batch,
    device=a.device,
)

from ultralytics import YOLO

# ====== LOAD MODEL ======
model = YOLO(r"/kaggle/working/runs/detect/train/weights/best.pt")

# ====== ĐÁNH GIÁ ======
metrics = model.val(
    data=r"/kaggle/working/data.yaml",
    split="test",        # test set
    imgsz=640
)

# ====== IN KẾT QUẢ ======
print("mAP@0.5     :", metrics.box.map50)
print("mAP@0.5:0.95:", metrics.box.map)
print("Precision   :", metrics.box.mp)
print("Recall      :", metrics.box.mr)

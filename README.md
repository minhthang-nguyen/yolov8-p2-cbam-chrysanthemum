# YOLOv8n P2-CBAM for Chrysanthemum Growth-Stage Detection

This repository contains the model configuration and experiment scaffolding for a YOLOv8n variant used for chrysanthemum growth-stage detection under field conditions.

## Main architectural modifications
- Added a **P2/4 detection branch** for higher-resolution features.
- Used **CBAM** at multiple feature scales.
- Extended detection from **P3/P4/P5** to **P2/P3/P4/P5**.

This project does not claim P2 or CBAM as newly invented components. The contribution is a task-specific architectural adaptation and experimental evaluation.

## Structure
```text
models/yolov8n_p2_cbam.yaml
scripts/train.py
scripts/val.py
scripts/predict.py
data/chrysanthemum.yaml.example
results/
docs/
requirements.txt
```

## Dataset classes
1. Vegetative
2. Fruiting
3. Flowering
4. Harvest

The dataset is not included.

## Reported result
The P2 + CBAM variant achieved **89.3% mAP50**, an improvement of **2.2 percentage points** over the YOLOv8n baseline in the associated experiments.

## License notice
The model configuration is derived from Ultralytics YOLOv8 and retains the original AGPL-3.0 header.

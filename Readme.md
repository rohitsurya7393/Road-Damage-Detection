# Road Damage Detection: A Comparison of YOLOv8 and Faster R-CNN

## Overview

This project focuses on building a deep learning-based system for road damage detection and comparing the performance of two prominent object detection models: **YOLOv8** and **Faster R-CNN (via Detectron2)**.

We explore how each model handles real-world road damage images, evaluate their accuracy, and analyze trade-offs in speed and precision. The dataset consists of annotated road images from multiple countries, including India and Japan.

## Objectives

- Detect and classify different types of road damage
- Compare YOLOv8 and Faster R-CNN on the same dataset
- Analyze performance using metrics like mAP, precision, recall, and inference speed

## Dataset

- Images sourced from India and Japan
- Provided in XML annotation format
- Converted into:
  - YOLO `.txt` format for YOLOv8
  - COCO `.json` format for Detectron2

## Key Contributions

- Data cleaning and augmentation to address class imbalance
- Conversion of annotations into YOLO and COCO formats
- Custom scripts for:
  - Data preprocessing
  - Annotation conversion
  - Train-test splitting
- Training YOLOv8 with Mosaic Augmentation and Focal Loss
- Training Faster R-CNN using Detectron2
- Initial attempts at EfficientDet training using TensorFlow

## Approach

| Model           | Description |
|----------------|-------------|
| **YOLOv8**      | Real-time detector using a single-stage architecture. Implemented via [Ultralytics](https://github.com/ultralytics/ultralytics). |
| **Faster R-CNN** | Two-stage detector using RPN. Implemented with [Detectron2](https://github.com/facebookresearch/detectron2). |

## Experimental Setup

- Train/Test Split: 80/20
- Evaluation Metric: mAP (mean Average Precision)
- Tools: Google Colab with T4/A100 GPU
- Visualizations: Confusion matrices, bar charts for mAP/Precision/Recall

## Results Summary

| Metric                     | YOLOv8       | Faster R-CNN |
|---------------------------|--------------|--------------|
| mAP@0.5                   | **92.41%**   | 73.22%       |
| mAP@0.5:0.95              | **66.21%**   | 40.15%       |
| Precision                 | **91.23%**   | 40.15%       |
| Recall                    | **85.42%**   | 55.34%       |
| Fitness Score             | **0.6883**   | 0.4521       |
| Inference Time (ms/frame)| 115.10       | **50.08**    |
| FPS                       | 8.69         | **19.97**    |

YOLOv8 outperformed Faster R-CNN in accuracy and generalization, while Faster R-CNN was faster in inference speed during evaluation.

## Challenges with EfficientDet

EfficientDet training was attempted using TensorFlow but not completed due to:

- Complex TFRecord conversions
- Tedious pipeline configuration
- Colab runtime and compatibility issues

## Sample Outputs

- YOLOv8 and Detectron2 predictions visualized on test samples
- Confusion matrices showing class-level accuracy
- Comparative bar charts for all metrics

## Lessons Learned

- Proper dataset organization and augmentation significantly improves model performance
- YOLOv8 is better suited for production-ready pipelines due to its ease of training and high precision
- Detectron2 provides flexible architecture and faster inference, useful for experimentation and analysis
- Background misclassification can heavily affect recall scores, especially in two-stage detectors

## Future Work

- Retry EfficientDet training with smaller model configs
- Test larger YOLOv8 variants (YOLOv8m, YOLOv8l)
- Deploy models via Streamlit interface for real-time visualization

## References

1. [Ultralytics YOLOv8 GitHub](https://github.com/ultralytics/ultralytics)  
2. [Detectron2 GitHub](https://github.com/facebookresearch/detectron2)  
3. [TensorFlow Object Detection API](https://github.com/tensorflow/models)  
4. [YOLOv8 Guide - Augmented Startups](https://www.youtube.com/watch?v=V9bVbJADpP4)  
5. [Detectron2 Training Guide](https://towardsdatascience.com/detectron2-train-custom-dataset)  

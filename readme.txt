
===========================================
Road Damage Detection - YOLOv8 & Detectron2
===========================================

Author: Surya Venkata Rohit Moganti
UBID: 50560088

Note: I have follwed a different directory structure in google colab and it cannot be replicated in the local machine.
I am attaching the code.ipynb in code folder which has clear details on how the code is being executed
The submission limit is just 2Gb but my dataset size is around 2.8GB and because of this I wont be able to submit the dataset
Use the following links to download the dataset and place in folder raw_dataset
'''
https://bigdatacup.s3.ap-northeast-1.amazonaws.com/2022/CRDDC2022/RDD2022/Country_Specific_Data_CRDDC2022/RDD2022_Japan.zip
https://bigdatacup.s3.ap-northeast-1.amazonaws.com/2022/CRDDC2022/RDD2022/Country_Specific_Data_CRDDC2022/RDD2022_India.zip
https://bigdatacup.s3.ap-northeast-1.amazonaws.com/2022/CRDDC2022/RDD2022/Country_Specific_Data_CRDDC2022/RDD2022_Czech.zip
https://bigdatacup.s3.ap-northeast-1.amazonaws.com/2022/CRDDC2022/RDD2022/Country_Specific_Data_CRDDC2022/RDD2022_China_MotorBike.zip
https://bigdatacup.s3.ap-northeast-1.amazonaws.com/2022/CRDDC2022/RDD2022/Country_Specific_Data_CRDDC2022/RDD2022_United_States.zip
'''
 I used countries ["China_MotorBike","Czech","India","Japan","United_States"]

------------------------------------------------
 Project Structure
------------------------------------------------
Code/
├── run.sh                  # Shell script to run the complete pipeline
├── clean_aug.ipynb         # Data augmentation and preprocessing (converted to .py during run)
├── organize.py             # Consolidates all countries' data into a single dataset
├── code.py                 # Main training and evaluation script (YOLO & Detectron2)
├── dataset_raw/            # Original dataset (with subfolders per country)
├── dataset_organized/      # Output of organize.py - all images and annotations combined
├── dataset_augmented/      # Augmented images saved here after clean_aug.ipynb
├── dataset_yolo/           # YOLO-specific split dataset (train/test) & YAML
├── dataset_coco/           # COCO-format dataset (train/test JSONs)
├── yolo_runs/              # YOLOv8 training outputs
└── detectron_runs/         # Detectron2 training outputs and evaluations

------------------------------------------------
 Setup Instructions
------------------------------------------------

This project is designed to run on **Google Colab** (for GPU acceleration). If running locally, make sure Python ≥3.8 and a CUDA-compatible GPU are available.

Step 1: Clone or extract this folder

Step 2: Ensure the following dependencies are installed:

```bash
pip install -U torch torchvision ultralytics
pip install -U 'git+https://github.com/facebookresearch/detectron2.git'
pip install tensorflow==2.12.0 tensorflow-estimator==2.12.0 tf_slim protobuf==3.20.3
pip install tqdm lxml pycocotools

Step 3: In your local machine the code starts with dataset_raw and after executing the organize.py the dataset is dataset_organized

Step 4: This dataset_organized is converted to dataset_augmented by executing clean_aug.ipynb

Step 5: The dataset_augmented folder has to be uploaded to google drive and in the same directory the code.ipynb has to be executed for the models to appear there itself.


------------------------------------------------
 Execute Instructions
------------------------------------------------

Step 1: chmod +x run.sh

Step 2: ./run.sh


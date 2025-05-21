#!/bin/bash

# Exit on error
set -e

echo " Starting Road Damage Detection Pipeline..."

echo " Converting clean_aug.ipynb to clean_aug.py..."
jupyter nbconvert --to script clean_aug.ipynb --output clean_aug

echo " Running Data Cleaning and Augmentation..."
python3 clean_aug.py

echo " Organizing Dataset..."
python3 organize.py

echo " Running Main Detection Pipeline..."
python3 code.py

echo " All steps completed successfully!"
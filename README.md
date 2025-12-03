# Image Labeler using Amazon Rekognition

This project demonstrates how to use **Amazon Rekognition** with **Python** to detect labels in images stored in an **S3 bucket**.

## Features
- Upload images to Amazon S3
- Use Amazon Rekognition to detect labels
- Display detected labels with confidence percentage

## Requirements
- Python 3.8+
- AWS account with Access Key and Secret Key
- boto3 library

## Setup Instructions

1. **Clone the repository:**
```bash
git clone https://github.com/Faizah-55/ImageLabeler.git


2- Create a virtual environment (optional but recommended):
python -m venv .venv
source .venv/Scripts/activate  # Git Bash
# or
.\.venv\Scripts\activate       # CMD
 
 3- Install dependencies:

pip install -r requirements.txt

4- Configure AWS CLI: 
aws configure
 
 5- Update image_labeler.py with your S3 bucket name and image file name.

 6-Run the script: 
 python image_labeler.py

Example Output: 

Detected Labels:
Cat - Confidence: 98.31%
Pet - Confidence: 93.12%
Animal - Confidence: 90.14%

# 🖼️ Image Labeler using Amazon Rekognition

This project demonstrates how to use **AWS Rekognition** with **Python** to automatically detect and label objects inside images stored in an **Amazon S3 bucket**.

The goal of this project is to show:
- How to use AWS services (S3 + Rekognition)
- How Python interacts with cloud services
- How to build a simple real-world machine learning application

---

## 🚀 Project Features
- Upload an image to Amazon S3  
- Use Amazon Rekognition to detect labels  
- Print detected labels + confidence score  
- Simple Python code (beginner friendly)

---

## 📁 Project Structure



ImageLabeler/
│── image_labeler.py
│── requirements.txt
│── README.md



---

## 🛠️ Requirements

Before running the project, install:

- Python 3.8+
- AWS Account
- AWS CLI installed
- boto3 library

---

## 🔧 Installation & Setup (Step by Step)

### 1️⃣ Clone the repository
```bash
git clone https://github.com/# 🖼️ Image Labeler using Amazon Rekognition

This project demonstrates how to use **AWS Rekognition** with **Python** to automatically detect and label objects inside images stored in an **Amazon S3 bucket**.

The goal of this project is to show:
- How to use AWS services (S3 + Rekognition)
- How Python interacts with cloud services
- How to build a simple real-world machine learning application

---

## 🚀 Project Features
- Upload an image to Amazon S3  
- Use Amazon Rekognition to detect labels  
- Print detected labels + confidence score  
- Simple Python code (beginner friendly)

---

## 📁 Project Structure



ImageLabeler/
│── image_labeler.py
│── requirements.txt
│── README.md
│── example_output.png ← your image example


---

## 🛠️ Requirements

Before running the project, install:

- Python 3.8+
- AWS Account
- AWS CLI installed
- boto3 library

---

## 🔧 Installation & Setup (Step by Step)

### 1️⃣ Clone the repository
```bash
git clone https://github.com/your-username/ImageLabeler.git
cd ImageLabeler

2️⃣ Create virtual environment (optional but recommended)
python -m venv .venv
source .venv/Scripts/activate   # Git Bash
# or
.\.venv\Scripts\activate        # CMD / PowerShell

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Configure AWS CLI
aws configure


Enter your:

AWS Access Key

AWS Secret Key

Default region (example: us-east-1)

Default output format: json

5️⃣ Update image_labeler.py

Open image_labeler.py and update:

bucket_name → your S3 bucket name

image_name → the image file in the bucket

6️⃣ Run the script
python image_labeler.py

📸 Example Output
Detected Labels:
Cat - Confidence: 98.31%
Pet - Confidence: 93.12%
Animal - Confidence: 90.14%





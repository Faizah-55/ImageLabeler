import boto3

rekognition = boto3.client('rekognition')

def detect_labels(bucket, image):
    response = rekognition.detect_labels(
        Image={'S3Object': {'Bucket': bucket, 'Name': image}},
        MaxLabels=10
    )
    print(f"Labels for {image}:")
    for label in response['Labels']:
        print(f"- {label['Name']} ({label['Confidence']:.2f}%)")

def main():
    bucket = 'image-labeler-bucket1'
    image = 'cat.jpg'
    detect_labels(bucket, image)

if __name__ == "__main__":
    main()

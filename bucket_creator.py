import boto3
from botocore.exceptions import ClientError
from dotenv import load_dotenv
import os

load_dotenv()

BASE_NAME = os.getenv('BASE_NAME')
REGION = os.getenv('REGION')

def create_bucket(bucket_name: str, region: str):
    try:
        s3 = boto3.client("s3", region_name=region)
        s3.create_bucket(
            Bucket=bucket_name,
            CreateBucketConfiguration={"LocationConstraint": region}
        )
        print(f"Bucket creado: s3://{bucket_name}")
    except ClientError as e:
        if e.response['Error']['Code'] == 'BucketAlreadyOwnedByYou':
            print(f"Bucket ya existe: s3://{bucket_name}")
        else:
            print(f"Error: {e}")
            raise

if __name__ == "__main__":
    buckets = ['raw', 'stage', 'consume']
    for bucket_type in buckets:
        bucket_name = f"{BASE_NAME}-{bucket_type}"
        create_bucket(bucket_name, REGION)


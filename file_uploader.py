
from pathlib import Path
from dotenv import load_dotenv
import boto3
import os


load_dotenv()

BASENAME = os.getenv('BASE_NAME')
s3 = boto3.client('s3')

def upload_files_from_folder(folder: str):
    base_path = Path(folder)
    prefix = 'raw'

    if not base_path.exists():
        raise FileNotFoundError(f"La carpeta '{folder}' no existe.")

    for file_path in base_path.iterdir():
        if file_path.is_file():
            file_name = file_path.name
            name_without_ext = file_path.stem
            s3_key = f"{name_without_ext}/{file_name}"

            print(f"Subiendo {file_path} a s3://{BASENAME}-{prefix}/{s3_key}")
            s3.upload_file(str(file_path), f"{BASENAME}-{prefix}", s3_key)

    print("Subida finalizada.")

if __name__ == "__main__":
    upload_files_from_folder("files")

    
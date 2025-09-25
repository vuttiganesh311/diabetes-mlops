import shutil
import os

def ingest_file(source_path, dest_folder):
    os.makedirs(dest_folder, exist_ok=True)
    dest_path = os.path.join(dest_folder, os.path.basename(source_path))
    shutil.copy(source_path, dest_path)
    print(f"File copied to: {dest_path}")
    return dest_path

if __name__ == "__main__":
    ingest_file("data/raw/diabetes.csv", "data/raw/")
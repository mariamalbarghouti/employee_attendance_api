import cv2
import face_recognition
import requests
from io import BytesIO
import os

def download_image(url):
    response = requests.get(url)
    if response.status_code == 200:
        image = face_recognition.load_image_file(BytesIO(response.content))
        return image
    else:
        raise Exception(f"Failed to download image from {url}")

def load_local_image(image_path):
    if os.path.exists(image_path):
        image = face_recognition.load_image_file(image_path)
        return image
    else:
        raise Exception(f"Image at path {image_path} not found")

def compare_faces(encoding_url, encoding_local):
    results = face_recognition.compare_faces([encoding_url], encoding_local)
    return results[0]

def format_filename(filename):
    name, ext = os.path.splitext(filename)
    name = name.replace('_', ' ').strip()
    return name

def find_matching_face(image_url, db_folder_path):
    # تحميل صورة المستخدم من الرابط
    image_url = download_image(image_url)
    encoding_url = face_recognition.face_encodings(image_url)
    if not encoding_url:
        raise Exception("No faces found in the URL image.")
    encoding_url = encoding_url[0]

    # التكرار على كل الصور في قاعدة البيانات
    for filename in os.listdir(db_folder_path):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            local_image_path = os.path.join(db_folder_path, filename)
            image_local = load_local_image(local_image_path)
            encoding_local = face_recognition.face_encodings(image_local)
            if not encoding_local:
                print(f"No faces found in the local image {filename}. Skipping.")
                continue
            encoding_local = encoding_local[0]

            if compare_faces(encoding_url, encoding_local):
                formatted_name = format_filename(filename)
                return True, formatted_name

    return False, None

# Example image URL
image_url = 'https://cdn.elbashayer.com/elbashayer/uploads/2021/09/elbashayer-2021-09-17_107414.jpg'
db_folder_path = '../../media/images/'

is_found, matching_image = find_matching_face(image_url, db_folder_path)
if is_found:
    print(f"The face in the provided image matches with the image: {matching_image}")
else:
    print("No matching face found in the database.")

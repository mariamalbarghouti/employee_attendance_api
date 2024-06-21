import face_recognition
from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import Item
from .serializers import ItemSerializer, ImageSerializer ,ImageComparisonSerializer
import requests
from io import BytesIO
from io import BytesIO
import os
import numpy as np
from PIL import Image
@api_view(['GET'])
def getData(request):
    items = Item.objects.all()
    serializer = ItemSerializer(items, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addItem(request):
    serializer = ItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

# ImageSerializer

@api_view(['POST'])
def addImage(request):
    serializer = ImageSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


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

def find_matching_face(person_image, db_folder_path):
    encoding_employee = face_recognition.face_encodings(person_image)
    if not encoding_employee:
        raise Exception("No faces found in the uploaded image.")
    encoding_employee = encoding_employee[0]

    for filename in os.listdir(db_folder_path):
        local_image_path = os.path.join(db_folder_path, filename)
        image_local = load_local_image(local_image_path)
        encoding_local = face_recognition.face_encodings(image_local)
        if not encoding_local:
            print(f"No faces found in the local image {filename}. Skipping.")
            continue
        encoding_local = encoding_local[0]

        if face_recognition.compare_faces([encoding_employee], encoding_local)[0]:
            formatted_name = format_filename(filename)
            return True, formatted_name

    return False, None


@api_view(['POST'])
def compareFaces(request):
    try:
        serializer = ImageComparisonSerializer(data=request.data)
        if serializer.is_valid():
            person_image = serializer.validated_data['person']
            person_image = Image.open(person_image)
            person_image = np.array(person_image)
            is_found, employee_name = find_matching_face(person_image, 'media/images/')
            print(f"is_found: {is_found}, employee_name {employee_name}")
            return Response({"is_found": is_found, "employee_name": employee_name}, status=201)
        return Response({"error": 'Serialization Error'}, status=400)
    except Exception as e:
        return Response({"error": str(e)}, status=400)

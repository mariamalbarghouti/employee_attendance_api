# import cv2
# import face_recognition
# import requests
# from io import BytesIO
#
# def download_image(url):
#     response = requests.get(url)
#     if response.status_code == 200:
#         image = face_recognition.load_image_file(BytesIO(response.content))
#         return image
#     else:
#         raise Exception(f"Failed to download image from {url}")
#
# def compare_faces(image_url_1, image_url_2):
#     image_1 = download_image(image_url_1)
#     image_2 = download_image(image_url_2)
#
#     encoding_1 = face_recognition.face_encodings(image_1)[0]
#     encoding_2 = face_recognition.face_encodings(image_2)[0]
#
#     results = face_recognition.compare_faces([encoding_1], encoding_2)
#     return results[0]
#
# # Example image URLs
# image_url_1 = 'https://i.pinimg.com/564x/27/7f/07/277f07919d765dd619e62da00fa5a5fb.jpg'
# image_url_2 = 'https://i.pinimg.com/564x/17/b2/0a/17b20abeaeb26eba52f904849e81b97a.jpg'
#
# are_same_person = compare_faces(image_url_1, image_url_2)
# if are_same_person:
#     print("The faces in both images are of the same person.")
# else:
#     print("The faces in both images are of different persons.")

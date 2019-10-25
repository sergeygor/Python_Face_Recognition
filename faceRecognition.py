import face_recognition

# Get image
image = face_recognition.load_image_file('unknownFace/group01.jpg')
# Get faces
face_location = face_recognition.face_locations(image)
# Array of coordinates of each face
print(face_location)
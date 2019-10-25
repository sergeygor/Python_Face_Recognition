import face_recognition

image_of_Einstein = face_recognition.load_image_file('knownFace/Albert Einstein.jpg')
einstain_face_encoding = face_recognition.face_encodings(image_of_Einstein)[0]

unknown_image = face_recognition.load_image_file('unknownFace/un01.jpg')
unknown_face_encoding = face_recognition.face_encodings(unknown_image)[0]

# Compare faces
result = face_recognition.compare_faces([einstain_face_encoding], unknown_face_encoding)

if result[0]:
    print('Albert Einstein was found!')
else:
    print('Albert Einstein was NOT FOUND!')

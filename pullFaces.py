from PIL import Image
import face_recognition

# Get image
image = face_recognition.load_image_file('unknownFace/group01.jpg')
face_locations = face_recognition.face_locations(image)

# Loop through face_location
for face_location in face_locations:
    top, right, bottom, left = face_location

    # Get image in the form of an array that we can get actual image using pillow library
    face_image = image[top:bottom, left:right]
    pil_image = Image.fromarray(face_image)

    # pil_image.show()
    pil_image.save(f'unpackImages/{top}.jpg')

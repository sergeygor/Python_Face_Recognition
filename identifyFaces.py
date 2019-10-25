import face_recognition
from PIL import Image, ImageDraw

image_of_Elizabeth = face_recognition.load_image_file('knownFace/Elizabeth .jpg')
elizabeth_face_encoding = face_recognition.face_encodings(image_of_Elizabeth)[0]

# Create array of encodings and names
known_face_encodings = [
    elizabeth_face_encoding
]

known_face_names = [
    'Elizabeth'
]
# Load test image to find face in it
test_image = face_recognition.load_image_file('unknownFace/group02.jpg')

# Find faces in test image
face_locations = face_recognition.face_locations(test_image)
face_encoding = face_recognition.face_encodings(test_image, face_locations)

# Convert to PIL format
pil_image = Image.fromarray(test_image)

# Create a ImageDraw instance
draw = ImageDraw.Draw(pil_image)

# Loop thought faces in test image
for (top, right, bottom, left), face_encoding in zip(face_locations, face_encoding):
    matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

    name = 'Unknown Person'

    # If match
    if True in matches:
        first_match_index = matches.index(True)
        name = known_face_names[first_match_index]

    # Draw the box
    draw.rectangle(((left, top), (right, bottom)), outline=(0, 0, 0))

    # Draw label
    text_width, text_height = draw.textsize(name)
    draw.rectangle(((left, bottom - text_height - 10), (right, bottom)), fill=(0, 0, 0), outline=(0, 0, 0))

    # Draw text
    draw.text((left + 6, bottom - text_height - 5), name, fill=(255, 255, 255, 255))

del draw
# Display image
pil_image.show()

# Save image
pil_image.save('unpackImages/identify.jpg')

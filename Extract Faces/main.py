# Required Libraries
import cv2
import sys

# argv[] function to get
# the path of the image
PathOfImage = sys.argv[1]

# Converting the image into
# Black and white
img = cv2.imread(PathOfImage)
blackandwhite = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Using Cascade Library
# From cv2
faceCascadeLib = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# Detecting Faces with size
# Bigger than (30,30) pixels
faces_detected = faceCascadeLib.detectMultiScale(
    blackandwhite,
    scaleFactor=1.3,
    minNeighbors=3,
    minSize=(30, 30)
)

# No. of faces found
print("We Found {} Faces in the Image.".format(len(faces_detected)))

# Now Crop the detected face
# in rectangle format
for (a, b, w, h) in faces_detected:
    cv2.rectangle(img, (a, b), (a + w, b + h), (0, 255, 0), 2)
    cropped_color = img[b:b + h, a:a + w]
    
    # Save the cropped image
    print("Face found. Saving cropped Image.")
    cv2.imwrite(str(w) + str(h) + '_face.jpg', cropped_color)
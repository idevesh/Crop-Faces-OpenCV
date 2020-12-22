# Crop-Faces-OpenCV

In this tutorial, we will write a script that uses OpenCV and Python to extract faces from an input image. We will be using the pre-trained model to detect faces named Haar Cascade on Github.

## Prerequisite for this topic -

1. Python 3 installed on your system
2. Numpy Library
3. OpenCV Library

## Approach:

1. First, we will load the required libraries into the python file ( NumPy, OpenCV, etc.).
2. Now, create a variable to store the path of the image using the sys.argv[] function.
3. Read the image file using the cv2.imread() function.
4. Convert the image to black and white using the cv2.cvtColor() function as the Haar cascade only works on the gray images.
5. Load the Haar cascade from the cv2 library and store it in a variable.
6. Now, detect faces from the image using the detectMultiScale() function from the cv2 library.
7. Then, we will use the cv2.rectangle() function to create a rectangle around the detected face.
8. Now, save the image file using the cv2.imwrite() function with the name of your choice.

## Terms Used in code
1. scaleFactor: This variable is used to reduce the image size at each image scale to improve the detection of the faces.
2. minNeighbors: This variable is used to specify how many faces in a rectangle can reside in it. Too high value can Ignore True Positives. So we will be using 3(value) to reduce all false positives.
3. minSize:  This variable is used to define the minimum possible face size (in pixels). Smaller values will be ignored and all values higher than this will be considered.



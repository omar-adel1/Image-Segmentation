import cv2
import numpy as np

# Load the image
image = cv2.imread('flfl.jpg')

# Convert the image from BGR to RGB (OpenCV uses BGR by default)
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Define the range of red color in HSV
lower_red = np.array([0, 50, 50])
upper_red = np.array([10, 255, 255])

# Define the range of green color in HSV (expanded ranges)
lower_green = np.array([35, 50, 50])
upper_green = np.array([90, 255, 255])

# Convert the image to HSV color space
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Threshold the HSV image to get only red and green colors
mask_red = cv2.inRange(hsv_image, lower_red, upper_red)
mask_green = cv2.inRange(hsv_image, lower_green, upper_green)

# Find contours for red objects
contours_red, _ = cv2.findContours(mask_red, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Find contours for green objects
contours_green, _ = cv2.findContours(mask_green, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Draw bounding boxes around red objects
for contour in contours_red:
    x, y, w, h = cv2.boundingRect(contour)
    cv2.rectangle(image_rgb, (x, y), (x + w, y + h), (255, 0, 0), 2)

# Draw bounding boxes around green objects
for contour in contours_green:
    x, y, w, h = cv2.boundingRect(contour)
    cv2.rectangle(image_rgb, (x, y), (x + w, y + h), (0, 255, 0), 2)

# Display the image with bounding boxes
cv2.imshow('Bounding Boxes', cv2.cvtColor(image_rgb, cv2.COLOR_RGB2BGR))
cv2.waitKey(0)
cv2.destroyAllWindows()

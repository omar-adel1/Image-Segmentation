import cv2
import numpy as np
import matplotlib.pyplot as plt

# Constants for color ranges
RED_LOWER1 = np.array([0, 100, 20])
RED_UPPER1 = np.array([10, 255, 255])
RED_LOWER2 = np.array([160, 100, 20])
RED_UPPER2 = np.array([179, 255, 255])

GREEN_LOWER1 = np.array([35, 50, 50])
GREEN_UPPER1 = np.array([70, 255, 255])
GREEN_LOWER2 = np.array([71, 50, 50])
GREEN_UPPER2 = np.array([90, 255, 255])

def load_rgb_image(image_path):
    """Load an image from the specified path."""
    img = cv2.imread(image_path)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    return img_rgb

def apply_color_threshold(hsv_img, lower_range, upper_range):
    """Apply color thresholding to the HSV image."""
    mask = cv2.inRange(hsv_img, lower_range, upper_range)
    return mask

def draw_bounding_boxes(img, contours, color):
    """Draw bounding boxes around the detected objects."""
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
    return img

def main():
    # Load the image
    image_path = './images/emerald.jpg'
    img_rgb = load_rgb_image(image_path)

    # Convert the image to HSV color space
    hsv_img = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2HSV)

    # Apply color thresholding to detect red and green colors
    red_mask = apply_color_threshold(hsv_img, RED_LOWER1, RED_UPPER1) + \
               apply_color_threshold(hsv_img, RED_LOWER2, RED_UPPER2)

    green_mask = apply_color_threshold(hsv_img, GREEN_LOWER1, GREEN_UPPER1) + \
                 apply_color_threshold(hsv_img, GREEN_LOWER2, GREEN_UPPER2)

    """
    -Finds contours in the binary mask full_mask_red representing the red objects.
    -cv2.RETR_EXTERNAL retrieves only the external contours (contours along the outer edge of the object)
    -cv2.CHAIN_APPROX_SIMPLE compresses horizontal, vertical, and diagonal segments, leaving only their end points.
    """
    contours_red, _ = cv2.findContours(red_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours_green, _ = cv2.findContours(green_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Draw bounding boxes around red and green objects
    if contours_red:
        img_rgb = draw_bounding_boxes(img_rgb, contours_red, (255, 0, 0))
    if contours_green:
        img_rgb = draw_bounding_boxes(img_rgb, contours_green, (0, 255, 0))

    # Display the image with bounding boxes
    plt.imshow(img_rgb)
    plt.axis('off')  # Turn off axis
    plt.show()

if __name__ == "__main__":
    main()

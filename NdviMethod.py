import cv2
import numpy as np
import matplotlib.pyplot as plt

def calculate_vegetation_percentage(image_path):
    # Read the image
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError("Image not found or unable to read")

    # Convert the image from BGR to HSV color space
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Define the range for green color in HSV space
    lower_green = np.array([40, 160, 45])
    upper_green = np.array([255, 255, 255])

    # Create a mask that isolates the green areas
    mask = cv2.inRange(hsv_image, lower_green, upper_green)

    # Calculate the percentage of the image that is vegetation
    vegetation_pixels = cv2.countNonZero(mask)
    total_pixels = image.shape[0] * image.shape[1]
    vegetation_percentage = (vegetation_pixels / total_pixels) * 100

    return vegetation_percentage

# Use ndvi image
image_path = "Delhi.jpg"
vegetation_percentage = calculate_vegetation_percentage(image_path)

print(f'Vegetation cover: {vegetation_percentage:.2f}%')

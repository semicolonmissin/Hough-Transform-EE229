import cv2
import numpy as np
import matplotlib.pyplot as plt


# Provide the image path manually
image_path = 'iitb.jpg'  # Replace with your actual image path


# Read the image from the local file
image = cv2.imread(image_path)


# Check if the image was loaded successfully
if image is None:
    print("Error: Image not found or could not be loaded.")
else:
    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


    # Apply a Gaussian blur to the image
    blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)


    # Detect edges using the Canny edge detection algorithm
    edges = cv2.Canny(blurred_image, 100, 200)


    # Display the original and processed images
    plt.figure(figsize=(10, 7))


    plt.subplot(2, 2, 1)
    plt.title('Original Image')
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.axis('off')


    plt.subplot(2, 2, 2)
    plt.title('Grayscale Image')
    plt.imshow(gray_image, cmap='gray')
    plt.axis('off')


    plt.subplot(2, 2, 3)
    plt.title('Blurred Image')
    plt.imshow(blurred_image, cmap='gray')
    plt.axis('off')


    plt.subplot(2, 2, 4)
    plt.title('Edge Detection')
    plt.imshow(edges, cmap='gray')
    plt.axis('off')


    plt.tight_layout()
    plt.show()

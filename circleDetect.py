import cv2
import numpy as np

# Load the image
image = cv2.imread("planets.jpg")
# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Gaussian blur to reduce noise and improve circle detection
blurred = cv2.GaussianBlur(gray, (9, 9), 2)

# Use HoughCircles to detect circles
circles = cv2.HoughCircles(blurred, cv2.HOUGH_GRADIENT, dp=1, minDist=30,
                           param1=50, param2=30, minRadius=0, maxRadius=0)

# If circles are detected
if circles is not None:
    circles = np.uint16(np.around(circles))
    for circle in circles[0, :]:
        # Get the center coordinates and radius of each circle
        center = (circle[0], circle[1])
        radius = circle[2]
        # Draw the circle center
        cv2.circle(image, center, 1, (0, 255, 0), 3)
        # Draw the circle outline
        cv2.circle(image, center, radius, (255, 0, 0), 2)

# Save the result to a file
cv2.imwrite("Output5.jpg", image)

# Optionally, display the result
cv2.imshow("Detected Circles", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

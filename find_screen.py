import cv2
import numpy as np

# Load the mockup image
img = cv2.imread('C:/Users/junio/Desktop/Boomo_Post_Instagram.jpg')

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply blur and edge detection
blur = cv2.GaussianBlur(gray, (5, 5), 0)
edges = cv2.Canny(blur, 50, 150)

# Find contours
contours, _ = cv2.findContours(edges, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
contours = sorted(contours, key=cv2.contourArea, reverse=True)[:5]

screen_contour = None
for c in contours:
    # Approximate the contour
    peri = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.02 * peri, True)
    
    # If our approximated contour has four points, we can assume it is the screen
    if len(approx) == 4:
        screen_contour = approx
        break

if screen_contour is not None:
    print("Found a screen contour at:")
    for pt in screen_contour:
        print(pt[0])
else:
    print("No screen contour found.")

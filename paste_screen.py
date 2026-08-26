import cv2
import numpy as np

# Load images
bg = cv2.imread('C:/Users/junio/Desktop/Boomo_Post_Instagram.jpg')
fg = cv2.imread('C:/Users/junio/Desktop/Boomo_Site_Real.png')

if bg is None or fg is None:
    print("Could not load images.")
    exit(1)

# Destination points in the background image (the 4 corners of the laptop screen)
# Order: Top-Left, Top-Right, Bottom-Right, Bottom-Left
pts_dst = np.array([
    [426, 415], # Top-Left
    [814, 429], # Top-Right
    [788, 722], # Bottom-Right
    [397, 683]  # Bottom-Left
], dtype="float32")

h, w = fg.shape[:2]

# Source points in the foreground image (the 4 corners of the screenshot)
pts_src = np.array([
    [0, 0],       # Top-Left
    [w, 0],       # Top-Right
    [w, h],       # Bottom-Right
    [0, h]        # Bottom-Left
], dtype="float32")

# Calculate Perspective Transform Matrix
M = cv2.getPerspectiveTransform(pts_src, pts_dst)

# Warp the foreground image to fit the background image
warped_fg = cv2.warpPerspective(fg, M, (bg.shape[1], bg.shape[0]))

# Create a mask of the warped foreground
mask = np.zeros((bg.shape[0], bg.shape[1]), dtype=np.uint8)
cv2.fillConvexPoly(mask, np.int32(pts_dst), 255)

# Smooth the edges of the mask slightly
mask = cv2.GaussianBlur(mask, (3, 3), 0)

# Convert mask to 3 channels
mask_3ch = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR) / 255.0

# Blend the images
bg_float = bg.astype(float)
warped_fg_float = warped_fg.astype(float)

blended = (bg_float * (1.0 - mask_3ch)) + (warped_fg_float * mask_3ch)

# Ensure the output is valid uint8
final_img = np.clip(blended, 0, 255).astype(np.uint8)

# Add a slight dark overlay to make the screen look more realistic (emulating screen glare/brightness)
# Actually, let's keep it bright since it's an OLED look
# Save the result
cv2.imwrite('C:/Users/junio/Desktop/Boomo_Post_Final.jpg', final_img)
print("Saved to Boomo_Post_Final.jpg")

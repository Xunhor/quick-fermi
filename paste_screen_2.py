import cv2
import numpy as np

bg = cv2.imread('C:/Users/junio/Desktop/Boomo_Post_Instagram.jpg')
fg = cv2.imread('C:/Users/junio/Desktop/Boomo_Site_Real.png')

pts_dst = np.array([
    [428, 417], # Top-Left
    [802, 423], # Top-Right
    [777, 712], # Bottom-Right
    [399, 679]  # Bottom-Left
], dtype="float32")

h, w = fg.shape[:2]
pts_src = np.array([
    [0, 0],
    [w, 0],
    [w, h],
    [0, h]
], dtype="float32")

M = cv2.getPerspectiveTransform(pts_src, pts_dst)
warped_fg = cv2.warpPerspective(fg, M, (bg.shape[1], bg.shape[0]))

mask = np.zeros((bg.shape[0], bg.shape[1]), dtype=np.uint8)
cv2.fillConvexPoly(mask, np.int32(pts_dst), 255)
mask = cv2.GaussianBlur(mask, (3, 3), 0)
mask_3ch = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR) / 255.0

bg_float = bg.astype(float)
warped_fg_float = warped_fg.astype(float)

blended = (bg_float * (1.0 - mask_3ch)) + (warped_fg_float * mask_3ch)
final_img = np.clip(blended, 0, 255).astype(np.uint8)

cv2.imwrite('C:/Users/junio/Desktop/Boomo_Post_Final.jpg', final_img)

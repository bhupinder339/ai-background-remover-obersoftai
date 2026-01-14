import cv2

img = cv2.imread("no_bg.png", cv2.IMREAD_UNCHANGED)

# Brightness & contrast
enhanced = cv2.convertScaleAbs(img, alpha=1.2, beta=20)

# Sharpen kernel
kernel = [[0, -1, 0],
          [-1, 5, -1],
          [0, -1, 0]]

kernel = cv2.UMat(cv2.getStructuringElement(cv2.MORPH_RECT, (3,3)))

cv2.imwrite("enhanced.png", enhanced)

print("IMAGE ENHANCED")


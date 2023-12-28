import cv2
import numpy as np

# Load an image
image = cv2.imread("D:\wp2568544.jpg")

# Resize image to 720x1080
image = cv2.resize(image, (720, 600))

# Convert RGB to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Convert grayscale to binary
_, binary_image = cv2.threshold(gray_image, 128, 255, cv2.THRESH_BINARY)

# Convert RGB to binary
_, binary_rgb_image = cv2.threshold(image, 128, 255, cv2.THRESH_BINARY)

# Convert RGB to HSV
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Convert HSV to RGB
rgb_from_hsv_image = cv2.cvtColor(hsv_image, cv2.COLOR_HSV2BGR)

# Convert RGB to YCbCr
yuv_image = cv2.cvtColor(image, cv2.COLOR_BGR2YCrCb)

# Convert YCbCr to RGB
rgb_from_yuv_image = cv2.cvtColor(yuv_image, cv2.COLOR_YCrCb2BGR)

# Save the converted images
cv2.imwrite('gray_image.jpg', gray_image)
cv2.imwrite('binary_image.jpg', binary_image)
cv2.imwrite('binary_rgb_image.jpg', binary_rgb_image)
cv2.imwrite('hsv_image.jpg', hsv_image)
cv2.imwrite('rgb_from_hsv_image.jpg', rgb_from_hsv_image)
cv2.imwrite('yuv_image.jpg', yuv_image)
cv2.imwrite('rgb_from_yuv_image.jpg', rgb_from_yuv_image)

# Display the images
cv2.imshow('Gray Image', gray_image)
cv2.imshow('Binary Image', binary_image)
cv2.imshow('Binary RGB Image', binary_rgb_image)
cv2.imshow('HSV Image', hsv_image)
cv2.imshow('RGB from HSV Image', rgb_from_hsv_image)
cv2.imshow('YUV Image', yuv_image)
cv2.imshow('RGB from YUV Image', rgb_from_yuv_image)

# Wait for a key press and close all windows
cv2.waitKey(0)
cv2.destroyAllWindows()

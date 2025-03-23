import cv2
import numpy as np
import matplotlib.pyplot as plt

image1 = cv2.imread("assets/my_image1.png")

if image1 is None:
    print("image1 failed")
    exit()

gray_image1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)

# -----------------------------------
colors = ('b', 'g', 'r')
plt.figure(figsize=(12, 6))

for i, color in enumerate(colors):
    hist = cv2.calcHist([image1], [i], None, [256], [0, 256])
    plt.plot(hist, color=color)
    plt.xlim([0, 256])

plt.title("Histogram for RGB Channels (Image 1)")
plt.xlabel("Pixel Value")
plt.ylabel("Frequency")
plt.show()

# -----------------------------------
plt.figure(figsize=(12, 6))
hist_gray1 = cv2.calcHist([gray_image1], [0], None, [256], [0, 256])
plt.plot(hist_gray1, color="black")
plt.title("Histogram for Grayscale Image (Image 1)")
plt.xlabel("Pixel Value")
plt.ylabel("Frequency")
plt.show()

# -----------------------------------
cdf1 = hist_gray1.cumsum()
cdf_normalized1 = cdf1 * hist_gray1.max() / cdf1.max()

plt.figure(figsize=(12, 6))
plt.plot(cdf_normalized1, color='red')
plt.title("Cumulative Distribution Function (CDF) for Image 1")
plt.xlabel("Pixel Value")
plt.ylabel("Cumulative Frequency")
plt.show()

# -----------------------------------
# Histogram Equalization
equalized_image1 = cv2.equalizeHist(gray_image1)

# -----------------------------------
# CLAHE (Contrast Limited Adaptive Histogram Equalization)
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
clahe_image1 = clahe.apply(gray_image1)

# -----------------------------------
# False Color Mapping
color_mapped_image1 = cv2.applyColorMap(gray_image1, cv2.COLORMAP_JET)

# -----------------------------------
image2 = cv2.imread("assets/my_image2.png")

if image2 is None:
    print("image2 failed")
    exit()

gray_image2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

hist1 = cv2.calcHist([gray_image1], [0], None, [256], [0, 256])
hist2 = cv2.calcHist([gray_image2], [0], None, [256], [0, 256])

similarity = cv2.compareHist(hist1, hist2, cv2.HISTCMP_CORREL)
print(f"Similarity between images (Correlation): {similarity}")

# -----------------------------------
cv2.imshow("Original Image (Image 1)", image1)
cv2.imshow("Grayscale Image (Image 1)", gray_image1)
cv2.imshow("Equalized Image (Image 1)", equalized_image1)
cv2.imshow("CLAHE Image (Image 1)", clahe_image1)
cv2.imshow("False Color Image (Image 1)", color_mapped_image1)

cv2.imshow("Original Image (Image 2)", image2)
cv2.imshow("Grayscale Image (Image 2)", gray_image2)

cv2.waitKey(0)
cv2.destroyAllWindows()

# -----------------------------------
hist_diff = np.abs(hist1 - hist2)

plt.figure(figsize=(12, 6))
plt.plot(hist_diff, color="purple")
plt.title("Histogram Difference Between Image 1 and Image 2")
plt.xlabel("Pixel Value")
plt.ylabel("Difference in Frequency")
plt.show()

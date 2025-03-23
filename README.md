# Histogram Homework Project

This project is a Python-based solution that performs various image processing operations, including histogram calculations, contrast enhancement, and image comparison. The goal is to analyze images using histograms and explore techniques such as histogram equalization and CLAHE (Contrast Limited Adaptive Histogram Equalization). It also compares the histograms of two images and visualizes the results.

---

## Table of Contents

- [Project Overview](#project-overview)
- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)
- [Installation Instructions](#installation-instructions)
- [Usage Instructions](#usage-instructions)
- [How to Run the Code](#how-to-run-the-code)
- [Contributing](#contributing)
- [License](#license)

---

## Project Overview

This project takes two images as input and performs the following steps:

1. **Load Images**: Loads two images (my_image1.png and my_image2.png).
2. **Convert to Grayscale**: Converts the images to grayscale for easier analysis.
3. **Histogram Calculation**: Computes and visualizes histograms for both the RGB channels (for the color image) and grayscale images.
4. **CDF Calculation**: Calculates and visualizes the Cumulative Distribution Function (CDF) for grayscale images.
5. **Contrast Enhancement**: Enhances the contrast using histogram equalization and CLAHE techniques.
6. **False Color Mapping**: Applies false color mapping on the grayscale image to give a colorized version.
7. **Image Comparison**: Compares the histograms of the two images to assess their similarity.
8. **Histogram Difference Visualization**: Displays the difference in histograms between the two images.

---

## Technologies Used

- **Python 3.x**
- **OpenCV**: For image processing tasks such as converting to grayscale, histogram calculations, and contrast enhancements.
- **Matplotlib**: For visualizing histograms and images.
- **NumPy**: For numerical operations and array manipulations.

---

## Project Structure

The project follows a simple directory structure:


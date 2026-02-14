# Histogram  Project

This project is a Python-based solution that performs various image processing operations, including histogram calculations, contrast enhancement, and image comparison. The goal is to analyze images using histograms and explore techniques such as histogram equalization and CLAHE (Contrast Limited Adaptive Histogram Equalization). It also compares the histograms of two images and visualizes the results.

---

## Table of Contents

- [Project Overview](#project-overview)
- [Technologies Used](#technologies-used)
- [Installation Instructions](#installation-instructions)
- [Usage Instructions](#usage-instructions)
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

## Screenshots

### Original Images

| Image 1 | Image 2 |
|---------|---------|
| ![Original Image 1](src/images/Original%20Image%20(Image%201).png) | ![Original Image 2](src/images/Original%20Image%20(Image%202).png) |

### Grayscale Conversion

| Grayscale Image 1 | Grayscale Image 2 |
|-------------------|-------------------|
| ![Grayscale Image 1](src/images/Grayscale%20Image%20(Image%201).png) | ![Grayscale Image 2](src/images/Grayscale%20Image%20(Image%202).png) |

### Contrast Enhancement Results

| Equalized Image | CLAHE Image | False Color Image |
|-----------------|-------------|-------------------|
| ![Equalized](src/images/Equalized%20Image%20(Image%201).png) | ![CLAHE](src/images/CLAHE%20Image%20(Image%201).png) | ![False Color](src/images/False%20Color%20Image%20(Image%201).png) |

### Histogram Visualizations

| RGB Histogram | Grayscale Histogram |
|---------------|---------------------|
| ![RGB Histogram](src/images/Figure_1.png) | ![Grayscale Histogram](src/images/Figure_2.png) |

| CDF Visualization | Histogram Difference |
|-------------------|---------------------|
| ![CDF](src/images/Figure_3.png) | ![Histogram Difference](src/images/Figure_4.png) |

## Technologies Used

- **Python 3.x**
- **OpenCV**: For image processing tasks such as converting to grayscale, histogram calculations, and contrast enhancements.
- **Matplotlib**: For visualizing histograms and images.
- **NumPy**: For numerical operations and array manipulations.

---

## Installation Instructions

Follow these steps to set up the project:

1. Clone the repository:

    ```bash
    git clone https://github.com/Abdulrezak-halid/Histogram-homework.git
    cd Histogram-homework
    ```

2. Set up a virtual environment:

    ```bash
    python3 -m venv venv
    source venv/bin/activate   # For Linux/Mac
    venv\Scripts\activate      # For Windows
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

    If you don't have a `requirements.txt`, you can manually install dependencies:

    ```bash
    pip install opencv-python numpy matplotlib
    ```

---

## Usage Instructions

To run the project, simply execute the main script `histogram.py` in your terminal. Make sure the images (`my_image1.png` and `my_image2.png`) are in the correct directory (`images/`).

```bash
python histogram.py
```
## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.





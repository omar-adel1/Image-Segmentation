# Image Segmentation Using HSV Color Space
Image segmentation is a fundamental task in computer vision that involves partitioning an image into multiple segments or regions to simplify its representation and facilitate analysis. In this particular implementation, we perform image segmentation using the HSV (Hue, Saturation, Value) color space.

- [Features](#Features)
- [Implementation](#Implementation)
- [Authors](#Authors)

## Features
- **Color Thresholding**: The code applies color thresholding to an input image in the HSV color space to detect specific colors (red and green in this case).
- **Bounding Box Drawing**: Detected objects are outlined with bounding boxes to highlight their locations in the image.
- **Support for Multiple Color Ranges**: The code accommodates for the variation in color representation by defining multiple lower and upper threshold ranges for each color of interest (red and green).
- **External Contour Detection**: It uses the OpenCV function `cv2.findContours()` with the retrieval mode `cv2.RETR_EXTERNAL` to find only the external contours of objects in the binary masks, which are essentially the outer edges of the detected objects.

## Implementation
- **Dependencies**: The code utilizes the OpenCV library (`cv2`) for image processing tasks and NumPy for array operations. Additionally, it uses Matplotlib (`plt`) for visualizing the results.
- **Loading Image**: The script loads an image from the specified file path using OpenCV's `cv2.imread()` function and then converts it from BGR to RGB color space using `cv2.cvtColor()`.
- **Color Thresholding**: It defines lower and upper HSV ranges for red and green colors and applies color thresholding to the input image to create binary masks for each color.
- **Bounding Box Drawing**: Detected contours from the binary masks are drawn as bounding boxes around the objects using `cv2.rectangle()`.
- **Main Function**: The main function orchestrates the entire process, calling necessary functions in sequence.
- **Execution**: The script can be executed standalone, and upon running, it displays the input image with bounding boxes drawn around detected objects.

## Authors

| Name | GitHub | LinkedIn |
| ---- | ------ | -------- |
| Omar Adel Hassan | [@Omar_Adel](https://github.com/omar-adel1) | [![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/omar-adel-59b707231/) |
| Sharif Ehab | [@Sharif_Ehab](https://github.com/SharifEhab) | [![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/sharif-elmasry-b167a3252/) |
| Mostafa Khaled | [@Mostafa_Khaled](https://github.com/MostafaDarwish93) | [![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/mostafa-darwish-75a29225b/) |
| Bahey Ismail | [@Bahey_Ismail ](https://github.com/Bahey1200022) | [![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/bahey-ismail-1602431a4/) |
| Rawan Abdelnaser | [@Rawan Abdelnaser ](https://github.com/Rowanabdelnasser) | [![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/rawan-abdelnasser-9b7999233/) |


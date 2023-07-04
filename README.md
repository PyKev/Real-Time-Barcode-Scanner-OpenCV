# Real-Time Barcode Scanner

This project consists of a Python program that allows you to scan barcodes in real-time using the camera of a mobile device. To achieve this, it utilizes the "IP Webcam" application available on the Google Play Store, which allows streaming the camera video through an IP address.

## Prerequisites

- Python 3.x installed on your system.
- Additional Python libraries:
  - cv2 (OpenCV): For image processing and barcode detection.
  - playsound: For playing a sound when a valid barcode is detected.
  - pandas: For reading and writing Excel files.
  - tkinter: For creating the graphical user interface.

## Installation

1. Download the source code of the project from this GitHub repository.

2. Install the required Python libraries by running the following command: `pip install cv2 playsound pandas tkinter`

## Usage

1. Download and install the "IP Webcam" application from the Google Play Store on your mobile device.

2. Open the "IP Webcam" application and configure the video streaming options. Make sure to note down the IP address and port displayed on the screen.

3. Run the Python program using the following command:

4. A window with a graphical user interface will appear. Follow these steps:

- Click the "Select file" (Seleccionar archivo) button to choose the Excel file where the detected barcodes will be saved. By default, the program expects an Excel file with the following columns: BARCODE, NAME, DES, TYPE. If you want to work with different columns, you will need to modify the code when prompted to enter the data (name, description, type).

- Enter the IP address and port from the "IP Webcam" application video stream.

- Click the "Scan" (Escanear) button to start scanning barcodes.

5. Hold your mobile device in a way that the camera can clearly see the barcodes. The program will detect and highlight valid barcodes in real-time.

6. When a valid barcode is detected, a sound will play, and options will be provided to register the barcode in the Excel file. If the code is already registered, a message will be displayed indicating that it is already in the list.

7. To stop the program, press the 'q' key in the GUI window.

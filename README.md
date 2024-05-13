# Background Remover with Gradio Client
This Python script utilizes the Gradio client to interact with a hosted machine learning model for background removal. It then composites the result onto a specified background image.

## Prerequisites
- Python 3.6+
- Pillow (PIL Fork) for image processing
- Gradio client for interacting with the hosted model

You can install the required packages using pip:
```bash
pip install pillow gradio_client
```

## How to Run the Script
1. Save your script as `app.py`.
2. Place the image you want to process as `test.jpg` in the same directory as your script.
3. Save your desired background image as `bg.png` in the same directory.
4. Run the script using the following command:
   ```bash
   python app.py
   ```

The script will perform the following actions:
- Connect to the hosted model via Gradio client.
- Send `test.jpg` for background removal.
- Upon receiving the processed image, it will be saved as `image.png` in a temporary directory.
- Load `image.png` and `bg.png`, then crop and resize the background image to match the dimensions of the processed image.
- Composite the processed image onto the background image.
- Save the composited image as `output.png` in the same directory as your script.

## Usage
The script is designed to be run as a standalone application. It does not require any command line arguments, as the file paths are hardcoded for simplicity. For different images, replace `test.jpg` and `bg.png` with your images and ensure they are in the correct directory before running the script.

## Output
The final output, `output.png`, will be the background removed image composited onto the specified background image and saved in the same directory as the script.

## Disclaimer
Please note that the hosted model's availability and performance are subject to the provider's policies and server status. This script is a basic example and may need adjustments for production use.

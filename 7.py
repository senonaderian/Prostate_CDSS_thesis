import os
import cv2
import numpy as np


def preprocess_image(image_path, output_size=(224, 224)):
    # Print the file path to ensure it's correct
    print(f"Attempting to open file: {image_path}")

    # Check if the image file exists
    if not os.path.isfile(image_path):
        raise FileNotFoundError(f"Image file not found: {image_path}")

    # Read image in grayscale
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Check if the image was loaded correctly
    if image is None:
        raise FileNotFoundError(f"Unable to read image file: {image_path}")

    # Resize the image to the specified dimensions
    image_resized = cv2.resize(image, output_size)

    # Convert image to float32 for normalization
    image_float = image_resized.astype(np.float32)

    # Compute the mean and standard deviation
    mean = np.mean(image_float)
    std = np.std(image_float)

    # Print statistics before normalization
    print(f"Mean before normalization: {mean}")
    print(f"Std dev before normalization: {std}")

    # Normalize the image: subtract mean and divide by standard deviation
    if std != 0:  # To avoid division by zero
        image_normalized = (image_float - mean) / std
    else:
        image_normalized = image_float - mean  # If std is zero, just subtract the mean

    # Scale normalized values to the range [0, 255]
    image_normalized = 255 * (image_normalized - np.min(image_normalized)) / (
                np.max(image_normalized) - np.min(image_normalized))

    # Convert back to uint8 for image display
    image_normalized = image_normalized.astype(np.uint8)

    # Print statistics after normalization
    print(f"Min value after normalization: {np.min(image_normalized)}")
    print(f"Max value after normalization: {np.max(image_normalized)}")

    # This normalization is crucial for stabilizing and speeding up model training
    print("Normalization was applied to stabilize and speed up model training.")

    return image_normalized


# Example usage
input_image_path = r'D:\My_Projects\CDSS\t2tra.jpg'  # Corrected file path
try:
    processed_image = preprocess_image(input_image_path)
    # Save the processed image if needed
    cv2.imwrite('processed_image.jpg', processed_image)
except FileNotFoundError as e:
    print(e)

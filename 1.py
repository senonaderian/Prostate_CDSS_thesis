import cv2
import numpy as np
import os


def preprocess_image(image_path):
    # Load the image in grayscale
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Resize the image to 224x224 pixels
    image_resized = cv2.resize(image, (224, 224))

    # Normalize the image to range [0, 1]
    image_normalized = image_resized / 255.0

    return image_normalized


def load_and_preprocess_images(image_folder):
    processed_images = []

    for sequence_type in ['CS13D-SE-PROSTATE', 'ADC', 'T2-weighted']:
        sequence_folder = os.path.join(image_folder, sequence_type)
        sequence_images = []

        for image_name in os.listdir(sequence_folder):
            image_path = os.path.join(sequence_folder, image_name)
            processed_image = preprocess_image(image_path)
            sequence_images.append(processed_image)

        # Assume that the images are ordered consistently across sequences
        processed_images.append(np.array(sequence_images))

    # Stack the sequences along the last axis to create a 3-channel image
    combined_image = np.stack(processed_images, axis=-1)

    return combined_image


# Example usage
image_folder = 'path_to_images'
all_processed_images = {}

for patient_folder in os.listdir(image_folder):
    patient_path = os.path.join(image_folder, patient_folder)
    combined_image = load_and_preprocess_images(patient_path)
    all_processed_images[patient_folder] = combined_image

# Processed images are now stored in the 'all_processed_images' dictionary

#!/usr/bin/env python3

from PIL import Image
import os

# Set the default image directory and the destination directory
directory = '../Automated Catalog/supplier-data/copy_of_images'
destination_folder = "../Automated Catalog/supplier-data/copy_of_images"

# Check if the destination folder exists and create it if it does not.
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

# Holds the images in the directory folder for further processing.
input_files = []

# Iterate through files in the directory
for files in os.listdir(directory):
    input_files.append(files)

# Process each image file
for img in input_files:
    image_path = os.path.join(directory, img)
    image = Image.open(image_path)
    # Resize and rotate the image
    rotated_resized_image = image.resize((600, 400))
    output_path = os.path.join(destination_folder, os.path.splitext(img)[0] + '.jpeg')
    rotated_resized_image.convert("RGB").save(output_path, "JPEG")


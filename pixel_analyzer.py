import os

import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

def analyze_stats(image_path, plot: bool):
    # Load the image and convert it to grayscale if it's not already
    image = Image.open(image_path).convert('L')

    # Convert image to a NumPy array
    image_array = np.array(image)

    # Calculate the mean and standard deviation of the pixel values
    mean = np.mean(image_array)
    std = np.std(image_array)

    if plot:
        # Plot the distribution of pixel values
        plt.figure(figsize=(8, 6))
        plt.hist(image_array.flatten(), bins=256, range=(0, 256), color='gray', alpha=0.75)
        plt.title('Pixel Value Distribution')
        plt.xlabel('Pixel Value')
        plt.ylabel('Frequency')
        plt.grid(True)
        plt.show()

    return mean, std


def check_stds(directory: str):
    std_devs = {}

    for img in os.listdir(directory):
        image_path = os.path.join(directory, img)
        n_img = int(os.path.splitext(img)[0])
        if os.path.exists(image_path):
            _, std = analyze_stats(image_path, plot=False)
            std_devs[n_img] = std
            print(f"Image {img}: Standard Deviation = {std:.2f}")
        else:
            print(f"Image {img} not found in the directory.")

    return std_devs


def plot_stds(std_devs):
    photo_numbers = list(std_devs.keys())
    std_values = list(std_devs.values())

    plt.figure(figsize=(10, 6))
    plt.scatter(photo_numbers, std_values, color='blue', marker='o')
    plt.title('Standard Deviation vs. Photo Number')
    plt.xlabel('Photo Number')
    plt.ylabel('Standard Deviation')
    plt.grid(True)
    plt.show()




# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import torch
import os
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from pixel_analyzer import *
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #image_path = '1001.jpg'
    #mean, std = analyze(image_path, False)
    path = 'std_threshold_test'
    stds = check_stds(path)
    plot_stds(stds)
    print(stds)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/

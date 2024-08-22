
import os
import shutil
import random

def distribute_files_to_three(source_dir, dest_dir1, dest_dir2, dest_dir3, proportion1=0.7, proportion2=0.15):
    """
    Randomly distributes files from source_dir to three destination directories based on given proportions.

    Args:
    - source_dir (str): The directory containing the original files.
    - dest_dir1 (str): The first destination directory.
    - dest_dir2 (str): The second destination directory.
    - dest_dir3 (str): The third destination directory.
    - proportion1 (float): The proportion of files to copy to dest_dir1 (between 0 and 1).
    - proportion2 (float): The proportion of files to copy to dest_dir2 (between 0 and 1).

    The remaining files will be copied to dest_dir3.
    """
    # Validate proportions
    if not (0 <= proportion1 <= 1 and 0 <= proportion2 <= 1):
        raise ValueError("Proportions should be between 0 and 1.")
    if proportion1 + proportion2 > 1:
        raise ValueError("The sum of the first two proportions should not exceed 1.")

    # Get list of all files in the source directory
    all_files = os.listdir(source_dir)
    total_files = len(all_files)

    # Calculate the number of files to copy
    num_files_to_copy1 = int(total_files * proportion1)
    num_files_to_copy2 = int(total_files * proportion2)
    num_files_to_copy3 = total_files - num_files_to_copy1 - num_files_to_copy2

    # Randomly shuffle and split the files
    random.shuffle(all_files)
    files_for_dest1 = all_files[:num_files_to_copy1]
    files_for_dest2 = all_files[num_files_to_copy1:num_files_to_copy1 + num_files_to_copy2]
    files_for_dest3 = all_files[num_files_to_copy1 + num_files_to_copy2:]

    # Ensure destination directories exist
    os.makedirs(dest_dir1, exist_ok=True)
    os.makedirs(dest_dir2, exist_ok=True)
    os.makedirs(dest_dir3, exist_ok=True)

    # Copy the files
    for file_name in files_for_dest1:
        shutil.copy(os.path.join(source_dir, file_name), os.path.join(dest_dir1, file_name))
    for file_name in files_for_dest2:
        shutil.copy(os.path.join(source_dir, file_name), os.path.join(dest_dir2, file_name))
    for file_name in files_for_dest3:
        shutil.copy(os.path.join(source_dir, file_name), os.path.join(dest_dir3, file_name))

    print(
        f"Copied {num_files_to_copy1} files to {dest_dir1}, {num_files_to_copy2} files to {dest_dir2}, and {num_files_to_copy3} files to {dest_dir3}.")

# distribute healthy data
distribute_files_to_three('/Users/tommyzhao/Desktop/data/healthy',
                          'dataset/train/healthy', 'dataset/val/healthy', 'dataset/test/healthy',
                          proportion1=0.7, proportion2=0.15)

# distribute diabetes data
distribute_files_to_three('/Users/tommyzhao/Desktop/data/diabetic',
                          'dataset/train/diabetic', 'dataset/val/diabetic', 'dataset/test/diabetic',
                          proportion1=0.7, proportion2=0.15)

import os
import shutil
from striprtf.striprtf import rtf_to_text


def load_rtf_to_array(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    # Convert RTF content to plain text
    # Split the text into lines or paragraphs (based on your need)
    text_array = content.splitlines()  # Splits into lines
    # text_array = plain_text.split('\n\n')  # Splits into paragraphs
    return text_array

diabetes_list_path = '/Users/tommyzhao/Desktop/data/diabetes_list.txt'
healthy_list_path = '/Users/tommyzhao/Desktop/data/healthy_list.txt'
diabetes_list = load_rtf_to_array(diabetes_list_path)
healthy_list = load_rtf_to_array(healthy_list_path)


def entries_in_string(entries, target_string):
    """
    Detect if any entries in the array appear in the target string.

    :param entries: List of entries to search for.
    :param target_string: The string in which to search for entries.
    :return: True if any entry is found in the target string, False otherwise.
    """
    for entry in entries:
        if entry in target_string:
            return True
    return False


def copy_files(source_dir, destination_dir):
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)

    i = 0
    for patient_dir in os.listdir(source_dir):
        if entries_in_string(diabetes_list, patient_dir):
            patient_dir = os.path.join(source_dir, patient_dir);
            n = 0
            for toe in os.listdir(patient_dir):
                if entries_in_string(['L2', 'R2'], toe):
                    date = toe[:-3]
                    toe = os.path.join(patient_dir, toe, date + '_figure_mask');
                    for file_name in os.listdir(toe):
                        try:
                            if int(file_name[:-4]) >= 1300:
                                full_file_name = os.path.join(toe, file_name)
                                if os.path.isfile(full_file_name):
                                    new_file_name = str(i) + '.' + str(n) + '.jpg'
                                    new = os.path.join(destination_dir, new_file_name)
                                    shutil.copy2(full_file_name, new)
                                    print(f"Copied: {full_file_name} to {destination_dir}")
                                    n += 1
                                else:
                                    print(f"invalid file: {full_file_name}")
                        except ValueError:
                            pass
                        else:
                            continue
                else:
                    continue
            i += 1
        else:
            continue


# Example usage
# source_directory = '/Volumes/清湃共享文件夹3/实验数据/3Dfoot（友谊医院）/20240409-趙有芹（术前）（右脚）/240409003_R2/figure_sameframe'
source_directory = '/Volumes/清湃共享文件夹3/实验数据/3Dfoot（友谊医院）'
destination_directory = '/Users/tommyzhao/Desktop/data/diabetic'

copy_files(source_directory, destination_directory)

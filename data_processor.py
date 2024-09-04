import os
import shutil
import names


# returns the first thing from a collection that is present in string
# and none if not present
def present(string, collection):
    for x in collection:
        if x in string:
            return x
    return None


# initiaizes a directory with diabetic and healthy patient initials
def initialize(base_dir, class1_names, class2_names):
    """
    Initializes the directory structure.

    :param base_dir: The base directory where class subdirectories will be created.
    :param class1_names: A dictionary with names for the first class.
    :param class2_names: A dictionary with names for the second class.
    """
    # Define subdirectories for classes
    class1_dir = os.path.join(base_dir, 'diabetic')
    class2_dir = os.path.join(base_dir, 'healthy')

    # Create class directories
    os.makedirs(class1_dir, exist_ok=True)
    os.makedirs(class2_dir, exist_ok=True)

    # Create subdirectories for names in Class1
    for name in class1_names:
        name_dir = os.path.join(class1_dir, name)
        os.makedirs(name_dir, exist_ok=True)

    # Create subdirectories for names in Class2
    for name in class2_names:
        name_dir = os.path.join(class2_dir, name)
        os.makedirs(name_dir, exist_ok=True)


def ignore_files(dir, files):
    return [f for f in files if f == 'Thumbs.db']


def copy_data(source_dir, destination_dir):
    moved_patients = set()
    toes = [f"L{i}" for i in range(1, 6)] + [f"R{i}" for i in range(1, 6)]

    # first handle diabetic patients
    for patient_dir in os.listdir(source_dir):
        name = present(patient_dir, names.diabetic_list)
        init = ""
        if True: #"术后" not in patient_dir:
            if name is not None and name not in moved_patients:  # valid patient to move
                init = names.diabetic_dict[name]
                target_base = os.path.join(destination_dir, "diabetic", init)
                patient_dir_full = os.path.join(source_dir, patient_dir);
                moved_toes = set()
                print(f"looking at patient {name} ({init}) at directory {patient_dir_full}")
                for possible_toe in os.listdir(patient_dir_full):
                    print(f"looking at {possible_toe}")
                    toe = present(possible_toe, toes)
                    if toe is not None and toe not in moved_toes:  # valid toe to move
                        skip = True
                        figure_mask = ""
                        for file_name in os.listdir(os.path.join(patient_dir_full, possible_toe)):
                            # already in toe, find the correct figure_mask
                            if "_figure_vb" in file_name:
                                figure_mask = file_name
                                skip = False
                                print("no figure vb; not a toe")
                        if not skip:
                            copy_source = os.path.join(patient_dir_full, possible_toe, figure_mask)
                            target = os.path.join(target_base, toe)
                            os.makedirs(target, exist_ok=True)
                            shutil.copytree(copy_source, os.path.join(target, "figure_vb"), ignore=ignore_files)
                            print(f"successfully copied from {copy_source} to {target}")
                            moved_toes.add(toe)
                    else:
                        print(f"{possible_toe} is not a toe or has already been moved; skip")
                        continue
                moved_patients.add(name)
            else:
                continue
    print(f"Successfully moved :{moved_patients}")
    print(f"Patients left: {set(names.diabetic_list) - moved_patients}")


def copy_data2(source_dir, destination_dir):
    moved_patients = set()
    toes = [f"L{i}" for i in range(1, 6)] + [f"R{i}" for i in range(1, 6)]

    # handle healthy patients
    for patient_dir in os.listdir(source_dir):
        name = present(patient_dir, names.healthy_list)
        init = ""
        if True: #"术后" not in patient_dir:
            if name is not None: #and name not in moved_patients:  # valid patient to move
                init = names.healthy_dict[name]
                target_base = os.path.join(destination_dir, "healthy", init)
                patient_dir_full = os.path.join(source_dir, patient_dir);
                moved_toes = set()
                print(f"looking at patient {name} ({init}) at directory {patient_dir_full}")
                for possible_toe in os.listdir(patient_dir_full):
                    print(f"looking at {possible_toe}")
                    toe = present(possible_toe, toes)
                    if toe is not None and toe not in moved_toes:  # valid toe to move
                        skip = True
                        figure_mask = ""
                        for file_name in os.listdir(os.path.join(patient_dir_full, possible_toe)):
                            # already in toe, find the correct figure_mask
                            if "_figure_mask" in file_name:
                                figure_mask = file_name
                                skip = False
                        if not skip:
                            copy_source = os.path.join(patient_dir_full, possible_toe, figure_mask)
                            target = os.path.join(target_base, toe)
                            os.makedirs(target, exist_ok=True)
                            shutil.copytree(copy_source, os.path.join(target, "figure_mask"), ignore=ignore_files)
                            print(f"successfully copied from {copy_source} to {target}")
                            moved_toes.add(toe)
                    else:
                        print(f"{possible_toe} is not a toe or has already been moved; skip")
                        continue
                moved_patients.add(name)
            else:
                continue
    print(f"Successfully moved :{moved_patients}")
    print(f"Patients left: {set(names.healthy_list) - moved_patients}")


# Example usage
# source_directory = '/Volumes/清湃共享文件夹3/实验数据/3Dfoot（友谊医院）/20240409-趙有芹（术前）（右脚）/240409003_R2/figure_sameframe'
source_directory = '/Volumes/清湃共享文件夹3/实验数据/3Dfoot（友谊医院）'
source_directory2 = '/Volumes/清湃共享文件夹3/实验数据/3Dfoot'
destination_directory = '/Users/tommyzhao/Desktop/data2'

# initialize(destination_directory, names.diabetic_init, names.healthy_init)
copy_data(source_directory, destination_directory)
# toes = [f"L{i}" for i in range(1, 6)] + [f"R{i}" for i in range(1, 6)]

# print(present("dsfkjshfdkjR1", toes))

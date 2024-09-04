import os
import shutil


def construct(model_name):
    dataset_path = model_name + "_dataset"
    os.makedirs(dataset_path, exist_ok=True)
    test = os.path.join(dataset_path, "test")
    train = os.path.join(dataset_path, "train")
    val = os.path.join(dataset_path, "val")
    os.makedirs(test, exist_ok=True)
    os.makedirs(train, exist_ok=True)
    os.makedirs(val, exist_ok=True)

    main_dirs = [test, train, val]

    # Subdirectories to be created under each main directory
    subdirs = ["healthy", "diabetic"]

    # Create the subdirectories
    for main_dir in main_dirs:
        for subdir in subdirs:
            # Construct the full path to the subdirectory
            subdir_path = os.path.join(main_dir, subdir)

            # Create the subdirectory
            os.makedirs(subdir_path, exist_ok=True)

    healthy = ["LQJ", "XLX", "ZYL", "ZPF", "YJX", "ZNY"]
    diabetic = ["WXH", "LJZ", "LXR", "XJK", "ZAL", "ZCH"]

    model_to_patients = {}
    model_names = ["2A", "2B", "2C", "2D", "2E", "2F"]

    for i, model in enumerate(model_names):
        healthy_initial = healthy[i]
        diabetic_initial = diabetic[i]
        model_to_patients[model] = (diabetic_initial, healthy_initial)

    data_path = '/Users/tommyzhao/Desktop/data2'

    for img_class in os.listdir(data_path):
        val_done = False
        class_dir = os.path.join(data_path, img_class)
        if not os.path.isdir(class_dir):
            continue

        for patient in os.listdir(class_dir):
            patient_dir = os.path.join(class_dir, patient)

            if not os.path.isdir(patient_dir):
                continue

            if img_class == "healthy":
                n = 1
            else:
                n = 0

            if patient == model_to_patients[model_name][n]:
                for toe in os.listdir(patient_dir):
                    d = os.path.join(patient_dir, toe, "figure_mask")
                    if not os.path.isdir(d):
                        continue
                    for file in os.listdir(d):
                        if file.lower().endswith(('.jpg', '.jpeg')):
                            dest = os.path.join(dataset_path, "test", img_class)
                            new_name = patient + "_" + toe + "_" + file
                            file_dir = os.path.join(d, file)
                            shutil.copy2(file_dir, os.path.join(dest,new_name))
                            print(f"Copied from {file_dir} to {dest} as {new_name}")
            elif not val_done:
                for toe in os.listdir(patient_dir):
                    d = os.path.join(patient_dir, toe, "figure_mask")
                    if not os.path.isdir(d):
                        continue
                    for file in os.listdir(d):
                        if file.lower().endswith(('.jpg', '.jpeg')):
                            dest = os.path.join(dataset_path, "val", img_class)
                            new_name = patient + "_" + toe + "_" + file
                            file_dir = os.path.join(d, file)
                            shutil.copy2(file_dir, os.path.join(dest,new_name))
                            print(f"Copied from {file_dir} to {dest} as {new_name}")
                val_done = True
            else:
                for toe in os.listdir(patient_dir):
                    d = os.path.join(patient_dir, toe, "figure_mask")
                    if not os.path.isdir(d):
                        continue
                    for file in os.listdir(d):
                        if file.lower().endswith(('.jpg', '.jpeg')):
                            dest = os.path.join(dataset_path, "train", img_class)
                            new_name = patient + "_" + toe + "_" + file
                            file_dir = os.path.join(d, file)
                            shutil.copy2(file_dir, os.path.join(dest,new_name))
                            print(f"Copied from {file_dir} to {dest} as {new_name}")


construct("2B")
print("done")
import os
import torch
import torch.nn as nn
from torchvision import models, transforms
from PIL import Image
import torch.nn.functional as F
import matplotlib.pyplot as plt

print(os.listdir('models'))
model_name = input("Enter model to test: ")
test_class = int(input("Test model on healthy (1) or diabetic (0) patient"))
d = 'std_threshold_test' if test_class == 1 else 'dataset/diabetes_patient_test2'
#image_path = os.path.join(d, os.listdir(d)[0])


# Load model
model = models.resnet50()
num_ftrs = model.fc.in_features
model.fc = nn.Linear(num_ftrs, 2)
model.load_state_dict(torch.load('models/' + model_name + '.pth', map_location=torch.device('cpu'), weights_only=True))
model.eval()

# Transformation
transform = transforms.Compose([
    transforms.Grayscale(num_output_channels=3),  # Convert grayscale to 3-channel RGB
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
])

correct = 0
total = 0
incorrect = []
for file in os.listdir(d):
    image_path = os.path.join(d, file)
    # Inference on a new image
    try:
        image = Image.open(image_path)
        image = transform(image).unsqueeze(0)  # Add batch dimension

        print('Image: ' + file)

        with torch.no_grad():

            output = model(image)
            _, predicted = torch.max(output, 1)
            probabilities = F.softmax(output, dim=1)  # Apply softmax to get probabilities
            result = 'Healthy' if predicted.item() == 1 else 'Diabetic'
            if predicted.item() == test_class:
                correct += 1
            else:
                file_name = os.path.splitext(os.path.basename(file))[0]
                incorrect.append(file_name)
            total += 1
            print('Predicted: ' + result)
            print(f"Class probabilities: {probabilities.squeeze().tolist()}")
    except:
        pass

print(f"Accuracy (%):  {(correct/total) * 100}" "%")
incorrect.sort()
print(f"Incorrect identifications: {incorrect}")
plt.hist(incorrect, bins=700, range=(1000, 1700))
plt.show()


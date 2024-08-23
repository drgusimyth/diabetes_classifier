import os
import torch
import torch.nn as nn
from torchvision import models, transforms
from PIL import Image
import torch.nn.functional as F


d = 'dataset/test/diabetic'
#image_path = os.path.join(d, os.listdir(d)[0])


# Load model
model = models.resnet50()
num_ftrs = model.fc.in_features
model.fc = nn.Linear(num_ftrs, 2)
model.load_state_dict(torch.load('vascular_scan_classifier.pth', map_location=torch.device('cpu'), weights_only=True))
model.eval()

# Transformation
transform = transforms.Compose([
    transforms.Grayscale(num_output_channels=3),  # Convert grayscale to 3-channel RGB
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
])

correct = 0
total = len(os.listdir(d))
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
            if predicted.item() == 0:
                correct += 1
            print('Predicted: ' + result)
            print(f"Class probabilities: {probabilities.squeeze().tolist()}")
    except:
        pass
print(f"Accuracy (%):  {(correct/total) * 100}" "%")


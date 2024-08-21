import torch
from torchvision import models, transforms
from PIL import Image

# Load model
model = models.resnet50()
num_ftrs = model.fc.in_features
model.fc = nn.Linear(num_ftrs, 2)
model.load_state_dict(torch.load('vascular_scan_classifier.pth'))
model.eval()

# Transformation
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
])

# Inference on a new image
image = Image.open('path_to_new_image.jpg')
image = transform(image).unsqueeze(0)  # Add batch dimension

with torch.no_grad():
    output = model(image)
    _, predicted = torch.max(output, 1)
    print('Predicted:', 'Healthy' if predicted.item() == 0 else 'Diabetic')

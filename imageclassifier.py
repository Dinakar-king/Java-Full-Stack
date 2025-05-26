import torch 
from torchvision import models, transforms 
from PIL import Image 
import requests 
import json 
 
# Load the pretrained ResNet50 model (original output = 1000 ImageNet 

model = models.resnet18(pretrained=True) 
model.eval()  # Set to evaluation mode 
 
# Image preprocessing (same as ImageNet training) 
preprocess = transforms.Compose([ 
    transforms.Resize(256), 
    transforms.CenterCrop(224), 
    transforms.ToTensor(), 
    transforms.Normalize( 
        mean=[0.485, 0.456, 0.406],  # Imagenet mean 
        std=[0.229, 0.224, 0.225]    # Imagenet std 
    ) 
]) 
 
# Load an example image (replace with your image path or URL) 
img_url ="https://upload.wikimedia.org/wikipedia/commons/2/26/YellowLabradorLooking_new.jpg" 
image = Image.open(requests.get(img_url, stream=True).raw) 
#image = Image.open("C:/Users/thupa/OneDrive/Desktop/frontend/Ai Model/cat.jpg") 
 
# Preprocess the image 
input_tensor = preprocess(image) 
input_batch = input_tensor.unsqueeze(0) 
 
# Run inference 
with torch.no_grad(): 
    output = model(input_batch) 
 
# Load ImageNet labels 
LABELS_URL = "https://raw.githubusercontent.com/pytorch/hub/master/imagenet_classes.txt" 
labels = requests.get(LABELS_URL).text.splitlines() 

probabilities = torch.nn.functional.softmax(output[0], dim=0) 
top5_prob, top5_catid = torch.topk(probabilities, 5) 
print("Top 5 Predictions:") 
for i in range(top5_prob.size(0)): 
    print(f"{labels[top5_catid[i]]}: {top5_prob[i].item()*100:.2f}%")
    
def predict_image(image):
    input_tensor = preprocess(image).unsqueeze(0)
    with torch.no_grad():
        output = model(input_tensor)
        probs = torch.nn.functional.softmax(output[0],dim=0)
    top_prob, top_class = torch.max(probs,dim=0)
    return labels[top_class], top_prob.item()*100
import torch
import cv2
import numpy as np
from PIL import Image
import torchvision.transforms as transforms

def load_segmentation_model(model_path):
    # Loads a pre-trained segmentation model
    try:
        model = torch.hub.load('pytorch/vision:v0.10.0', 'deeplabv3_resnet101', pretrained=True)
        model.eval()
        return model
    except Exception as e:
       print(f"Error loading segmentation model:{e}")
       return None
def preprocess_image(image):
    # Preprocesses the image to be used in the model.
    transform = transforms.Compose([
      transforms.ToTensor(),
      transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
   ])
    image = Image.fromarray(image)
    return transform(image).unsqueeze(0)
def segment_hair(image, model):
     # Performs hair segmentation using PyTorch.
    try:
       input_tensor = preprocess_image(image)
       with torch.no_grad():
          output = model(input_tensor)['out']
       output_predictions = output.argmax(1).squeeze().cpu().numpy()
       mask = (output_predictions == 15).astype(np.uint8) * 255 # 15 is for the hair class
       return mask
    except Exception as e:
       print(f"Error during hair segmentation:{e}")
       return None
def overlay_hairstyle(user_image, hair_mask, hairstyle_image):
    # Overlays a hairstyle image on the user's image, using the hair mask.
    try:
        user_image = cv2.cvtColor(user_image, cv2.COLOR_RGB2BGR) # Convert user image to BGR
        hairstyle_image = cv2.imread(hairstyle_image) # Read the image path of the given hairstyle
        hairstyle_image = cv2.cvtColor(hairstyle_image, cv2.COLOR_BGR2RGB) # Convert hairstyle image to RGB
        hairstyle_image = cv2.resize(hairstyle_image, (user_image.shape[1], user_image.shape[0])) # Resize the hairstyle image with user image.
        masked_user_image = cv2.bitwise_and(user_image, user_image, mask = cv2.cvtColor(hair_mask, cv2.COLOR_GRAY2BGR))
        masked_hairstyle = cv2.bitwise_and(hairstyle_image, hairstyle_image, mask = cv2.cvtColor(hair_mask, cv2.COLOR_GRAY2BGR))
        combined_image = cv2.addWeighted(masked_user_image, 1, masked_hairstyle, 0.7, 0)
        return combined_image
    except Exception as e:
       print(f"Error overlaying hairstyle image:{e}")
       return None
import os
import re
import time
import traceback
from tqdm import tqdm
from PIL import Image
import torch
from transformers import pipeline, AutoModelForImageClassification, ViTImageProcessor




# classifier = pipeline("image-classification", model="Falconsai/nsfw_image_detection")
# Load Model
model = AutoModelForImageClassification.from_pretrained("Falconsai/nsfw_image_detection", device_map="auto")
processor = ViTImageProcessor.from_pretrained('Falconsai/nsfw_image_detection',device_map="auto")

# Load porn website lists
with open(f'{os.path.dirname(__file__)}/../../block.txt', 'r') as f:
    block_list = f.read().splitlines()
    

def experiment():

    data_dir = f'{os.path.dirname(__file__)}/../../nsfw_model/images/P2datasetFull/train/2/'
    entries = os.listdir(data_dir)
    num_samples = len(entries)
    correct_predictions = 0
    pbar = tqdm(entries[:num_samples])
    for i,entry in enumerate(pbar):
            
        try:
            image = Image.open(data_dir+entry)
            #prediction
            with torch.no_grad():
                inputs = processor(images=image, return_tensors="pt")
                outputs = model(**inputs)
                logits = outputs.logits

            predicted_label = logits.argmax(-1).item()
            res = model.config.id2label[predicted_label]
            # classifier(image)
            if res == "nsfw":
                correct_predictions += 1
            # print(outputs)
            
            pbar.set_postfix({'res': res, 'accuracy': (correct_predictions)/(i+1)})
        except:
            traceback.print_exc()
            time.sleep(1)
            print("Error processing image: ", entry)
            continue

def porn_img_detect(image_path):
    try:
        image = Image.open(image_path)
        with torch.no_grad():
            inputs = processor(images=image, return_tensors="pt")
            outputs = model(**inputs)
            logits = outputs.logits

        predicted_label = logits.argmax(-1).item()
        res = model.config.id2label[predicted_label]
        return res
    except Exception as e:
        traceback.print_exc()
        time.sleep(1)
        print("Error processing image: ", image_path)
        return e
    
def porn_link_detection(link):
    link = re.sub(r'^https?:\/\/', '', link)
    
    for block_link in block_list:
        if block_link in link:
            print(f"Link: {link} is blocked")
            return True
    print(f"Link: {link} is not blocked")
    return False
    
if __name__ == '__main__':
    porn_link_detection("https://www.xvideos.com/")
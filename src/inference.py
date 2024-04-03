import os
import json
import io
import re
import time
import traceback
from tqdm import tqdm
from PIL import Image
import torch
from py_ipfs_cid import compute_cid
from transformers import pipeline, AutoModelForImageClassification, ViTImageProcessor




# classifier = pipeline("image-classification", model="Falconsai/nsfw_image_detection")
# Load Model
model = AutoModelForImageClassification.from_pretrained("Falconsai/nsfw_image_detection", device_map="auto")
processor = ViTImageProcessor.from_pretrained('Falconsai/nsfw_image_detection',device_map="auto")

# # Load porn website lists
# with open(f'{os.path.dirname(__file__)}/../../block.txt', 'r') as f:
#     block_list = f.read().splitlines()
    

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
            prob = logits.softmax(-1).max().item()
            v0cid = compute_cid(image)
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
def process_img():
    data_dir = f'{os.path.dirname(__file__)}/../../nsfw_model/images/P2datasetFull/test1/2/'
    entries = os.listdir(data_dir)
    num_samples = len(entries)
    pbar = tqdm(entries[:num_samples])
    if os.path.isfile(f"{os.path.dirname(__file__)}/../nsfwcids.json"):
        res_json = json.load(open(f"{os.path.dirname(__file__)}/../nsfwcids.json"))
    else:
        res_json = dict()
    for i,entry in enumerate(pbar):
            
        try:
            image = Image.open(data_dir+entry).convert("RGB")
            #prediction
            with torch.no_grad():
                inputs = processor(images=image, return_tensors="pt")
                outputs = model(**inputs)
                logits = outputs.logits

            predicted_label = logits.argmax(-1).item()
            res = model.config.id2label[predicted_label]
            prob = logits.softmax(-1).max().item()
            v0cid = compute_cid(image.tobytes())
            if res == "nsfw":
                res_json[v0cid] = {"is_nsfw_image": res, "probability": prob}
            # classifier(image)
            
            pbar.set_postfix({'res': res, 'cid': v0cid})
        except:
            traceback.print_exc()
            time.sleep(1)
            print("Error processing image: ", entry)
    print("Length of nsfw cids: ", len(res_json))
    json.dump(res_json, open(f"{os.path.dirname(__file__)}/../nsfwcids.json", "w"))
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
    process_img()
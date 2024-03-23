import os
import requests
import re
import traceback
import requests
from io import BytesIO

import torch
from flask import Flask, request, jsonify
from PIL import Image
from transformers import AutoModelForImageClassification, ViTImageProcessor

app = Flask(__name__)
dir_path = os.path.dirname(os.path.realpath(__file__))

# Load Model
model = AutoModelForImageClassification.from_pretrained("Falconsai/nsfw_image_detection", device_map="auto")
processor = ViTImageProcessor.from_pretrained('Falconsai/nsfw_image_detection',device_map="auto")

# Load porn website lists
with open(f'{dir_path}/../block.txt', 'r') as f:
    block_list = f.read().splitlines()

from PIL import Image
import torch
import traceback

def porn_img_detect(image: Image.Image):
    """
    Detects if an image contains pornographic content.

    Args:
        image (PIL.Image.Image): The input image to be analyzed.

    Returns:
        str: The predicted label for the image. It can be either 'porn' or 'not_porn'.

    Raises:
        Exception: If an error occurs during the detection process.
    """
    try:
        with torch.no_grad():
            # Preprocess the image
            inputs = processor(images=image, return_tensors="pt")

            # Perform inference
            outputs = model(**inputs)
            logits = outputs.logits

        # Get the predicted label
        predicted_label = logits.argmax(-1).item()

        # Return the corresponding label
        return model.config.id2label[predicted_label]
    except Exception as e:
        traceback.print_exc()
        return str(e)

import re

def porn_link_detection(link):
    """
    Detects if a given link is blacklisted.

    Args:
        link (str): The link to be checked.

    Returns:
        bool: True if the link is blacklisted, False otherwise.
    """
    link = re.sub(r'^https?:\/\/', '', link)
    link = re.sub(r'^www\.', '', link)
    
    for block_link in block_list:
        if block_link in link:
            print("Input link: ", link, "\nBlack-listed link: ",block_link, "\n+=+=+=+=+=+=")
            return True
    return False


def is_porn_image_url(url):
    """
    Checks if the given image URL contains pornographic content.

    Args:
        url (str): The URL of the image to be analyzed.

    Returns:
        bool: True if the image is classified as pornographic, False otherwise.
    """
    try:
        response = requests.get(url)
        image = Image.open(BytesIO(response.content))
        print("Analyzing image using ViT model")
        res = porn_img_detect(image)
        return res == "nsfw"
    except Exception:
        return False

@app.route('/link', methods=['POST'])
def link_endpoint():
    """
    This endpoint accepts a POST request with a JSON body containing a list of links.
    Each link is checked to determine if it is a pornographic image or a link to a pornographic website.
    The endpoint returns a JSON response with a 'result' key indicating whether the link is pornographic.
    """
    
    data = request.get_json()
    links = data.get('link')
    
    if not links:
        return jsonify({'error': 'No link provided'}), 400
    if type(links) != list:
        return jsonify({'error': 'Link must be a list'}), 400
    
    # First check if the link contains an image file
    res = []
    for link in links:
        is_porn = is_porn_image_url(link)
        if not is_porn:
            is_porn = porn_link_detection(link)
        res.append(is_porn)
        
    return jsonify({'result': res})

if __name__ == '__main__':
    # TODO: Specify host and port for the Flask app
    app.run(debug=True,host="0.0.0.0")
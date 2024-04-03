# <img src="https://www.gitbook.com/cdn-cgi/image/width=36,dpr=2,height=36,fit=contain,format=auto/https%3A%2F%2F576435799-files.gitbook.io%2F~%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-MauK7Ig3eWeXC35bZV7%252Ficon%252FUuoj67jxo8XNDYmZKupy%252Flogo_transparent.png%3Falt%3Dmedia%26token%3D8e053c6b-b5b3-4055-86dc-380c9f0a609d" width="30" height="30"/> Web3 NSFW Detection Project

### This project aims to develop a web-based application for detecting and filtering NSFW content using the Vision Transformer (ViT) model.  

## NSFW CIDs  

The file [nsfwcids.json](./nsfwcids.json) includes a list of 7K content identifiers (CIDs) that have been classified as Not Safe For Work (NSFW). You are welcome to download and contribute updates to this list.

## Remote API Service

### We have established an API that processes any provided image URL. You can utilize it with the following code snippet:

```py
import requests
import json

headers = {
    'Content-Type': 'application/json',
}
# Sample Input Data
json_data = {
    'link': [
        'https://plutotest.acl.swanipfs.com/ipfs/QmbxYuLWdyQQpdK9wKqK4A8TiFtMf885d6mHrfvaf6CZyX?filename=istockphoto-157030584-612x612.jpg',
        'https://plutotest.acl.swanipfs.com/ipfs/QmRACojSdFuqnyyfQZ9Zgiz6zrVCUX1JRkYZyvRGu1MCzG?filename=Ipfs-logo-1024-ice-text.png',
        'https://plutotest.acl.swanipfs.com/ipfs/QmSeUJZYyC2UVJK2oH7HzVvd3XgEFPtkoiZWSQ6YzSKP36?filename=Happy-Guy.jpg',
        'https://plutotest.acl.swanipfs.com/ipfs/QmUhnnxBNP2tmYAFaBKYqem5weS9H4jXQcjwT7kvSWgXYV?filename=nm-how-happiness-affects-health-tnail.jpg',
    ],
}

response = requests.post(f"https://u3xc9xrzmv.dev2.crosschain.computer/link", headers=headers, json=json_data)

try:
    print(json.dumps(response.json(), indent=4))
except Exception as e:
    print(e)
    print(response)
```

### Sample output  
```
{
    "result": [
        {
            "cid": "bafkreifimggaqwgu2pkjwx6hjwtpw7icswyiifgm2riiuy3kazsw7n67xy",
            "is_nsfw_image": true,
            "link": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSYf_0-TvQ0WIDT0wFTAzdqD-c0y1mSfQjfOO0ydStXxA&s",
            "probability": 0.999750554561615
        },
        {
            "cid": "bafkreidcpmeykuc6atin6zxiednu6vsejitdwsuj6e6hiepqscvihvnvgu",
            "is_nsfw_image": true,
            "link": "https://cdni.pornpics.de/460/7/622/16870332/16870332_155_7baa.jpg",
            "probability": 0.999907374382019
        },
        {
            "cid": "bafkreiaohmu6r7htsd57l6deqijexobisuhzqsjb2nkt2wc3fwpghiwmfa",
            "is_nsfw_image": true,
            "link": "https://cdn77-pic.xvideos-cdn.com/videos/thumbs169poster/28/56/d5/2856d555486fba22716a930e8a928c7f-2/2856d555486fba22716a930e8a928c7f.30.jpg",
            "probability": 0.9998795986175537
        },
        {
            "cid": "bafkreib6pmuc666jed4rasgc7xrhbyrdujligzgfxoemo4ncsbrzzviqoq",
            "is_nsfw_image": true,
            "link": "https://cdn.pornapi.online/content/2023-06-15/eGOkYIoH.jpg",
            "probability": 0.9998980760574341
        },
        {
            "cid": "bafkreibndlhmo442b2xpvr4fsd6rckn2nc7w472l6ti7jzapkvddmh5fcq",
            "is_nsfw_image": true,
            "link": "https://porn62.com/wp-content/uploads/2020/10/xxx-porn.jpg",
            "probability": 0.9998544454574585
        },
        {
            "cid": "bafkreibiv3ntv7fbw2xiedq4pzkjrr4xdrhw5v2aevhnefn366p2kedixm",
            "is_nsfw_image": true,
            "link": "https://static-ca-cdn.eporner.com/gallery/58/U0/pvyTrBuU058/11679702-ai-porn-bbw-image-5.jpg",
            "probability": 0.999873161315918
        },
        {
            "cid": "bafkreibufeswf5gtvgwfu3g52ag5fc3hs3imf3q2dgjjvmqfejkc23vxya",
            "is_nsfw_image": false,
            "link": "https://plutotest.acl.swanipfs.com/ipfs/QmbxYuLWdyQQpdK9wKqK4A8TiFtMf885d6mHrfvaf6CZyX?filename=istockphoto-157030584-612x612.jpg",
            "probability": 0.9925754070281982
        },
        {
            "cid": "bafkreibmfbifzisgpntdaeljw7nbchdnlbijccitaymcozakaiznzaiw64",
            "is_nsfw_image": false,
            "link": "https://plutotest.acl.swanipfs.com/ipfs/QmRACojSdFuqnyyfQZ9Zgiz6zrVCUX1JRkYZyvRGu1MCzG?filename=Ipfs-logo-1024-ice-text.png",
            "probability": 0.999238133430481
        },
        {
            "cid": "bafkreidermoo52zy2nhj6cdmafqfnenfwfwtgrnaio3aijbslk6nyw56te",
            "is_nsfw_image": false,
            "link": "https://plutotest.acl.swanipfs.com/ipfs/QmSeUJZYyC2UVJK2oH7HzVvd3XgEFPtkoiZWSQ6YzSKP36?filename=Happy-Guy.jpg",
            "probability": 0.9997988343238831
        },
        {
            "cid": "bafkreifymod6f45nik5vrctrqzbgvhkh6oe7nr33mq45hbzu6mnxftyrcu",
            "is_nsfw_image": false,
            "link": "https://plutotest.acl.swanipfs.com/ipfs/QmUhnnxBNP2tmYAFaBKYqem5weS9H4jXQcjwT7kvSWgXYV?filename=nm-how-happiness-affects-health-tnail.jpg",
            "probability": 0.9997853636741638
        }
    ]
}

```




## Docker Application

To run the project as a Docker application, follow these steps:

1. Clone the repository:

    ```bash
    git clone https://github.com/swanchain/nsfw-detection.git
    ```

2. Navigate to the project directory:

    ```bash
    cd detection/
    ```

3. Build the Docker image:

    ```bash
    docker build -t nsfw_detection .
    ```

4. Run the Docker container:

    ```bash
    docker run -p 5000:5000 nsfw_detection
    ```

5. Send your curl request to `http://localhost:5000/link` to access the application.

    ```bash
    curl -X POST -H "Content-Type: application/json" -d '{"link":["www.example.com"]}' http://localhost:5000/link
    ```


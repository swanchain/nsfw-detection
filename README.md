# Web3 Porn Detection Project

This project aims to develop a web-based application for detecting and filtering pornographic content using the Vision Transformer (ViT) model.
The websites on the blacklist (block.txt) were acquired by [Bon-Appetit](https://github.com/Bon-Appetit/porn-domains)
The ViT model was built by [Falconsai](https://huggingface.co/Falconsai/nsfw_image_detection)

## Docker Application

To run the project as a Docker application, follow these steps:

1. Clone the repository:

    ```bash
    git clone https://github.com/tomyang/porn_detection.git
    ```

2. Navigate to the project directory:

    ```bash
    cd porn_detection/vit_based
    ```

3. Build the Docker image:

    ```bash
    docker build -t porn_detection .
    ```

4. Run the Docker container:

    ```bash
    docker run -p 5000:5000 porn_detection
    ```

5. Send your curl request to `http://localhost:5000/link` to access the application.

    ```bash
    curl -X POST -H "Content-Type: application/json" -d '{"link":["www.example.com"]}' http://localhost:5000/link
    ```



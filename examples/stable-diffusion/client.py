import base64, io, requests, PIL.Image as Image

if __name__ == "__main__":
    response = requests.post(
        "http://127.0.0.1:50855/predict",
        json={"text": "lightning-inspired bedroom"},
    )

    image = Image.open(io.BytesIO(base64.b64decode(response.json()["image"][22:])))
    image.save("response.png")

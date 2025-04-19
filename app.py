from flask import Flask, render_template
from google.cloud import storage
import os

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/manchester")
def manchester():
    # Init GCS client
    client = storage.Client()
    bucket = client.bucket("spaces-and-faces")
    
    # List image files in the manchester folder
    blobs = bucket.list_blobs(prefix="images/manchester/")
    base_url = "https://storage.googleapis.com/spaces-and-faces/"

    # Filter image files (png/jpg only)
    image_urls = [
        f"{base_url}{blob.name}" for blob in blobs
        if blob.name.lower().endswith((".jpg", ".png"))
    ]

    # Optional: Sort by numeric filename
    def numeric_sort_key(url):
        filename = url.split("/")[-1].split(".")[0]
        try:
            return int(filename)
        except ValueError:
            return 9999

    image_urls.sort(key=numeric_sort_key)

    return render_template("manchester.html", images=image_urls)

@app.route("/brussels")
def brussels():
    base_url = "https://storage.googleapis.com/spaces-and-faces/images/brussels/"
    image_names = [
        f"{i}.png" if i in [1, 2, 3, 8, 9, 10, 11, 12, 17, 19, 20, 22, 24, 25, 26, 27] else f"{i}.jpg"
        for i in range(1, 30)
    ]
    image_urls = [f"{base_url}{name}" for name in image_names]
    return render_template("brussels.html", images=image_urls)

if __name__ == "__main__":
    app.run(debug=True)

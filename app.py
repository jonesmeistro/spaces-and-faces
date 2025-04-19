from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/manchester")
def manchester():
    base_url = "https://storage.googleapis.com/spaces-and-faces/images/manchester/"
    image_names = [
        f"{i}.png" if i in [1, 5, 6, 7, 8, 12, 14, 15, 16, 17, 21] else f"{i}.jpg"
        for i in range(1, 23)
    ]
    image_urls = [f"{base_url}{name}" for name in image_names]
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

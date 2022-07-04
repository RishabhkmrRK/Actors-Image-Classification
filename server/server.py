from flask import Flask, request, jsonify
import util

app = Flask(__name__)


@app.route('/classify_image', methods=['GET', 'POST'])
def classify_image():
    image_data = request.form.get('image_data')
    X = util.classify_image(image_data)
    print(X)
    response = jsonify(X)
    response.headers.add('Access-Control-Allow-Origin', '*')
    print(response)
    return response

if __name__ == "__main__":
    print("Starting Python Flask Server For Sports Celebrity Image Classification")
    util.load_saved_artifacts()
    app.run(port=5000)
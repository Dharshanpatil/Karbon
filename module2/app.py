from flask import Flask, request, render_template, jsonify
import json
from model import analyze_data

app = Flask(__name__)

@app.route('/')
def upload_file():
    return render_template('upload.html')

@app.route('/upload', methods=['POST'])
def upload_file_post():
    file = request.files['data_file']
    data = json.load(file)
    result = analyze_data(data)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)

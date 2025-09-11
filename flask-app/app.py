import os
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Folder to store uploaded files
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/")
def home():
    return render_template("index.html", name="World")

# Route for uploading files
@app.route("/addFile", methods=["GET", "POST"])
def add_file():
    if request.method == "POST":
        if 'file' not in request.files:
            return "No file part in request"
        file = request.files['file']
        if file.filename == "":
            return "No file selected"
        if file:
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filepath)
            return f"File '{file.filename}' uploaded successfully!"
    return render_template("upload.html")

if __name__ == "__main__":
    app.run(debug=True)

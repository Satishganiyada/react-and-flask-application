from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS
import os

# static_folder points to frontend build (production)
app = Flask(__name__, static_folder="../frontend/dist", static_url_path="/")
CORS(app)  # allow cross-origin in dev (you can restrict origins)

@app.route("/api/hello")
def hello():
    return jsonify({"message": "Hello from Flask!"})

# Serve SPA in production (after frontend build)
@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def serve(path):
    if path != "" and os.path.exists(os.path.join(app.static_folder, path)):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, "index.html")

if __name__ == "__main__":
    # only for quick dev test (not production)
    app.run(host="0.0.0.0", port=5000, debug=True)


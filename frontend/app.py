from flask import Flask, render_template_string
import requests

app = Flask(__name__)

BACKEND_API = "http://13.53.52.207:5000/api/hello"
@app.route("/hello")
def hello():
     return """
    <html>
        <head><title>Python Frontend</title></head>
        <body>
            <h1>hello from front end</h1>
        </body>
    </html>
    """
    
@app.route("/")
def home():
    try:
        response = requests.get(BACKEND_API)
        message = response.json().get("message", "No message")
    except Exception as e:
        message = f"Error: {str(e)}"

    return render_template_string("""
    <html>
        <head><title>Python Frontend</title></head>
        <body>
            <h1>{{ message }}</h1>
        </body>
    </html>
    """, message=message)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)




### This is a simple FLASK application, Which wee can upload files to the application and store those in a folder.

# installation setup for flask-app

### sudo apt update
### sudo apt install python3-venv -y
### python3 -m venv myenv
### source myenv/bin/activate
### pip install flask

# Run the application
### python app.py

# Expose port in the app.py file to acess it in your browser
### app.run(debug=True)  => app.run(host="0.0.0.0", port=5000, debug=True)

# --------------------------------------------------------------------------
# Containerise this application with docker
## Create Dockerfile in the flask-app/

## create dockerimage - docker build -t image name

## Run the container - docker run -d -p 5000:5000 image name 

### Now your application will live on ur browser





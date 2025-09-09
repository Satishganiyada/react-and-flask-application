# react-and-flask-application

# pre-requesites
sudo apt update && sudo apt upgrade -y

# essential packages
sudo apt install -y build-essential curl git nginx ufw python3 python3-venv python3-pip

# Front-end:    
    # install node.js:
        curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -
        sudo apt-get install -y nodejs
    # create front-end folder and install react and dependencies
        cd ~/myproject
        mkdir frontend && cd frontend

    # Create a Vite React app (interactive)
        npm create vite@latest myapp -- --template react
        cd myapp
        npm install
      


# Back-end:
    # install flask and set python environment
        python3 -m venv venv
        source venv/bin/activate
        pip install --upgrade pip
        pip install flask flask-cors gunicorn

    # create app.py in backend folder and paste the code

# start front and backend:
   # start fronend 
      npm run dev  
   # start backend
    python app.py   
    Backend: http://localhost:5000/api/hello
    Frontend dev: open http://<your-machine-ip>:5173
# for outside testing open ports
    sudo ufw allow 5000
        
    
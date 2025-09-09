Back-end setup for python application:

sudo apt update
sudo apt install python3-venv -y
python3 -m venv myenv
source myenv/bin/activate
pip install flask flask_cors
python app.py
after running python app.py if it shows address already in use u have to delete the process and again run it 
 ss -tnlp |grep 5000 (command that where the port is running at)
kill -9 pid (to delete the process)
local-testing:
curl http://127.0.0.1:5000/api/hello    (app.py)=> (@app.route("/api/hello"))-path 
response:
{
  "message": "Hello from Flask!"
}
outside-testing:
Gave acess to the 5000 port in aws security groups
public ip :5000/api/hello




---------------------------------------------------------------------------------------
Front-end setup:

sudo apt update
sudo apt install python3-venv -y
python3 -m venv myenv
source myenv/bin/activate 
pip install flask requests
update ip address in app.py
python app.py
 open security groups and acess to port 8080
http://16.170.219.47:8080/ to host it in in the browser









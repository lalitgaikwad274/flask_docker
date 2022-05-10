# flask_docker
it is a docker file. after executing that docker file we can see some web pages running on that server 


# Description

This is simple flask based web app. when we run 
the the docker image with port no it will start the server at that port and we see the web app using by own system ip address like 192.168.xx.xx:8000

## Run

To run docker file go the directory flask_docker
build the docker file

```bash
sudo docker image build -t flask_docker .
```

run the docker image 
```bash
sudo docker run -p 5000:5000 -d flask_docker
```
OR

Directory run the app
```bash
python3 run.py
```

# Dockering a Machine learning model after creating flask and testing it before deploying to Kubernetes.


This is a sample code to deploy your machine learning model in Flask into Docker / Kubernetes.

1) Get the code from the repo.
2) Make sure all the services you want to use are in Docker compose. Check the ports as well.
3) Go to Flask folder.
4) Check if all the requirements to be installed are in the requirement folder 
5) Check if Dockerfile is having the work directory as app or anything you mentioned.
6) All check if its installing the requirements.
7) Now inside folder app/ paste your main.py as init.py
8) Check all the params and cofig files needed for that file are in the main folder Flask and called correctly.

9)Now check the flask app by running it and testing at local host like usual. If working,

10)Build the docker file using

(Make sure you are in parent directory or root directory)
sudo docker build --tag flask-docker-demo-app .  

11) Run and test by 
sudo docker run --name flask-docker-demo-app -p 5001:5001 flask-docker-demo-app

12) You can now move this to the container in Kubernetes and then use the url endpoint as mentioned in kubernetes and test it with the new url.

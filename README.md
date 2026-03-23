\# DevOps Cloud Project



\## Description

Ce projet contient une API Flask conteneurisée avec Docker, des manifests Kubernetes et un pipeline CI/CD.



\## Structure

\- app : application Flask

\- k8s : fichiers Kubernetes

\- .github/workflows : pipeline CI/CD



\## Lancer l'application



cd app

pip install -r requirements.txt

python app.py



\## Docker



docker build -t devops-api .

docker run -p 5000:5000 devops-api



\## Endpoints



/

 /health

 /info
CI/CD pipeline updated 

test docker push


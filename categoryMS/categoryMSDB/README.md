* Create postgres Docker image

docker build -t categoryMS-image .

* Push the iMage to repo

aws ecr get-login-password --region us-east-1 --profile m2mprofile| docker login --username AWS --password-stdin 646336443392.dkr.ecr.us-east-1.amazonaws.com


docker tag categoryMS-image:latest 646336443392.dkr.ecr.us-east-1.amazonaws.com/m2m:categoryMSDB

 
docker push 646336443392.dkr.ecr.us-east-1.amazonaws.com/m2m:categoryMSDB


* To Run the docker image on local container

docker run -d --name postgres-container -p 5432:5432 categoryMS-image

Once Image is available in ECR, create ECS Task definition and launch Fargate service from that.

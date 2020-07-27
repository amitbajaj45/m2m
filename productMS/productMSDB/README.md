* Create postgres Docker image

docker build -t productms-image .

* Push the iMage to repo

aws ecr get-login-password --region us-east-1 --profile m2mprofile| docker login --username AWS --password-stdin 646336443392.dkr.ecr.us-east-1.amazonaws.com


docker tag productms-image:latest 646336443392.dkr.ecr.us-east-1.amazonaws.com/m2m:productMSDB

 
docker push 646336443392.dkr.ecr.us-east-1.amazonaws.com/m2m:productMSDB


* To Run the docker image on local container

docker run -d --name postgres-container -p 5432:5432 productms-image

Once Image is available in ECR, create ECS Task definition and launch Fargate service from that.

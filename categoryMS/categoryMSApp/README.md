* Create Docker Image

docker build -t categoryMSapp-image .

* Push it to ECR

* Replace m2mprofile with correct AWS profile.

aws ecr get-login-password --region us-east-1 --profile m2mprofile| docker login --username AWS --password-stdin 646336443392.dkr.ecr.us-east-1.amazonaws.com


docker tag categoryMSapp-image:latest 646336443392.dkr.ecr.us-east-1.amazonaws.com/m2m:categoryMSApp


docker push 646336443392.dkr.ecr.us-east-1.amazonaws.com/m2m:categoryMSApp


* To run it on local docker container, use below command:


docker run -d --name categoryMS-container -p 8080:8080 -p 9990:9990  categoryMSapp-image

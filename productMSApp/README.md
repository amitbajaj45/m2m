* Create Docker Image

docker build -t productmsapp-image .

* Push it to ECR

* Replace m2mprofile with correct AWS profile.

aws ecr get-login-password --region us-east-1 --profile m2mprofile| docker login --username AWS --password-stdin 646336443392.dkr.ecr.us-east-1.amazonaws.com


docker tag productmsapp-image:latest 646336443392.dkr.ecr.us-east-1.amazonaws.com/m2m:productMSApp


docker push 646336443392.dkr.ecr.us-east-1.amazonaws.com/m2m:productMSApp


* To run it on local docker container, use below command:


docker run -d --name productms-container -p 8080:8080 -p 9990:9990  productmsapp-image

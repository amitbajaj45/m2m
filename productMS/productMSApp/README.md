* Create Docker Image

docker build -t productmsapp-image .

* Push it to ECR

* Replace m2mprofile with correct AWS profile.

region=$(aws configure get region --profile m2mprofile)
accountid=$(aws sts get-caller-identity --query Account --output text --profile m2mprofile)

* Push the iMage to repo

aws ecr get-login-password \
  --region $region --profile m2mprofile | docker login \
  --username AWS \
  --password-stdin $accountid.dkr.ecr.$region.amazonaws.com
  
  
aws ecr create-repository --profile m2mprofile --repository-name m2m/productmsapp-image

  

docker tag productmsapp-image $accountid.dkr.ecr.$region.amazonaws.com/m2m/productmsapp-image:latest

docker push $accountid.dkr.ecr.$region.amazonaws.com/m2m/productmsapp-image:latest

  
  


* To run it on local docker container, use below command:


docker run -d --name productms-container -p 8080:8080 -p 9990:9990  productmsapp-image

docker run -d --name productms-container1 -p 8080:8080 -p 9990:9990 -e "DB_URL=jdbc:postgresql://ECSALB-1d65367beed7ac74.elb.us-east-1.amazonaws.com:5432/productms?ApplicationName=productMicroService" -e "DB_HOST=ECSALB-1d65367beed7ac74.elb.us-east-1.amazonaws.com" -e "DB_PORT=5432" -e "DB_NAME=productms" -e "DB_USER=admin" -e "DB_PASS=passwOrd" productmsapp-image


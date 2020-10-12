On cloud9

git clone https://github.com/amitbajaj45/m2m.git cd m2m/categoryMS/categoryMSApp

region=$(aws configure get region) accountid=$(aws sts get-caller-identity --query Account --output text)

Push the iMage to repo
aws ecr get-login-password
--region $region | docker login
--username AWS
--password-stdin $accountid.dkr.ecr.$region.amazonaws.com

aws ecr create-repository --repository-name m2m/categorymsapp-image

docker build -t categorymsapp-image .

docker tag categorymsapp-image $accountid.dkr.ecr.$region.amazonaws.com/m2m/categorymsapp-image:latest

docker push $accountid.dkr.ecr.$region.amazonaws.com/m2m/categorymsapp-image:latest

from local machine ----

Create Docker Image
docker build -t categorymsapp-image .

Push it to ECR

Replace m2mprofile with correct AWS profile.

region=$(aws configure get region --profile m2mprofile) accountid=$(aws sts get-caller-identity --query Account --output text --profile m2mprofile)

Push the iMage to repo
aws ecr get-login-password
--region $region --profile m2mprofile | docker login
--username AWS
--password-stdin $accountid.dkr.ecr.$region.amazonaws.com

aws ecr create-repository --profile m2mprofile --repository-name m2m/categorymsapp-image

docker tag categorymsapp-image $accountid.dkr.ecr.$region.amazonaws.com/m2m/categorymsapp-image:latest

docker push $accountid.dkr.ecr.$region.amazonaws.com/m2m/categorymsapp-image:latest

To run it on local docker container, use below command:
docker run -d --name categoryms-container -p 8080:8080 -p 9990:9990 categorymsapp-image

docker run -d --name categoryms-container1 -p 8080:8080 -p 9990:9990 -e "DB_URL=jdbc:postgresql://ECSALB-1d65367beed7ac74.elb.us-east-1.amazonaws.com:5432/categoryms?ApplicationName=categoryMicroService" -e "DB_HOST=ECSALB-1d65367beed7ac74.elb.us-east-1.amazonaws.com" -e "DB_PORT=5432" -e "DB_NAME=categoryms" -e "DB_USER=admin" -e "DB_PASS=passwOrd" categorymsapp-image

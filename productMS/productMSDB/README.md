* clone the git repo if not done already

git clone https://github.com/amitbajaj45/m2m.git 

On Cloud9
cd m2m/productMS/productMSDB

docker build -t productmsdb-ubuntu-image .

region=$(aws configure get region)
accountid=$(aws sts get-caller-identity --query Account --output text)

* Push the iMage to repo

aws ecr get-login-password \
  --region $region | docker login \
  --username AWS \
  --password-stdin $accountid.dkr.ecr.$region.amazonaws.com
  

aws ecr create-repository --repository-name m2m/productmsdb-ubuntu-image

  

docker tag productmsdb-ubuntu-image $accountid.dkr.ecr.$region.amazonaws.com/m2m/productmsdb-ubuntu-image:latest

docker push $accountid.dkr.ecr.$region.amazonaws.com/m2m/productmsdb-ubuntu-image:latest


aws s3api create-bucket --bucket productmsapp-artifacts-${accountid} --create-bucket-configuration LocationConstraint=${region}
aws s3 cp productms-db.yaml s3://productmsapp-artifacts-${accountid}/

Go to s3 bucket and copy the object URL 
for example - https://productmsapp-artifacts-646336443392.s3-us-west-2.amazonaws.com/productms-db.yaml
 

ON local machine

* Create postgres Docker image

docker build -t productmsdb-ubuntu-image .

region=$(aws configure get region --profile m2mprofile)
accountid=$(aws sts get-caller-identity --query Account --output text --profile m2mprofile)

* Push the iMage to repo

aws ecr get-login-password \
  --region $region --profile m2mprofile | docker login \
  --username AWS \
  --password-stdin $accountid.dkr.ecr.$region.amazonaws.com
  

aws ecr create-repository --profile m2mprofile --repository-name m2m/productmsdb-ubuntu-image

  

docker tag productmsdb-ubuntu-image $accountid.dkr.ecr.$region.amazonaws.com/m2m/productmsdb-ubuntu-image:latest

docker push $accountid.dkr.ecr.$region.amazonaws.com/m2m/productmsdb-ubuntu-image:latest


* To Run the docker image on local container

docker run -d --name productms-db-container -p 5432:5432 productmsdb-image

Once Image is available in ECR, create ECS Task definition and launch Fargate service from that.
<USe Cloudformation scripts>

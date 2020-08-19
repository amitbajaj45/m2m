* clone the git repo if not done already

git clone https://github.com/amitbajaj45/m2m.git 

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

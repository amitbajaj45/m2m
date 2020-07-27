#!/bin/bash

export profileuser="m2mprofile"
cd ..
sam build -t template.yaml
sam package --s3-bucket m2m-project-artifacts --template-file .aws-sam/build/template.yaml --output-template-file deployment/m2m_deployment_template.yml --profile $profileuser
aws s3 cp deployment/m2m_deployment_template.yml s3://m2m-project-artifacts/m2m_deployment_template.yml --profile $profileuser
cd deployment
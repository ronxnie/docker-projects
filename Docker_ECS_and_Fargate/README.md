# Docker ECS & Fargate Project

This project is a learning and deployment setup for containerizing an application with Docker and deploying it to Amazon ECS using AWS Fargate.

## Overview

This repository will be used to document and organize the steps involved in:
- Building a Docker image
- Pushing the image to Amazon ECR
- Creating ECS resources
- Deploying the application on AWS Fargate

## Project Purpose

The main goal of this project is to understand the end-to-end workflow of deploying containerized applications on AWS using modern DevOps practices.

## Getting Started

As files are added to this project, this README will be updated with:
- Project structure
- Setup instructions
- Deployment steps
- Configuration details
- Usage examples

## Files to Be Created

As this project progresses, the following files may be created to support the Docker and ECS deployment workflow:
- Dockerfile for containerizing the application
- requirements.txt for Python dependencies
- app/ directory for application source code
- task-definition.json for ECS task configuration
- ecs-service.json or service configuration files
- deployment scripts such as build.sh or deploy.sh
- .dockerignore to optimize Docker builds

## Deployment Steps

1. Login to AWS and search for ECS (Elastic Container Service).
2. Navigate to the Clusters page and create a new cluster by selecting the Fargate-only option. This ensures that your services run without needing to manage EC2 instances. Provide a meaningful name for your cluster, review the default settings, and then create the cluster.
3. If there is a problem in the Step 2, then please follow the next steps here: Create an IAM role for ECS so that the service can pull images from Amazon ECR and publish logs to CloudWatch. Go to the IAM console, choose Roles, and click Create role. Select AWS service as the trusted entity, choose Elastic Container Service as the service, and then pick the policy for ECS task execution, such as AmazonECSTaskExecutionRolePolicy. Complete the role setup, give it a clear name like ecsTaskExecutionRole, and attach it to your task definition later during deployment. Once done, then create a cluster.
4. Create a public Amazon ECR repository to store your container image. Open the Amazon ECR console, choose Public repositories, and click Create repository. Enter a repository name, choose the visibility as Public, and complete the creation process. After the repository is created, copy the repository URI because it will be used when pushing and pulling your Docker image. Also, on your local head down to any of the operating system and login to the instance using the below 

```bash
aws ecr-public get-login-password --region us-east-1 | docker login --username AWS --password-stdin public.ecr.aws/q8v9z1n
```

5. Create a new role for Elastic Container Service Task and add the permission AmazonECSTaskExecutionRolePolicy. In the IAM console, go to Roles, select Create role, choose AWS service as the trusted entity, and then select Elastic Container Service Task. Attach the managed policy AmazonECSTaskExecutionRolePolicy so the task can pull images and write logs. Give the role a clear name such as ECSBasicTaskExecutionRolePolicy and create it.
6. Build the Docker File and create an image using the below commands:

```bash
docker build -t ronxnie/public_repository_ecs_container .
```

7. Tag the image created by docker for pushing it on the Elastic Container Repository using the below command:

```bash
docker tag ronxnie/public_repository_ecs_container:latest public.ecr.aws/q8v9z1n2/ronxnie/public_repository_ecs_container:latest
```

8. Push the created image to the above created Elastic Container Repository using the below command:

```bash
docker push public.ecr.aws/q8v9z1n2/ronxnie/public_repository_ecs_container:latest
```

9. Access Elastic Container Service and select Task Definition, then create a new task definition from the page. Configure the task definition with the required container settings, assign the ECS task execution role, and set the image to the ECR repository URI that you pushed earlier. Enable the port number as 5000 since the docker image has the port enabled as 5000.
10. Go back to Elastic Container Service, select the created cluster, navigate to the Tasks section, and run a new task using the task definition you just created. In the VPC part make sure to add the Custom TCP as Port 5000 and the CDR as 0.0.0.0/0.
11. Once the task is running, access the Docker image from the public IP address followed by port 5000 to verify the deployment.

## Notes

This README is intentionally kept minimal at the start so it can be expanded as the project evolves.

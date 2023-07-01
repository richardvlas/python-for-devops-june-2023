[![Test Multiple Python Versions](https://github.com/richardvlas/python-for-devops-june-2023/actions/workflows/main.yml/badge.svg)](https://github.com/richardvlas/python-for-devops-june-2023/actions/workflows/main.yml)

![AWS CodeBuild](https://codebuild.ap-southeast-1.amazonaws.com/badges?uuid=eyJlbmNyeXB0ZWREYXRhIjoiYVpjYUIwc1hMR0NMR3ZtWXlhRmIyM0VzNXNqYy9UWmpENjlPRjh4dExTYW1jcFhYc0R3T0J0Yi83czdoR3Y5ZFo4WmJHcndXSy80RUEwOWV6U0tVdlRNPSIsIml2UGFyYW1ldGVyU3BlYyI6IndpWlJmOTVFTU93RE9kWmsiLCJtYXRlcmlhbFNldFNlcmlhbCI6MX0%3D&branch=main)

# Python for DevOps
From Zero Repository for doing Python DevOps work

## Create a project scaffold

### Colab Notebook
* This is an example of how to user [Colab](https://github.com/richardvlas/python-for-devops-june-2023/blob/main/getting_started_python.ipynb)

### Github Codespaces

Build out Python project scaffold:

* [Makefile](https://github.com/richardvlas/python-for-devops-june-2023/blob/main/Makefile)
* [requirements.txt](https://github.com/richardvlas/python-for-devops-june-2023/blob/main/requirements.txt)
* [test_devopslib.py](https://github.com/richardvlas/python-for-devops-june-2023/blob/main/test_devopslib.py)
* [devopslib.py](https://github.com/richardvlas/python-for-devops-june-2023/tree/main/devopslib)
* Dockerfile
* command-line tool
* Microservice

1. Create a virtual environment

    Run the following command to create a virtual environment:

    ```bash
    python3 -m venv ~/.venv
    ```

2. Edit my .bashrc file
    
    Open the .bashrc file in your home directory by following command:

    ```bash
    vim ~/.bashrc
    ```
    Add the following lines to the end of the file:

    ```bash
    source ~/.venv/bin/activate
    ```
    Save and close the file.

3. Activate the virtual environment
    
    Open a new terminal or run the following command to activate the virtual environment:

    ```bash
    source ~/.venv/bin/activate
    ```
    You can verify that the virtual environment is activated by running the following command:

    ```bash
    which python
    ```
    The output should be similar to the following:

    ```bash
    /home/<username>/.venv/bin/python
    ```

4. Call the make command all
    The make command run all steps to build out the project scaffold and deploy it to AWS.

    ```bash
    make all
    ```


### AWS CloudShell
### AWS Cloud9


## Command-Lines Tools and Step Functions
![image](https://github.com/richardvlas/python-for-devops-june-2023/assets/56484490/78a8580f-7a4a-452b-9d8a-605f27a94a72)


## Microservices

## Containerized Continues Delivery of Microservice App

![image](https://github.com/richardvlas/python-for-devops-june-2023/assets/56484490/4d9ff52f-373f-4f8c-baa2-da71a6b1e4fe)



Run the created docker image locally:

    ```bash
    docker run -p 127.0.0.1:8080:8080 a452053221a1
    ```

* `-p`  - publish a container's port(s) to the host
* `a452053221a1` - example image ID to run (get it from `docker images ls`)

### Required AWS Resources

**Amazon ECR**

* Amazon Elastic Container Registry (ECR) is a fully managed container registry service for storing, managing, and deploying Docker container images.

![image](https://github.com/richardvlas/python-for-devops-june-2023/assets/56484490/cec51252-c4a8-4821-bb41-dbcbbc1751cf)

**App Runner**

* AWS App Runner is a fully managed service that simplifies the deployment of containerized applications without the need to manage underlying infrastructure or containers.

![image](https://github.com/richardvlas/python-for-devops-june-2023/assets/56484490/c923c7a7-b39c-4431-8315-d78f00a27baa)

**CodeBuild**

* AWS CodeBuild is a fully managed build service that compiles, tests, and packages your source code to produce artifacts such as Docker container images or deployment packages.

![image](https://github.com/richardvlas/python-for-devops-june-2023/assets/56484490/befe45b5-762c-4a02-b026-a4cf817a0b33)



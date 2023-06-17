[![Test Multiple Python Versions](https://github.com/richardvlas/python-for-devops-june-2023/actions/workflows/main.yml/badge.svg)](https://github.com/richardvlas/python-for-devops-june-2023/actions/workflows/main.yml)

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

## Containerized Continuous Delivery

Run the created docker image locally:

    ```bash
    docker run -p 127.0.0.1:8080:8080 a452053221a1
    ```

    * -p  - publish a container's port(s) to the host
    * image ID - id of the image to run

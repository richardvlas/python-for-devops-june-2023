# Python for DevOps
From Zero Repository for doing Python DevOps work

## Create a project scaffold

### Colab Notebook
* This is an example of how to user [Colab](https://github.com/richardvlas/python-for-devops-june-2023/blob/main/getting_started_python.ipynb)

### Github Codespaces

Build out Python project scaffold:

* Makefile
* requirements.txt
* test_library.py
* python_library
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


### AWS CloudShell
### AWS Cloud9


## Command-Lines Tools

## Microservices

## Containerized Continuous Delivery

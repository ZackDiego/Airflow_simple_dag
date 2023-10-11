# Airflow DAG
## Created following tutorial from [coder2j](https://www.youtube.com/watch?v=K9AnJ9_ZAXE&t=3733s)

## Table of contents
* [General info](#general-info)
* [Main Technologies](#main-technologies)
* [Pre-requisites](#pre-requisites)
* [Setup](#setup)
* [Project Structure](#project-structure)


## General info
This project is experimenting some Airflow functionality 
	
## Main Technologies
Project is created with:
* Apache Airflow version 2.7.1

## Pre-requisites
- Install [Python](https://www.python.org) version 3.11

## Setup
To run this project, install dependencies and run the project with:
```
$ export AIRFLOW_HOME=~/airflow
$ airflow db init    (create sqlite database)
$ airflow create_user \
    --username <USERNAME> \
    --firstname <FIRST_NAME> \
    --lastname <LAST_NAME> \
    --email <EMAIL> \
    --role <ROLE> \
    --password <PASSWORD>
$ airflow webserver -p 8080
```
The airflow web server running on `localhost:8080`, it provides a user interface for managing DAGs, viewing task execution logs, and monitoring the status of tasks and workflows.

OR run with docker(make sure docker is installed) with docker-compose.yaml

```
docker-compose up
```

## Project Structure
The folder structure of this app is explained below:
| Name          | Description                                                                           |
| ------------- | ------------------------------------------------------------------------------------- |
| **dags/**     | Directory containing Apache Airflow Directed Acyclic Graph (DAG) definition files.      |
| **logs/**     | Directory where Airflow stores task execution logs and other log-related information.  |
| **airflow.cfg** | Airflow configuration file containing settings for the Airflow web server and scheduler. |



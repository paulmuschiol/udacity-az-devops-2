# Overview

Udacity Azure DevOps Project 2
Goal of the project is to setup a small ML app in Azure AppServices using a CI/CD pipeline.

## Project Plan

* [Trello Board](https://trello.com/b/gBSg2Be7/udacity-devops-r2)
* [Project plan](https://docs.google.com/spreadsheets/d/1eglH8eQMsFBMbxrhoCgWaRv9xnAr1unJ7hDYKaKsSjg/edit?usp=sharing)

## Instructions

<TODO:  
* Architectural Diagram (Shows how key parts of the system work)>

<TODO:  Instructions for running the Python project.  How could a user with no context run this project without asking you for any help.  Include screenshots with explicit steps to create that work. Be sure to at least include the following screenshots:

### Preparation
* Open up Azure Cloud Shell. If not done so create SSH Key and add to your github account.
* Clone the project from github into your azure cloud shell
* Create a virtual environment for python to run in.
![Alt](img/venv.png "Venv")

### Local Deployment
* To setup the evironment locally run `"make install_test" ` in the cloned project folder to install dependencies.
* You can now directly deploy your webapp to an Azure WebApp by running `az webapp up -n <your-appservice>` in the project folder in the Azure Cloud Shell. The "your-appservice" must be replaced by a globally unique string identifying your app. This can take a minute to deploy.
* This gives you a web address at the end you can look up. It should give you something similiar to this:
![Demo](img/demo.png "Demo")
* You can stream your logs in Azure Cloud Shell by `az webapp log tail`. You should see eomthing as below:
![Log](img/log.png "Log")
* Running `make all` additionally tests your environment. You should get below test result:
![make all](img/makeall.png "make all")

### Setup Azure Pipeline
* Go to Azure DevOps and create new project if required
* Navigate to Project Settings / Service Connections and setup a Service connection to aour Azure subscription (for details refer to the official documentation)
* Setup a pipeline by creating a new Pipeline. Refer here to your forked Git Project or setup a Azure Repo. For configuration you can utilize the [azure-pipelines.yml](azure-pipelines.yml) template pipeline.


* Project running on Azure App Service

* Project cloned into Azure Cloud Shell

* Passing tests that are displayed after running the `make all` command from the `Makefile`

* Output of a test run

* Successful deploy of the project in Azure Pipelines.  [Note the official documentation should be referred to and double checked as you setup CI/CD](https://docs.microsoft.com/en-us/azure/devops/pipelines/ecosystems/python-webapp?view=azure-devops).

* Running Azure App Service from Azure Pipelines automatic deployment

* Successful prediction from deployed flask app in Azure Cloud Shell.  [Use this file as a template for the deployed prediction](https://github.com/udacity/nd082-Azure-Cloud-DevOps-Starter-Code/blob/master/C2-AgileDevelopmentwithAzure/project/starter_files/flask-sklearn/make_predict_azure_app.sh).
The output should look similar to this:

```bash
udacity@Azure:~$ ./make_predict_azure_app.sh
Port: 443
{"prediction":[20.35373177134412]}
```

* Output of streamed log files from deployed application

> 

## Enhancements

<TODO: A short description of how to improve the project in the future>

## Demo 

<TODO: Add link Screencast on YouTube>



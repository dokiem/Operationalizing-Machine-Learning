# Operationalizing Machine Learning

In this project, we will work with Bank Makerting data and use Azure to configure a cloud-based machine learning production model, deploy it, and consume it. Additionally, we will also create, publish, and consume a pipeline. In the end, we will demonstrate all of my work by creating a README file and a screencast video

## Architectural Diagram

This is a architectural diagram that shows main steps, including authentication, automated ML experiment, deploy the best model, enable logging, swagger documentation, consume model endpoints, create and publish a pipeline and documentation
<img align="center" width="700" height="300" src="https://github.com/dokiem/Ex2/blob/main/images/Architecture-Diagram.png">

## Key Steps

1. Authentication

In this step, we need to practise with authentication from my local with Azure machine learning by install Azure CLI and do the command az login. We also can test creating Service Principal account and associate it with specific workspace.

2. Automated ML Experiment

We need to upload the file "BankMarketing.cs" to the dataset and create a new automated ML experiment, then we configure a new compute cluster and finally, we run the experiment using classification

<img align="center" width="700" height="300" src="https://github.com/dokiem/Ex2/blob/main/images/4.1.png">

<img align="center" width="700" height="300" src="https://github.com/dokiem/Ex2/blob/main/images/4.2.png">

<img align="center" width="700" height="300" src="https://github.com/dokiem/Ex2/blob/main/images/4.3.png">

3. Deploy the best model

We create a deployment for the best model and get endpoint, authentication info to predict the data

4. Enable logging

To enable logging for a deployment, we can use python with azureml-core to call the endpoint service and update configuration. However, I faced problem with the command, you can see in the picture below. Besides that, you can see logs getting from the service.

<img align="center" width="700" height="300" src="https://github.com/dokiem/Ex2/blob/main/images/6.1.png">

<img align="center" width="700" height="300" src="https://github.com/dokiem/Ex2/blob/main/images/6.2.png">

5. Swagger Documentation

To see swagger documentation, we can get swagger.json file and create a new swagger api server to explain the json file

<img align="center" width="700" height="300" src="https://github.com/dokiem/Ex2/blob/main/images/7.1.png">

<img align="center" width="700" height="300" src="https://github.com/dokiem/Ex2/blob/main/images/7.2.png">

6. Consume model endpoints

In order to consume the service endpoint, we can use python to call the endpoint api with key to get the result

<img align="center" width="700" height="300" src="https://github.com/dokiem/Ex2/blob/main/images/8.1.png">

7. Create and publish a pipeline

We create a pipeline to train the csv data and see the result of trainning progressing

<img align="center" width="700" height="300" src="https://github.com/dokiem/Ex2/blob/main/images/9.1.png">

<img align="center" width="700" height="300" src="https://github.com/dokiem/Ex2/blob/main/images/9.2.png">

<img align="center" width="700" height="300" src="https://github.com/dokiem/Ex2/blob/main/images/9.3.png">

<img align="center" width="700" height="300" src="https://github.com/dokiem/Ex2/blob/main/images/9.4.png">

<img align="center" width="700" height="300" src="https://github.com/dokiem/Ex2/blob/main/images/9.5.png">

<img align="center" width="700" height="300" src="https://github.com/dokiem/Ex2/blob/main/images/9.6.png">

<img align="center" width="700" height="300" src="https://github.com/dokiem/Ex2/blob/main/images/9.7.png">

## Screen Recording

You can watch the demo video [here](https://github.com/dokiem/Ex2/blob/main/video/kiemdv1-demostration.mkv).

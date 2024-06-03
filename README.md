# Operationalizing Machine Learning

In this project, we will work with Bank Marketing data and use Azure to configure a cloud-based machine learning production model, deploy it, and consume it. Additionally, we will also create, publish, and consume a pipeline.

## Architectural Diagram

This architectural diagram shows the main steps, including authentication, automated ML experiment, deploying the best model, enabling logging, swagger documentation, consuming model endpoints, creating and publishing a pipeline and documentation.

<img align="center" width="700" height="300" src="https://github.com/dokiem/Operationalizing-Machine-Learning/blob/main/images/Architecture-Diagram.png">

## Key Steps

1. Authentication

In this step, we need to practice authentication from my local with Azure machine learning by installing Azure CLI and doing the command az login. We also can test creating a Service Principal account and associate it with a specific workspace.

2. Automated ML Experiment

We need to upload the file "BankMarketing.cs" to the dataset and create a new automated ML experiment, then we configure a new compute cluster and finally, we run the experiment using classification

<img align="center" width="700" height="300" src="https://github.com/dokiem/Operationalizing-Machine-Learning/blob/main/images/4.1.png">

<img align="center" width="700" height="300" src="https://github.com/dokiem/Operationalizing-Machine-Learning/blob/main/images/4.2.png">

<img align="center" width="700" height="300" src="https://github.com/dokiem/Operationalizing-Machine-Learning/blob/main/images/4.3.png">

3. Deploy the best model

We create a deployment for the best model and get endpoint, authentication info to predict the data

4. Enable logging

To enable logging for deployment, we can use Python with azure ml-core to call the endpoint service and update configuration. However, I faced a problem with the command, as you can see in the picture below. Besides that, you can see logs getting from the service.

<img align="center" width="700" height="300" src="https://github.com/dokiem/Operationalizing-Machine-Learning/blob/main/images/6.1.png">

<img align="center" width="700" height="300" src="https://github.com/dokiem/Operationalizing-Machine-Learning/blob/main/images/6.2.png">

5. Swagger Documentation

We can get swagger.json file and create a new swagger API server to see the explanation

<img align="center" width="700" height="300" src="https://github.com/dokiem/Operationalizing-Machine-Learning/blob/main/images/7.1.png">

<img align="center" width="700" height="300" src="https://github.com/dokiem/Operationalizing-Machine-Learning/blob/main/images/7.2.png">

6. Consume model endpoints

In order to consume the service endpoint, we can use python to call the endpoint API with key to get the result

<img align="center" width="700" height="300" src="https://github.com/dokiem/Operationalizing-Machine-Learning/blob/main/images/8.1.png">

7. Create and publish a pipeline

We create a pipeline to train the data and see the training progressing

<img align="center" width="700" height="300" src="https://github.com/dokiem/Operationalizing-Machine-Learning/blob/main/images/9.1.png">

<img align="center" width="700" height="300" src="https://github.com/dokiem/Operationalizing-Machine-Learning/blob/main/images/9.2.png">

<img align="center" width="700" height="300" src="https://github.com/dokiem/Operationalizing-Machine-Learning/blob/main/images/9.3.png">

<img align="center" width="700" height="300" src="https://github.com/dokiem/Operationalizing-Machine-Learning/blob/main/images/9.4.png">

<img align="center" width="700" height="300" src="https://github.com/dokiem/Operationalizing-Machine-Learning/blob/main/images/9.5.png">

<img align="center" width="700" height="300" src="https://github.com/dokiem/Operationalizing-Machine-Learning/blob/main/images/9.6.png">

<img align="center" width="700" height="300" src="https://github.com/dokiem/Operationalizing-Machine-Learning/blob/main/images/9.7.png">

## Screen Recording

You can watch the demo video [here](https://youtu.be/czj5s-_Upik).

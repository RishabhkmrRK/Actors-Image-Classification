# Important Links:
1. Dataset - [Download from Google Images](https://github.com/RishabhkmrRK/Actors_image_classification_using_sklearn_with_EC2_model_deployment/tree/main/dataset/images)
2. Model Training - [Notebook](https://github.com/RishabhkmrRK/Actors_image_classification_using_sklearn_with_EC2_model_deployment/blob/main/model_training.ipynb)
3. Model deployment - [AWS EC2 Instance](http://ec2-52-66-249-90.ap-south-1.compute.amazonaws.com)

---

## Introduction
In this project, I have trained and deployed a machine learning model which classifies the images of Tv show "The Big Bang Theory" actors: Howard, Leonard, Raj and Sheldon. `Google images` was used to Gather data, `Sklearn` libraries to train model and `Amazon Web Services EC2` Instance to deploy model. 

## Workflow 
![ML model development process1](https://user-images.githubusercontent.com/30430757/176646092-196499ac-c780-4414-9c35-1e9f87ac3778.jpeg)

1. Data Preparation
    * Data Gathering/Web Scrapping: To gather data, `Fatkun` google chrome extension was used to bulk download images of respective actors from google.
    * Data cleaning: After downloading Raw dataset, python script was used to clean which reject images those do not have clear image and both eyes are not visible using opencv library. As opencv can only find images with proper face and two eyes visib;e, manually deletion of non required actor iamges from respective actors directory in dataset had be performed.

2. Feature Engineering
    * Feature Extraction: In this step, image was sized to 32x32 pixels and then pyWavelet was used to extract feature from image. After extracting feature from image, extracted image was vertical stack with the original one making the size of image 4096 (32x32x3 + 32x32).
    * Data Scaling: Scaling of the data was performed to makes it easy for a model to learn and understand the problem. Each data point in features was in range 0-255 (as each pixel is 8 bytes - 255 bits) and was scaled to 0-1 range using sklearn's `MinMaxScaler`.

3. Model Building
    * Model Training: To train model having 4096 features and bring a classifcation problem, Sklearn library modules `Logistic Regression`, `Random Forest` and `Support Vector Machine` were used.
    * Evaluation: To perform evaluation, sklearn `GridSearchCV` module was used to hypertune the parameter of each classification module.
    * Model Selection: The model with high accuracy and F1 score was selected which was Support Vector Machine with parameters: {'svc__C': 1, 'svc__kernel': 'linear'}.

4. Model Deployment
    * User Interface/client: This is web-page built using HTML, CSS and JavaScript which is used for interaction with user. Drop box is present here in which user uploads the needs to be classify image and get the prediction. Here `Nginx` used for web-hosting and reverse proxy.
    * Flask: Flask is a micro web framework written in Python. Server side programing was done here which recieves image from the client(user interface) and send the prediction back to client using saved model prection pickle file.    
    * AWS Ec2 Instance: Amazon Web Services Ec2 Instance was used to deploy the model containing all the server side and client side files.

## Conclusion

(#sklearn #web-scrapping #heruko #ML)
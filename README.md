# Important Links:
1. Dataset - [Download from Google Images](https://github.com/RishabhkmrRK/Actors_image_classification_using_sklearn_with_EC2_model_deployment/tree/main/dataset/images)
2. Model Training - [Notebook](https://github.com/RishabhkmrRK/Actors_image_classification_using_sklearn_with_EC2_model_deployment/blob/main/model_training.ipynb)
3. Model deployment - [AWS EC2 Instance](http://ec2-52-66-249-90.ap-south-1.compute.amazonaws.com)
    * Note: Due to limited dataset, model can only classify clear single person image with both eyes visible.

# Languages and Tools used:
[<img align="left" alt="jupyter" width="26px" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/jupyter/jupyter-original-wordmark.svg" style="padding-right:10px;"/>](https://jupyter.org/ "Jupyter Notebook")
[<img align="left" alt="opencv" width="26px" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/opencv/opencv-original.svg" style="padding-right:10px;"/>](https://opencv.org/ "OpenCV")
[<img align="left" alt="Python" width="26px" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" style="padding-right:10px;" />](https://www.python.org/ "Python")
[<img align="left" alt="flask" width="26px" fill= #000000 src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/flask/flask-original.svg" style="padding-right:10px;"/>](https://flask.palletsprojects.com/en/2.1.x/ "Flask")
[<img align="left" alt="nginx" width="26px" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/nginx/nginx-original.svg" style="padding-right:10px;" />](https://www.nginx.com/ "Nginx")
[<img align="left" alt="html" width="26px" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/html5/html5-original.svg" style="padding-right:10px;"/>](https://www.w3schools.com/tags/att_download.asp "HTML")
[<img align="left" alt="css" width="26px" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/css3/css3-original.svg" style="padding-right:10px;"/>](https://developer.mozilla.org/en-US/docs/Web/CSS "CSS")
[<img align="left" alt="javascript" width="26px" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/javascript/javascript-original.svg" style="padding-right:10px;"/>](https://www.javascript.com/ "JavaScript")
[<img align="left" alt="aws" width="26px" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/amazonwebservices/amazonwebservices-original.svg" style="padding-right:10px;" />](https://aws.amazon.com/ "AWS")

<br />
<br />
<br />


## Overview
In this project, I have trained and deployed a machine learning model which classifies the images of Tv show "The Big Bang Theory" actors: Howard, Leonard, Raj and Sheldon. `Google images` was used to Gather data, `Sklearn` libraries to train model and `Amazon Web Services EC2` Instance to deploy model. 

This project comes under Machine Learning Classification problem having 4 labels.
<br />
<br />

## Workflow
![ML model development process](https://user-images.githubusercontent.com/30430757/177333856-69c7dc27-c804-483c-9193-052d7acf9857.jpeg)

1. Data Preparation
    * Data Gathering/Web Scrapping: To gather data, `Fatkun` google chrome extension was used to bulk download images of respective actors from google.[Dataset](https://github.com/RishabhkmrRK/Actors_image_classification_using_sklearn_with_EC2_model_deployment/tree/main/dataset/images)
    * Data cleaning: After downloading Raw dataset, python script was used to clean which reject images those do not have clear image and both eyes are not visible using opencv library. As opencv can only find images with proper face and two eyes visib;e, manually deletion of non required actor iamges from respective actors directory in dataset had be performed.[Cleaning Code](https://github.com/RishabhkmrRK/Actors_image_classification_using_sklearn_with_EC2_model_deployment/blob/main/dataset_cleaning.ipynb)

2. Feature Engineering
    * Feature Extraction: In this step, image was sized to 32x32 pixels and then pyWavelet was used to extract feature from image. After extracting feature from image, extracted image was vertical stack with the original one making the size of image 4096 (32x32x3 + 32x32).
    * Data Scaling: Scaling of the data was performed to makes it easy for a model to learn and understand the problem. Each data point in features was in range 0-255 (as each pixel is 8 bytes - 255 bits) and was scaled to 0-1 range using sklearn's `MinMaxScaler`.

3. Model Building
    * Model Training: To train model having 4096 features and being a classifcation problem, Sklearn library modules `Logistic Regression`, `Random Forest` and `Support Vector Machine` were used.
    * Evaluation: To perform evaluation, sklearn `GridSearchCV` module was used to hypertune the parameter of each classification module.
    * Model Selection: The model with high accuracy  was selected which was Support Vector Machine with parameters: {'svc__C': 1, 'svc__kernel': 'linear'}.

4. Model Deployment
    * User Interface/client: This is web-page built using HTML, CSS and JavaScript which is used for interaction with user. Drop box is present here in which user uploads the needs to be classify image and get the prediction. Here `Nginx` used for web-hosting and reverse proxy.
    * Flask: Flask is a micro web framework written in Python. Server side programing was done here which recieves image from the client(user interface) and send the prediction back to client using saved model prection pickle file.    
    * AWS Ec2 Instance: Amazon Web Services Ec2 Instance was used to deploy the model containing all the server side and client side files.

<br />
<br />

## Conclusion

Model was successfully trained and deployed with 84% accuracy but due to limited dataset, model can only classify clear single person image with both eyes visible.

<br />
<br />

## Future Target
Next Step is to implement the same Classification Model using Deep-Learning (Neural Networks) and with much bigger dataset in hand.

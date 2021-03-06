# Disaster-pipeline-using-sklearn

## Project Summary:

This project is part of Udacity Data Science nanodegree program: Disaster Response Project.
This project is used to build a model that classifies disaster messages. Using the web app an emergency worker can input a new message and get classification results in several categories, which helps in getting the idea ofwhat kind of help is needed. Example: "food", "shelter" etc.

## Installation Instructions:

1. Download / clone the repository to local using below command.

https://github.com/Tara889/Disaster-pipeline-using-sklearn

2. Create and activate Anaconda environment, using below command.

conda create -n env-name python=3.6

conda activate env-name

3. cd into directory, install python dependencies using below command.

pip install -r requirements.txt

## Files and Data descriptions:

1. process_data.py: 

  This code extracts data from both CSV files messages.csv which contain message data and categories.csv which contain classes of messages and creates an merged and cleaned version of this data.
  
2. train_classifier.py: 

  This code takes the database produced by process_data.py as an input and uses the data in it to train a ML model for categorizing messages. 
  The output is a pickle file containing the fitted model. 
  
## Application Installation Instructions:

Run the below commands below.

  1. python process_data.py disaster_messages.csv disaster_categories.csv DisasterResponse.db
 
  once the command is executed you will find the file DiasasterResponse.db created and then run the next command below.
 
  2. python train_classifier.py ../data/DisasterResponse.db classifier.pkl

  once the above is executed your model are trained and build and next you can run the app by below command.

  3. python run.py

  Run the web application Go to http://0.0.0.0:3001/ (if facing problems try http://localhost:3001 in a local browser)
  
## Results:

![image](https://user-images.githubusercontent.com/87708828/130799265-4762c7ed-5282-4200-963f-ca1341c7728a.png)






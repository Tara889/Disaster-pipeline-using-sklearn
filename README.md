# Disaster-pipeline-using-sklearn

## Project Summary:

This project is part of Udacity Data Science nanodegree program: Disaster Response Project.
This project is used to build a model that classifies disaster messages. Using the web app an emergency worker can input a new message and get classification results in several categories, which helps in getting the idea ofwhat kind of help is needed. Example: "water", "shelter", "food", etc.

The web app also displays visualizations of the data.

Run the web application Go to http://0.0.0.0:3001/ (if facing problems try http://localhost:3001 in a browser)


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

In a terminal navigate to the project directory udacity-disaster-response/ (that contains this README) and run commands in the following sequence:

1. python process_data.py disaster_messages.csv disaster_categories.csv DisasterResponse.db
2. python train_classifier.py ../data/DisasterResponse.db classifier.pkl
3. python run.py

Run the web application Go to http://0.0.0.0:3001/ (if facing problems try http://localhost:3001 in a browser)
  
# Results:






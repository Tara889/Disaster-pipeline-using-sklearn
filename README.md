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

## Application Installation Instructions:

In a terminal navigate to the project directory udacity-disaster-response/ (that contains this README) and run commands in the following sequence:

1. python process_data.py disaster_messages.csv disaster_categories.csv DisasterResponse.db
2. python train_classifier.py ../data/DisasterResponse.db classifier.pkl
3. python run.py

Run the web application Go to http://0.0.0.0:3001/ (if facing problems try http://localhost:3001 in a browser)

## File descriptions:

1. Seattle Airbnb Dataset.ipynb -> Main jupyter notebook file(code)
2. listings.csv -> Input data - Air Bnb Seattle listings data-set
3. readme.md -> Instructions file

# Results:



# Acknowledgement and Referemces:
This data can be downloaded from https://www.kaggle.com/airbnb/seattle


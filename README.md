# Disaster-pipeline-using-sklearn

## Installation Instructions:

1. Download / clone the repository to local using below command.

https://github.com/Tara889/Disaster-pipeline-using-sklearn

2. Create and activate Anaconda environment, using below command.

conda create -n env-name python=3.6

conda activate env-name

3. cd into directory, install python dependencies using below command.

pip install -r requirements.txt

## Application Installation Instructions:

1. Data Files
  Run the data file by using the below command
  
  python process_data.py disaster_messages.csv disaster_categories.csv DisasterResponse.db
  
2. Model Files 

  Run the data file by using the below command
  
  python train_classifier.py ../data/DisasterResponse.db classifier.pkl

3. App Files
  
  Run the app, by using command below.

  phython run.py

## Project motivation:

This project is part of Udacity Data Science nanodegree program: Disaster Response Project.




## File descriptions:

1. Seattle Airbnb Dataset.ipynb -> Main jupyter notebook file(code)
2. listings.csv -> Input data - Air Bnb Seattle listings data-set
3. readme.md -> Instructions file

# Results:



# Acknowledgement and Referemces:
This data can be downloaded from https://www.kaggle.com/airbnb/seattle


"""
Created on Mon Aug 23 17:59:00

@author: Name: Tara Devi
         Email: nakshatra1988@gmail.com

"""

import sys
import pandas as pd
from sqlalchemy import create_engine

def load_data(messages_file, categories_file):
    '''
    input:
        messages_file: messages dataset file path.
        categories_file: categories dataset file path.
    output:
        df: The merged dataset
    '''
    messages = pd.read_csv(messages_file)
    categories = pd.read_csv(categories_file)
    df = pd.merge(messages, categories, left_on='id', right_on='id', how='outer')
    return df

def clean_data(df):
    '''
    input:
        df: The merged dataset in previous step.
    output:
        df: Dataset after cleaning.
    '''
    categories = df.categories.str.split(';', expand = True)
    row = categories.loc[0]
    category_colnames = row.apply(lambda x: x[:-2]).values.tolist()
    categories.columns = category_colnames
    categories.related.loc[categories.related == 'related-2'] = 'related-1'
    for column in categories:
        categories[column] = categories[column].astype(str).str[-1]
        categories[column] = pd.to_numeric(categories[column])
    df.drop('categories', axis = 1, inplace = True)
    df = pd.concat([df, categories], axis = 1)
    df.drop_duplicates(subset = 'id', inplace = True)
    return df

def save_data(df, database_file):
    engine = create_engine('sqlite:///' + database_file)
    df.to_sql('InsertTableName', engine, index=False)

def main():
    if len(sys.argv) == 4:

        messages_file, categories_file, database_file = sys.argv[1:]

        print('Loading data...\n    MESSAGES: {}\n    CATEGORIES: {}'
              .format(messages_file, categories_file))
        df = load_data(messages_file, categories_file)

        print('Cleaning data...')
        df = clean_data(df)

        print('Saving data...\n    DATABASE: {}'.format(database_file))
        save_data(df, database_file)

        print('Cleaned data saved to database!')

    else:
        print('Please provide the filepaths of the messages and categories '\
              'datasets as the first and second argument respectively, as '\
              'well as the filepath of the database to save the cleaned data '\
              'to as the third argument. \n\nExample: python process_data.py '\
              'disaster_messages.csv disaster_categories.csv '\
              'DisasterResponse.db')


if __name__ == '__main__':
    main()

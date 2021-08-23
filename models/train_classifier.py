"""
Created on Mon Aug 23 17:59:00

@author: Name: Tara Devi
         Email: nakshatra1988@gmail.com

"""

import sys
import nltk
import re
nltk.download(['punkt', 'wordnet'])
import warnings
warnings.filterwarnings("ignore")
import pandas as pd
from sqlalchemy import create_engine
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from sklearn.multioutput import MultiOutputClassifier
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
#from sklearn.externals import joblib
import joblib
from sklearn.metrics import classification_report, accuracy_score
from sklearn.multiclass import OneVsRestClassifier
from sklearn.svm import LinearSVC

def load_data(database_file):
    '''
    input:
        database_file: File path where sql database is saved.
    output:
        X: Training message List.
        Y: Training target.
        category_names: Categorical name for labeling.
    '''
    engine = create_engine('sqlite:///'+ database_file)
    df = pd.read_sql_table('InsertTableName', engine)
    X = df.message.values
    Y = df[df.columns[4:]].values
    category_names = list(df.columns[4:])
    return X, Y, category_names

def tokenize(text):
    '''
    input:
        text: Message data for tokenization.
    output:
        tokens: Result after tokenization.
    '''
    text = re.sub(r"[^a-zA-Z0-9]", " ", text.lower())
    token = word_tokenize(text)
    lemmatizer = WordNetLemmatizer()

    tokens = []
    for tok in token:
        clean_tok = lemmatizer.lemmatize(tok).lower().strip()
        tokens.append(clean_tok)
    return tokens


def build_model():
    '''
    input:
        None
    output:
        cv: GridSearch model result.
    '''
    pipeline = Pipeline([
        ('vect', CountVectorizer(tokenizer=tokenize)),
        ('tfidf', TfidfTransformer()),
        ('clf', MultiOutputClassifier(OneVsRestClassifier(LinearSVC(random_state = 0))))
    ])
    parameters = {
                'tfidf__smooth_idf':[True, False],
                'clf__estimator__estimator__C': [1, 2, 5]
             }
    cv = GridSearchCV(pipeline, param_grid=parameters, scoring='precision_samples', cv = 5)
    return cv

def evaluate_model(model, X_test, Y_test, category_names):
    Y_pred = model.predict(X_test)
    print(classification_report(Y_test, Y_pred, target_names = category_names))
    print('---------------------------------')
    for i in range(Y_test.shape[1]):
        print('%25s accuracy : %.2f' %(category_names[i], accuracy_score(Y_test[:,i], Y_pred[:,i])))

def save_model(model, model_file):
    joblib.dump(model, model_file)


def main():
    if len(sys.argv) == 3:
        database_file, model_file = sys.argv[1:]  #python train_classifier.py ../data/DisasterResponse.db classifier.pkl
        print('Loading data...\n    DATABASE: {}'.format(database_file))
        X, Y, category_names = load_data(database_file)
        X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)

        print('Building model...')
        model = build_model()

        print('Training model...')
        model.fit(X_train, Y_train)

        print('Evaluating model...')
        evaluate_model(model, X_test, Y_test, category_names)

        print('Saving model...\n    MODEL: {}'.format(model_file))
        save_model(model, model_file)

        print('Trained model saved!')

    else:
        print('Provide the filepath of the disaster messages database '\
              'as the first argument and the filepath of the pickle file to '\
              'save the model to as the second argument. \n\nExample: python '\
              'train_classifier.py ../data/DisasterResponse.db classifier.pkl')


if __name__ == '__main__':
    main()

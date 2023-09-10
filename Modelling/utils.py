"""
Modelling/utils.py
------------------
Utility functions
"""

import nltk
import re
from nltk.stem import WordNetLemmatizer
from Modelling.config import stopwords_list
from catboost import CatBoostClassifier

def remove_stopwords(text: str) -> str:
    words = nltk.word_tokenize(text.lower())
    lemmatizer = WordNetLemmatizer()
    lemmatized_words = [lemmatizer.lemmatize(word) for word in words]
    filtered_words = [word for word in lemmatized_words if word.isalpha() and word not in stopwords_list]
    clean_text = ' '.join(filtered_words)
    clean_text = re.sub(r'\s+', ' ', clean_text).strip()
    return clean_text


class ModelInference:
    def __init__(self,model_path,data):
        self.model_path = model_path
        self.data = data

    def preprocess_data(self):
        self.clean_text = remove_stopwords(self.data)
        return self.clean_text
    
    def get_model_prediction(self):
        if self.model_path.split(".")[-1] == "cbm":
            catboost_model = CatBoostClassifier()
            model = catboost_model.load_model(self.model_path)
        else:
            return "Invalid Model Type"
        
        prediction = model.predict([self.clean_text])
        probability = max(model.predict_proba([self.clean_text]))

        return {"result":prediction[0],"confidence_score":probability}
    

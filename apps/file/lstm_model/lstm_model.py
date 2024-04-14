import os
import json
from pathlib import Path

import pandas as pd
from pymystem3 import Mystem
from keras.models import load_model
from keras.utils import pad_sequences
from keras.preprocessing.text import Tokenizer, tokenizer_from_json


class Model:

    base_dir = Path(__file__).resolve().parent.parent

    model_relative_path = "best_model_LSTM10000_2.h5"
    tokenizer_relative_path = "tokenizer_json.json"

    def get_path_model(self):
        return str(self.base_dir) + "/lstm_model/best_model_LSTM10000_2.h5"

    def get_path_tokenizer(self):
        return str(self.base_dir) + "/lstm_model/tokenizer_json.json"


def process_file_data(file_path, name_column):
    data_comments = pd.read_excel(file_path)[name_column]
    m = Mystem()
    commentaries = []
    coefficient = []
    marks = []

    for comment_index in range(len(data_comments)):
        if type(data_comments[comment_index]) == str:
            lemms = m.lemmatize(data_comments[comment_index])
            prep = [word.strip(r'!?"#$%&()*+,-./:;<=>?@[\\]^_`{|}~\t\n').lower() for word in lemms if word.isalpha()]
            sequence = tokenizer.texts_to_sequences([' '.join(prep)])
            sequence = pad_sequences(sequence, 64)
            score = model.predict(sequence)

            if score[[0]] > 0.9:
                commentaries.append(data_comments[comment_index])
                marks.append('Отрицательный')
                coefficient.append(score)

            elif 0.9 > score[[0]] > 0.4:
                commentaries.append(data_comments[comment_index])
                marks.append('Нейтральный')
                coefficient.append(score)

            else:
                commentaries.append(data_comments[comment_index])
                marks.append('Положительный')
                coefficient.append(score)

    data = pd.DataFrame()
    data['Сообщение'] = commentaries
    data['Класс'] = marks
    data['Коэффициент'] = coefficient
    data.to_excel(file_path)


model_lstm = Model()

model = load_model(model_lstm.get_path_model())

with open(model_lstm.get_path_tokenizer()) as file:
    data = json.load(file)
    tokenizer = tokenizer_from_json(data)

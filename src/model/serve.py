from flask import Flask, render_template, request
from src.CONSTANTS import *
from src.utilities import prepare_inference_df

import numpy as np
import pandas as pd
import joblib
import os
import sys
import logging

sys.path.append("models")
sys.path.append("src/model")

curr_file_path = "src/model"
models_dirpath = 'models/'
template_dir = os.path.join(os.getcwd(), 'src/templates')

app = Flask(__name__, template_folder=template_dir)
model = joblib.load(open(os.getcwd() + '/' + models_dirpath + TRAINED_MODEL_NAME, 'rb'))


@app.route('/')
def index():
    logging.info('Rendering index template!')
    return render_template('index.html')


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    req = pd.DataFrame(request.form.to_dict(), index=[0])[REQUEST_COLUMNS]
    req[float_cols] = req[float_cols].astype(np.float32)
    req = prepare_inference_df(req)
    prediction = model.predict(req)
    logging.info('Predicted price:[{}]'.format(prediction))
    return render_template('index.html',
                           data="$" + str(np.around(prediction[0], decimals=2)))


if __name__ == '__main__':
    app.run(debug=True)

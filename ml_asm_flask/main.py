from flask import Flask, request, jsonify, redirect, url_for
import json
import numpy as np
import pickle
import tensorflow as tf
from tensorflow import keras

app = Flask(__name__)

@app.route("/get_ml_pred", methods=['POST'])
def get_ml_pred():
	ml_data = request.get_json()
	ml_pred = np.array2string(ml_model.predict(ml_data))

	return jsonify(ml_pred)

@app.route("/get_ann_pred", methods=['POST'])
def get_ann_pred():
	ann_data = request.get_json()
	ann_pred = np.array2string(ann_model.predict(ann_data))

	return jsonify(ann_pred)

if __name__ ==" __main__":
	ann_model = keras.models.load_model("/wine_qualifier", compile=True)
	ml_model = pickle.load(open("better_or_not.pickle", "rb"))

	print(ann_model.summary())


	app.run(debug=True, host='0.0.0.0')

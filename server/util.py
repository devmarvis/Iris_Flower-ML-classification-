import json
import joblib
import numpy as np


__model = None
__class_number_to_specie = {}

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
json_path = os.path.join(BASE_DIR, "num_to_specie_dict.json")
model_path = os.path.join(BASE_DIR, "classifier.pkl")


def load_saved_artifacts():
    print("loading saved artifacts...start")
    global __model, __class_number_to_specie

    with open(json_path, "r") as f:
        __class_number_to_specie = json.load(f)

    if __model is None:
        try:
            with open(model_path, "rb") as f:
                __model = joblib.load(f)
        except:
            print("Couldn't load model")



    print("loading saved artifacts...done")



def classify_flower(x_features):
    final_2d = np.reshape(np.array(x_features), (1, -1))
    pred = str(__model.predict(final_2d)[0])
    specie = __class_number_to_specie[pred]

    return {
        "specie": specie
    }


if __name__ == "__main__":
    load_saved_artifacts()
    print(classify_flower([7.4, 2.8, 6.1, 1.9]))
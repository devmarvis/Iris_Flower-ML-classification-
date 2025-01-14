import json
import joblib
import numpy as np


__model = None
__class_number_to_specie = {}


def load_saved_artifacts():
    print("loading saved artifacts...start")
    global __model, __class_number_to_specie

    with open("./artifacts/num_to_specie_dict.json", "r") as f:
        __class_number_to_specie = json.load(f)

    if __model is None:
        with open("./artifacts/classifier.pkl", "rb") as f:
            __model = joblib.load(f)

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
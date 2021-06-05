import joblib


def load_model():
    return joblib.load('model/model.pkl')


def predict(model, data):
    prediction = model.predict(data)
    print(prediction)
    return prediction[0]

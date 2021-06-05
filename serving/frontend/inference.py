import joblib


def load_model():
    return joblib.load('frontend/model/model.pkl')


def predict_dataframe(model, data):
    predictions = model.predict(data)
    return predictions

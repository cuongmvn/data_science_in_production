from typing import Optional

import numpy as np
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

from inference import load_model, predict

app = FastAPI(
    title='Load diabetes API',
    description='Predict the diabetes progression',
    version='0.1.0'
)
model = load_model()


class DiabetesInfo(BaseModel):
    age: float
    sex: float
    bmi: float
    bp: float
    s1: float
    s2: float
    s3: float
    s4: float
    s5: float
    s6: float
    #fake: Optional[str] = None


#################################################################################################################
#                                                        Routes                                                 #
#################################################################################################################
@app.get('/')
def root():
    response = {'response': 'Hello World'}
    return response


@app.post('/predict')
async def predict_diabetes_progress_1(diabetes_info: DiabetesInfo):
    # age, sex, body_mass_index, average_blood_pressure, total_serum_cholesterol, low_density_lipoproteins,
    # high_density_lipoproteins, total_cholesterol, possibly_log_of_serum_triglycerides_level, blood_sugar_level
    print(diabetes_info.dict())
    model_input_data = pd.DataFrame([diabetes_info.dict()])
    progression = predict(model, model_input_data)
    return progression


@app.post('/predict_old')
async def predict_diabetes_progress_old_1(
        age: float, sex: float, bmi: float, bp: float, s1: float, s2: float, s3: float, s4: float, s5: float,
        s6: float):
    # age, sex, body_mass_index, average_blood_pressure, total_serum_cholesterol, low_density_lipoproteins,
    # high_density_lipoproteins, total_cholesterol, possibly_log_of_serum_triglycerides_level, blood_sugar_level
    # print(age, sex, bmi, bp, s1, s2, s3, s4, s5, s6)
    model_input_data = np.array([age, sex, bmi, bp, s1, s2, s3, s4, s5, s6]).reshape(1, -1)
    progression = predict(model, model_input_data)
    return progression


@app.post('/predict_group')
async def predict_diabetes_progress_2(dataframe):
    pass


if __name__ == '__main__':
    uvicorn.run('main:app', host='127.0.0.1', port=8000, log_level='info', reload=True)

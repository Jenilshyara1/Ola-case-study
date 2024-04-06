from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from src.prediction import Model
from config import Config
import pandas as pd
import json


class Data(BaseModel):
    Education_Level: int
    Income: int
    Joining_Designation: int
    Grade: int
    Total_Business_Value: int
    Quarterly_Rating: int
    Age: int
    Gender: int
    City: str
    Quarterly_Rating_inc: int
    Age_cat: str
    joining_year: int


app = FastAPI()
model = Model(model_path=Config.MODEL_PATH)


@app.post("/prediction")
async def create_item(data: Data):
    x = {
        "Education_Level": data.Education_Level,
        "Income": data.Income,
        "Joining Designation": data.Joining_Designation,
        "Grade": data.Grade,
        "Total Business Value": data.Total_Business_Value,
        "Quarterly Rating": data.Quarterly_Rating,
        "Age": data.Age,
        "Gender": data.Gender,
        "City": data.City,
        "Quarterly Rating inc": data.Quarterly_Rating_inc,
        "Age_cat": data.Age_cat,
        "joining_year": data.joining_year,
    }
    x = pd.DataFrame(x, index=[0])
    output, output_proba = model.predict(x)
    print(output[0], output_proba[0][1])
    result = {"output": str(output[0]), "output_proba": str(max(list(output_proba[0])))}
    return JSONResponse(content=json.dumps(result))


# uvicorn.run(app=app,reload=True)

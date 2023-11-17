from fastapi import FastAPI
from pydantic import BaseModel
from model.model import predict_pipeline
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]

app.add_middleware(
  CORSMiddleware,
  allow_origins=origins,
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
)

class TextIn(BaseModel):
  fixed_acidity: float
  volatile_acidity: float
  citric_acid: float
  residual_sugar: float
  chlorides: float
  free_sulfur_dioxide: float
  total_sulfur_dioxide: float
  density: float
  pH: float
  sulphates: float
  alcohol: float

class PredictionOut(BaseModel):
  quality: int

@app.get("/")
def home():
  return {"health_check": "OK"}

@app.post("/predict", response_model=PredictionOut)
def predict(payload: TextIn):
  print(payload)
  quality = predict_pipeline(payload)
  return {"quality": quality}
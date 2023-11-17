import pickle
import re
from pathlib import Path

BASE_DIR = Path(__file__).resolve(strict=True).parent

with open(f"{BASE_DIR}/voting_clf2.pkl", "rb") as f:
  model = pickle.load(f)

def predict_pipeline(payload):
  temp = [
    payload.fixed_acidity,
    payload.volatile_acidity,
    payload.citric_acid,
    payload.residual_sugar,
    payload.chlorides,
    payload.free_sulfur_dioxide,
    payload.total_sulfur_dioxide,
    payload.density,
    payload.pH,
    payload.sulphates,
    payload.alcohol,
  ]
  pred = model.predict([temp])
  return pred
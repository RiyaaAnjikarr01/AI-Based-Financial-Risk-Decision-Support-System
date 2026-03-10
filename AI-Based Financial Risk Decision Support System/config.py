import os

class Config:
    SECRET_KEY = "financialrisksecret"
    DATA_PATH = os.path.join("data", "financial_data.csv")
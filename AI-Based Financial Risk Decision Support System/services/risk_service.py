from models.risk_model import RiskModel
from models.data_processor import DataProcessor
from config import Config

class RiskService:

    def __init__(self):

        data = DataProcessor.load_dataset(Config.DATA_PATH)
        data = DataProcessor.preprocess_data(data)

        self.model = RiskModel()
        self.model.train(data)

    def get_risk(self, income, debt, credit_score):

        return self.model.predict(income, debt, credit_score)
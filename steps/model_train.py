import logging
import pandas as pd 
from zenml import step 

@step
def train_model(df: pd.DataFrame)-> str:
    """
    Trains model on the ingested data

    Args:
        returns: dummy_model
    """
    logging.info("Training a dummy model")
    return "dummy_model"
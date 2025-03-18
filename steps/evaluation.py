import logging
import pandas as pd 
from zenml import step 



@step
def evaluate_model(model: str)-> None:
    """
    Evaluates the  model on ingest data
    Args:
        model: The input model
    """
    logging.info("Evaluating the model: {model}")
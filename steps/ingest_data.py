import logging
import pandas as pd 
from zenml import step
from materializers.custom_pandas_materializer import CustomPandasMaterializer

class IngestData:
    """
    Ingesting data from the data_path
    """
    def __init__(self, data_path: str):
        """Instiating the method
        Args: data_path
        """
        self.data_path = data_path
    
    def get_data(self) -> pd.DataFrame:
        """
        Ingesting data from the path 
        """
        logging.info(f"Ingesting Data from {self.data_path}")
        return pd.read_csv(self.data_path)
    
@step(output_materializers=CustomPandasMaterializer)
def ingest_df(data_path: str) -> pd.DataFrame:
    """"
    Ingesting the data from the data_path
    Args: 
    data_path: path to the data
    returns: 
    pd.Dataframe: ingest data from the path
    
    """
    try:
        ingest_data_instance = IngestData(data_path)  # Correct variable name
        df = ingest_data_instance.get_data()  # Call get_data on the instance
        return df
    except Exception as e:
        logging.error(f"Error while ingesting data {e}")
        raise e

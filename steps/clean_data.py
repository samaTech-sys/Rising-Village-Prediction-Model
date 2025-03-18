import logging 
import pandas as pd
from zenml import step
from materializers.custom_pandas_materializer import CustomPandasMaterializer

@step(output_materializers=CustomPandasMaterializer)
def clean_df(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean the input dataframe

    Args:
        df (pd.DataFrame): The input dataframe to be cleaned 

    Returns:
        pd.DataFrame: eturns the cleaned dataframe
    """
    df_cleaned = df.dropna()
    logging.info("Testing clean_df step....")
    logging.info(f"Dataframe Shape {df_cleaned.shape}")
    return df_cleaned # Return the DataFrame
    
from raisingVillage import logger
from abc import ABC, abstractmethod
import pandas as pd

# Abstract class for missing value handling (unchanged)
class MissingValueHandlingStrategy(ABC):
    @abstractmethod
    def handle(self, df: pd.DataFrame) -> pd.DataFrame:
        pass

# Concrete Strategy for dropping missing values
class DropMissingValuesStrategy(MissingValueHandlingStrategy):
    def __init__(self, axis=1, thresh=None):
        self.axis = axis
        self.thresh = thresh
        
    def handle(self, df: pd.DataFrame) -> pd.DataFrame:
        logger.info(f"\nDropping missing values with axis={self.axis} and threshold={self.thresh}")
        df_cleaned = df.dropna(axis=self.axis, thresh=self.thresh)
        logger.info("Missing Values dropped!")
        return df_cleaned

# Enhanced Concrete Strategy for filling missing values
class FillMissingValuesStrategy(MissingValueHandlingStrategy):
    def __init__(self, method="mean", fill_value=None, columns=None):
        """
        Initializes FillMissingValueStrategy
        
        Args:
            method (str): 'mean', 'median', 'mode', or 'constant'
            fill_value: Value to use when method='constant'
            columns (list): Specific columns to target (None for all columns)
        """
        self.method = method
        self.fill_value = fill_value
        self.columns = columns  # Changed parameter name to 'columns' for consistency
        
    def handle(self, df: pd.DataFrame) -> pd.DataFrame:
        logger.info(f"\nFilling missing values using method={self.method}")
        df_cleaned = df.copy()
        
        # Determine which columns to process
        columns_to_process = self.columns if self.columns is not None else df_cleaned.columns
        
        for column in columns_to_process:
            if column not in df_cleaned.columns:
                logger.warning(f"Column '{column}' not found in dataframe")
                continue
                
            if self.method == "mean" and pd.api.types.is_numeric_dtype(df_cleaned[column]):
                df_cleaned[column] = df_cleaned[column].fillna(df[column].mean())
            elif self.method == "median" and pd.api.types.is_numeric_dtype(df_cleaned[column]):
                df_cleaned[column] = df_cleaned[column].fillna(df[column].median())
            elif self.method == "mode":
                mode_val = df[column].mode()
                if not mode_val.empty:
                    df_cleaned[column] = df_cleaned[column].fillna(mode_val[0])
                else:
                    logger.warning(f"No mode value found for {column}, filling with 'Unknown'")
                    df_cleaned[column] = df_cleaned[column].fillna("Unknown")
            elif self.method == "constant":
                df_cleaned[column] = df_cleaned[column].fillna(self.fill_value)
            else:
                logger.warning(f"Method '{self.method}' not applicable for column '{column}'. Skipping.")
        
        logger.info("Missing Values Filled!")
        return df_cleaned

# Context class (unchanged)
class MissingValueHandler:
    def __init__(self, strategy: MissingValueHandlingStrategy):
        self._strategy = strategy

    def set_strategy(self, strategy: MissingValueHandlingStrategy):
        self._strategy = strategy
    
    def execute_strategy(self, df: pd.DataFrame) -> pd.DataFrame:
        logger.info("Executing Missing Value handling strategy!")
        return self._strategy.handle(df)

# Example Usage with TV Program Data
if __name__ == "__main__":
    # Load the data 
    df = pd.read_csv(r"C:\Users\USER\Desktop\MLDefaults\Rising-Village-Prediction-Model\artifacts\data_processing\selected_features.csv")
    
    print("Original Data:")
    print(df)
    
    # Strategy 1: Mode imputation for recommendation columns only
    #corrected_columns=['most_recommended_rtv_program', 'least_recommended_rtv_program']
    #strategy1 = FillMissingValuesStrategy(
    #    method="mode",
    #    columns=corrected_columns
    #)
    #handler = MissingValueHandler(strategy1)
    #df_imputed = handler.execute_strategy(df)
    
    #print("\nAfter Mode Imputation for Recommendation Columns:")
    #print(df_imputed)
    
    # Strategy 2: Mean imputation for numeric columns
    #strategy2 = FillMissingValuesStrategy(method="mean")
    #handler.set_strategy(strategy2)
    #df_imputed = handler.execute_strategy(df_imputed)
    
    #print("\nAfter Mean Imputation for Numeric Columns:")
    #print(df_imputed)
    
    # Strategy 3: Drop remaining missing values
    #strategy3 = DropMissingValuesStrategy(axis=0)
    #handler.set_strategy(strategy3)
    #df_final = handler.execute_strategy(df_imputed)
    
    #print("\nFinal Cleaned Data:")
    #print(df_final)
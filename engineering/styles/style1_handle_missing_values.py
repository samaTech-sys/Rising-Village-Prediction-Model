#Design: Strategy Pattern 
from raisingVillage import logger
from abc import ABC, abstractmethod

import pandas as pd 

#Abstract class for missing value handling 
class MissingValueHandlingStrategy(ABC):
    @abstractmethod
    def handle(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Abstract method do handle missing values in the dataframe

        Args:
            df (pd.DataFrame): The dataframe with missing values 

        Returns:
            pd.DataFrame: The dataframe with missing values handled 
            
        """
        pass 
    
#Concrete Strategy for dropping missing values 
class DropMissingValuesStrategy(MissingValueHandlingStrategy):
    def __init__(self, axis=1, thresh=None):
        """
        Initialises DroppingMissingValueStrategy with specific MissingValueHandlingStrategy

        Args:
            axis (int): 0 to drop rows with missing values, 1 to drop columns with missing values 
            thresh (int): The threshold for non-NA values. Minimum number of missing values required to dro a row or a column
        """
        self.axis = axis
        self.thresh = thresh
        
    def handle(self, df: pd.DataFrame) -> pd.DataFrame:
        logger.info("/n Dropping missing values with axis={self.axis} and threshold={self.thresh}")
        df_cleaned = df.dropna(axis=self.axis, thresh=self.thresh)
        logger.info("Missing Values dropped!")
        return df_cleaned

#Concrete Strategy for filling missing values 
class FillMissingValuesStrategy(MissingValueHandlingStrategy):
    def __init__(self, method="mean", fill_value=None):
        """
        Initalises FillMissingValueStrategy with a specific MissingValueHandlingStrategy

        Args:
            method (str, optional): The method to fill missing values ('mean', 'median', 'mode', 'any value')
            fill_value (any): The constant value to fill missing values.
        
        Return:
            None: 
        """
        self.method = method
        self.fill_value= fill_value
        
    def handle(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Fills missing values using specified method or constant 

        Args:
            df (pd.DataFrame): The dataframe with missing values 

        Returns:
            pd.DataFrame: The dataframe will missing values handled
        """
        logger.info("/n Dropping missing values using method={self.method}")
        df_cleaned = df.copy()
        if self.method == "mean":
            numeric_columns = df_cleaned.select_dtypes(include="number").columns
            df_cleaned[numeric_columns] = df_cleaned[numeric_columns].fillna(
                df[numeric_columns].mean()
            )
        elif self.method == "median":
            numeric_columns = df_cleaned.select_dtypes(include="number").columns
            df_cleaned[numeric_columns] = df_cleaned[numeric_columns].fillna(
                df[numeric_columns].median()
            )
        elif self.method == "mode":
            for column in df_cleaned.columns:
                df_cleaned[column].fillna(df[column].mode().iloc[0], inplace=True )
        elif self.method == "constant":
            numeric_columns = df_cleaned.select_dtypes(include="number").columns
            df_cleaned = df_cleaned.fillna(self.fill_value)
        else:
            logger.warning("Unknown Method: '{self.method}'. No such method for filling missing values")
        
        logger.info("Missing Values Filled!")
        return df_cleaned

#Concrete class that uses MissingValueHandlingStrategy
#---------------------------------------------------------------------------------------------#
class MissingValueHandler:
    def __init__(self, strategy: MissingValueHandlingStrategy):
        """
        Initialises the MissingValueHandle with a specific MissingValueHandlingStrategy

        Args:
            strategy (MissingValueHandlingStrategy): The strategy to be used 
        """
        self._strategy = strategy

    def set_strategy(self, strategy: MissingValueHandlingStrategy):
        """
        Sets new strategy for the MissingValueHandler

        Args:
            strategy (MissingValueHandlingStrategy): The strategy to be used. 
        """
        self._strategy = strategy
    
    def execute_strategy(self, df: pd.DataFrame):
        """
        Executes analysis using the current strategy

        Args:
            df (pd.DataFrame): The dataframe to containing missing vaues to be handled
        """
        logger.info("Executing Missing Value handling strategy!")
        self._strategy.handle(df)                        

#Example Usage 
   
if __name__ == "__main__":
    #Example Usage of data analysisr with different strategies
    
    #Load the data 
    #df = pd.read_csv("C:\\Users\\USER\\Desktop\\MLDefaults\\MLOps_Structure\\steps\\extracted_data\\breast_data.csv")
    
    #Initialise the data analysis with a specific strategy
    #missing_values_handler = MissingValueHandler(DropMissingValueStrategy())
    #missing_values_handler.execute_strategy(df)
    
    #Change strategy to statistics and execute
    #missing_values_handler.set_strategy(FillMissingValuesStrategy(method="mean"))
    #missing_values_handler.execute_strategy(df)
    pass

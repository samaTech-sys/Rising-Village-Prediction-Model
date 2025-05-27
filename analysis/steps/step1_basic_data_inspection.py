from abc import ABC, abstractmethod
import pandas as pd

# Abstract base class for Data Inspection Strategies
class DataInspectionStrategy(ABC):
    @abstractmethod
    def inspect(self, df: pd.DataFrame):
        """
        Performs a specific type of data inspection.

        Parameters:
            df (pd.DataFrame): The dataframe being inspected.
            
        Returns: 
            None: This method prints inspection results directly.
        """
        pass

# Concrete Strategy for Data Types Inspection
class DataTypesInspectionStrategy(DataInspectionStrategy):
    def inspect(self, df: pd.DataFrame):
        """
        Inspects and prints data types and non-null counts.

        Parameters:
            df (pd.DataFrame): The dataframe being inspected.
            
        Returns: 
            None: This method prints data types and non-null counts for columns in the dataset.
        """
        print("\nData Types and Non-Null Counts:")
        print(df.info())

# Concrete Strategy for Summary Statistics Inspection
class SummaryStatisticsInspectionStrategy(DataInspectionStrategy):
    def inspect(self, df: pd.DataFrame):
        """
        Inspects and prints summary statistics of the dataset.

        Parameters:
            df (pd.DataFrame): The dataframe being inspected.
            
        Returns: 
            None: This method prints summary statistics of features in the dataset.
        """
        print("\nSummary Statistics (Numerical Features):")
        print(df.describe())
        
        print("\nSummary Statistics (Categorical Features):")
        print(df.describe(include=["object"]))

# Concrete Class that uses DataInspectionStrategy
class DataInspector:
    def __init__(self, strategy: DataInspectionStrategy):
        """
        Initializes Data Inspector with a specific inspection strategy.

        Parameters:
            strategy (DataInspectionStrategy): The strategy to be used.
        """
        self._strategy = strategy

    def set_strategy(self, strategy: DataInspectionStrategy):
        """
        Sets a new strategy for Data Inspector.

        Args:
            strategy (DataInspectionStrategy): The new strategy to be executed.
        """
        self._strategy = strategy
    
    def execute_inspection(self, df: pd.DataFrame):
        """
        Executes the inspection using the current strategy.

        Args:
            df (pd.DataFrame): The dataframe to be inspected.
        """
        self._strategy.inspect(df)                        

#Example Usage 
   
if __name__ == "__main__":
    #Example Usage of data inspector with different strategies
    
    #Load the data 
    #df = pd.read_csv("C:\\Users\\USER\\Desktop\\MLDefaults\\MLOps_Structure\\steps\\extracted_data\\breast_data.csv")
    
    #Initialise the data inspector with a specific strategy
    #inspector = DataInspector(DataTypesInspectionStrategy())
    #inspector.execute_inspection(df)
    
    #Change strategy to statistics and execute
    #inspector.set_strategy(SummaryStatisticsInspectionStrategy())
    #inspector.execute_inspection(df)
    pass
            
            
    

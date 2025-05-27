#Design: Strategy Pattern 
from raisingVillage import logger  
from abc import ABC, abstractmethod

import pandas as pd 
import numpy as np
import seaborn as sns 
import matplotlib.pyplot as plt

#Abstract class for outlier detection strategy 
class OutlierDetectionStrategy(ABC):
    @abstractmethod
    def handle(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Abstract method to detect outliers in the dataframe

        Args:
            df (pd.DataFrame): The dataframe with outliers

        Returns:
            pd.DataFrame: The dataframe with outliers handled
            
        """
        pass 
    
#Concrete Strategy for Z-score based on outlier strategy
class ZScoreOutlierDetection(OutlierDetectionStrategy):
    def __init__(self, threshold=3):
        """
        Initialised the ZScoreOutlierDetection method with OutlierDetectionStrategy

        Args:
            threshold (int): Number of outliers to handle. Defaults to 3.
        """
        self.threshold = threshold
        
def detect_outliers(self, df: pd.DataFrame) -> pd.DataFrame:
    logger.info("/n Detecting outliers using the ZScore method")
    z_scores = np.abs((df - df.mean())/ df.std())
    outliers = z_scores > self.threshold
    logger.info("Outliers detected with z scores: {self.threshold}")
    return outliers

#Concrete Strategy for IQR based Outlier detection 
class IQROutlierDetection(OutlierDetectionStrategy):
    def handle(self, df: pd.DataFrame) -> pd.DataFrame:
        logger.info("/n Detecting outliers using IQR method.")
        Q1 = df.quantile(0.25)
        Q3 = df.quantile(0.75)
        IQR = Q3 - Q1
        outliers = (df < (Q1-1.5 *IQR) | df < (Q3 + 1.5 *IQR)) 
        logger.info("Outliers detected using IQR method")
        return outliers

#Concrete class that uses MissingValueHandlingStrategy
#---------------------------------------------------------------------------------------------#
class OutlierDetector:
    def __init__(self, strategy: OutlierDetectionStrategy):
        """
        Initialises the OutlierDetector with a specific OutlierDetectionStrategy

        Args:
            strategy (OutlierDetectionStrategy): The strategy to be used 
        """
        self._strategy = strategy

    def set_strategy(self, strategy: OutlierDetectionStrategy):
        """
        Sets new strategy for the OutlierDetector

        Args:
            strategy (OutlierDetectionStrategy): The strategy to be used. 
        """
        logger.info("Switching Outlier Detection Strategy")
        self._strategy = strategy
    
    def detect_outliers(self, df: pd.DataFrame):
        logger.info("Executing outlier detection strategy!")
        self._strategy.detect_outliers(df)    
        
    def handle_outliers(self, df: pd.DataFrame, method="remove"):
        outliers = self.detect_outliers(df)
        if method=="remove":
            logger.info("Removing outliers from the dataset")
            df_cleaned = df[(~outliers).all(axis=1)]
        elif  method=="cap":
            logger.info("Capping outliers from the dataset")
            df_cleaned = df.clip(lower=df.quantile(0.01), upper=df.quantile(0.99), axis=1)
        else:
            logger.info("Unknnown method: '{method}'. No outliers.")
            return df                          
        
        logger.info("Outlier handling completed.")
        return df_cleaned
    
    def visualize_outliers(self, df: pd.DataFrame, features=list):
        logger.info("Visualizing Outliers for features: {features}")
        for feature in features:
            plt.figure(figsize=(10,6))
            sns.boxplot(x=df[feature])
            plt.title("Boxplot of {feature}")
            plt.show()
        logger.info("Outlier visualization completed")

#Example Usage 
   
if __name__ == "__main__":
    #Example Usage of data analysisr with different strategies
    
    #Load the data 
    #df = pd.read_csv("C:\\Users\\USER\\Desktop\\MLDefaults\\MLOps_Structure\\steps\\extracted_data\\breast_data.csv")
    
    #Initialise the data analysis with a specific strategy
    #handle_outliers = OutlierDetector(ZScoreOutlierDetection())
    #handle_outliers.execute_strategy(df)
    
    #Change strategy to statistics and execute
    #missing_values_handler.set_strategy(FillMissingValueStrategy())
    #missing_values_handler.execute_strategy(df)
    pass

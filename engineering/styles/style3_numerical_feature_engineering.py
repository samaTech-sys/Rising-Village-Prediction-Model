#Design: Strategy Pattern 
from raisingVillage import logger
from abc import ABC, abstractmethod

import pandas as pd 
import numpy as np
from sklearn.preprocessing import MinMaxScaler, StandardScaler

#Abstract class for feature engineering strategy
#------------------------------------------------------------------------------------------#
#This class defines a common interface for different feature engineering strategies
#The subclasses must implement apply_transformation method.
class NumericalFeatureEngineeringStrategy(ABC):
    @abstractmethod
    def apply_transformation(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Abstract method to apply feature engineering transformation

        Args:
            df (pd.DataFrame): The dataframe with features to be engineered

        Returns:
            pd.DataFrame: The dataframe containing features to be engineered
            
        """
        pass 
    
#Concrete Strategy for Log Transformation
#------------------------------------------------------------------------
#This strategy applies a logarithimic transormation to skewed features 
class LogTransformation(NumericalFeatureEngineeringStrategy):
    def __init__(self, features):
        """
        Initialises LogTransformation with specific FeatureEngineeringStrategy

        Args:
            # features (list): The list of features on which to apply Log transformation 
            
        """
        self.features = features
        
def apply_transformation(self, df: pd.DataFrame) -> pd.DataFrame:
    """
    Applies log transformation to specified features in the dataframe.

    Args:
        df (pd.DataFrame): The Dataframe containing features 

    Returns:
        pd.DataFrame: The dataframe with log-transformed features. 
        
    """
    logger.info("/n Applying log transformation to features: {self.features}")
    df_transformed = df.copy()
    for feature in self.features:
        df_transformed[feature] =np.log1p(
            df[feature]
        ) #log1p handles log(0) by calculating log(1+x) to reduce skewedness
        logger.info("Log Transformation completed!")
        return df_transformed


#Concrete Strategy for Standard Scaling
#------------------------------------------------------------------------
#This strategy applies standard scaling (z-score normalization) 
class StandardScaling(NumericalFeatureEngineeringStrategy):
    def __init__(self, features):
        """
        Initalises StandardScalling with a specific FeatureEngineeringStrategy

        Args:
            features (list): The list of features to apply standard scalling
        
        """
        self.features = features
        self.scaler = StandardScaler()
        
def apply_transformation(self, df: pd.DataFrame) -> pd.DataFrame:
    """
    Applies Standard Scaling to Specified features in the dataframe 

    Args:
        df (pd.DataFrame): The dataframe with features on which standard scaling is to be applied.

    Returns:
        pd.DataFrame: The dataframe with standardized features
    """
    logger.info("/n Applying standard scaling to features: {self.method}")
    df_transformed = df.copy()
    df_transformed[self.features] = self.scaler.fit_transformation(df[self.features])
    logger.info("Missing Values Filled!")
    return df_transformed

#Concrete Strategy for Min-Max Scaling
#------------------------------------------------------------------------
#This strategy applies standard Min-Max Scalling to features,  
class MinMaxScaling(NumericalFeatureEngineeringStrategy):
    def __init__(self, features, feature_range=(0,1)):
        """
        Initalises MinMaxScaling with a specific FeatureEngineeringStrategy

        Args:
            features (list): The list of features to apply the Min-Max Scaling
            feature_range(tuple): The target range for scaling defined
        
        """
        self.features = features
        self.scaler = MinMaxScaler(feature_range=feature_range)
        
def apply_transformation(self, df: pd.DataFrame) -> pd.DataFrame:
    """
    Applies Min-Max Scaler to Specified features in the dataframe 

    Args:
        df (pd.DataFrame): The dataframe with features on which Min-Max Scaler is to be applied.

    Returns:
        pd.DataFrame: The dataframe with scaled features
    """
    logger.info("/n Applying Min-Max to features: {self.features}")
    df_transformed = df.copy()
    df_transformed[self.features] = self.scaler.fit_transformation(df[self.features])
    logger.info("Min-Max Scaling Completed!")
    return df_transformed

#Concrete class that uses MissingValueHandlingStrategy
#---------------------------------------------------------------------------------------------#
class FeatureEngineering:
    def __init__(self, strategy: NumericalFeatureEngineeringStrategy):
        """
        Initialises FeatureEngineering with a specific NumericalFeatureEngineeringStrategy

        Args:
            strategy (FeatureEngineeringStrategy): The strategy to be used 
        """
        self._strategy = strategy

    def set_strategy(self, strategy: NumericalFeatureEngineeringStrategy):
        """
        Sets new strategy for the FeatureEngineering

        Args:
            strategy (FeatureEngineeringStrategy): The strategy to be used. 
        """
        logger.info("Switching Feature Engineering Strategy")
        self._strategy = strategy
    
    def apply_feature_engineering_strategy(self, df: pd.DataFrame):
        """
        Executes analysis using the current strategy

        Args:
            df (pd.DataFrame): The dataframe to containing features to be engineered
        """
        logger.info("Executing FeatureEngineering transformation strategy!")
        self._strategy.apply_transformation(df)                        

#Example Usage 
   
if __name__ == "__main__":
    #Example Usage of feature Engineering with different strategies
    
    #Load the data 
    #df = pd.read_csv("C:\\Users\\USER\\Desktop\\MLDefaults\\MLOps_Structure\\steps\\extracted_data\\breast_data.csv")
    
    #Log Transformation Example
    #log_transformer = FeatureEngineering(LogTransformation(features=["area_mean", "area_se"]))
    #df_log_transformed = log_transformer.apply_feature_engineering_strategy(df)
    
    #Standard Scaler Example 
    #standard_scaler = FeatureEngineering(StandardScaling(features=["area_mean", "area_se"]))
    #df_standard_scaled = standard_scaler.apply_feature_engineering_strategy(df)
    
    #MinMax Scaling Example
    #min_max_scaler = FeatureEngineering(MinMaxScaling(features=["area_mean", "area_se"]))
    #df_min_max_scaled = min_max_scaler.apply_feature_engineering_strategy(df)
   
    pass

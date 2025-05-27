#Design: Strategy Pattern 
from raisingVillage import logger
from abc import ABC, abstractmethod

import pandas as pd 
import numpy as np
from sklearn.preprocessing import OneHotEncoder

#Abstract class for feature engineering strategy
#------------------------------------------------------------------------------------------#
#This class defines a common interface for different feature engineering strategies
#The subclasses must implement apply_transformation method.
class CategoricalFeatureEngineeringStrategy(ABC):
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

#Concrete Strategy for OneHotEncoding
#------------------------------------------------------------------------
#This strategy applies standard Min-Max Scalling to features,  
class OneHotEncoding(CategoricalFeatureEngineeringStrategy):
    def __init__(self, features):
        """
        Initalises OneHotEncoding with a specific FeatureEngineeringStrategy

        Args:
            features (list): The list of features to apply the Min-Max Scaling
        
        """
        self.features = features
        self.encoder = OneHotEncoder(sparse=False, drop="first")
        
def apply_transformation(self, df: pd.DataFrame) -> pd.DataFrame:
    """
    Applies OnehotEncoder to Specified features in the dataframe 

    Args:
        df (pd.DataFrame): The dataframe with features on which Min-Max Scaler is to be applied.

    Returns:
        pd.DataFrame: The dataframe with scaled features
    """
    logger.info("/n Applying Min-Max to features: {self.features}")
    df_transformed = df.copy()
    encoded_df = pd.DataFrame(
        self.encoder.fit_transform(df[self.features]), 
        columns=self.encoder.get_feature_names_out(self.features)
    )
    df_transformed = df_transformed.drop(columns=self.features)
    df_transformed = pd.concat([df_transformed, encoded_df], )
    logger.info("One-Hot Encoding Completed!")
    return df_transformed

#Concrete class that uses MissingValueHandlingStrategy
#---------------------------------------------------------------------------------------------#
class FeatureEngineering:
    def __init__(self, strategy: CategoricalFeatureEngineeringStrategy):
        """
        Initialises FeatureEngineering with a specific FeatureEngineeringStrategy

        Args:
            strategy (FeatureEngineeringStrategy): The strategy to be used 
        """
        self._strategy = strategy

    def set_strategy(self, strategy: CategoricalFeatureEngineeringStrategy):
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
        logger.info("Executing CategoricalFeatureEngineering transformation strategy!")
        self._strategy.apply_transformation(df)                        

#Example Usage 
   
if __name__ == "__main__":
    #Example Usage of feature Engineering with different strategies
    
    #Load the data 
    #df = pd.read_csv("C:\\Users\\USER\\Desktop\\MLDefaults\\MLOps_Structure\\steps\\extracted_data\\breast_data.csv")
    
    #OneHotEncoding Example
    #one_hot_encoder = FeatureEngineering(OneHotEncoding(features=["area_mean", "area_se"]))
    #df_one_hot_encoded = one_hot_encoder.apply_feature_engineering_strategy(df)
    
    pass

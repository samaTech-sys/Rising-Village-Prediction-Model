#Design Used: Strategy Design Pattern 
from abc import ABC, abstractmethod

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt 

#Abstract Base class for Bivariate Analysis Strategy
#-------------------------------------------------------------------------------------------------#
#This class defines a common interface for biivariate analysis strategies
#Subclasses must implement the analyze method.
class BivariateAnalysisStrategy(ABC):
    @abstractmethod
    def analyse(self, df: pd.DataFrame, feature1: str, feature2: str ):
        """
        Performs biivarite analysis on two specified features of the dataframe
        
        Args:
            df (pd.DataFrame): The dataframe containing the data
            feature1 (str): The name of the feature1 or column1 to be analyzed 
            feature2 (str): The name of the feature2 or column2 to be analyzed 
            
        Return: 
           None: This method visualises the distribution of the two specified features
        """
        pass
    
# Concrete strategy for Numerical Features 
#-------------------------------------------------------------------------------------------------#
#This strategy analyses numerical features by plotting their distribution 
class NumericalBivariateAnalysis(BivariateAnalysisStrategy):
    def  analyse(self, df: pd.DataFrame,  feature1: str, feature2: str):
        """
        Plots the relationship between two numerical features  using scatter plot 
        
        Args:
            df (pd.DataFrame): The dataframe containing the data
            feature (str): The feature to be analysed 
            
        Return: 
           None: Displays scatter plot showing relationship between two specified features. 
           
        """
        plt.tight_layout()
        sns.scatterplot(x=feature1, y=feature2, data=df)
        plt.title(f"{feature1} vs {feature2}")
        plt.xlabel(feature1)
        plt.ylabel(feature2)
        plt.show()
    
#Concrete strategy for categorical feature vs Numerical Analysis 
#----------------------------------------------------------------------------------------------#
#This strategy analyses a relationship between a categorical feature and a numerical feature using a box plot
class CategoricalVsBivariateAnalysis(BivariateAnalysisStrategy):
    def analyse(self, df: pd.DataFrame, feature1: str, feature2: str):
        """
        plots the realtionship between a categorical feature and a numerical feature using boxplot 

        Args:
            df (pd.DataFrame): The dataframe containing data
            feature1 (str): The feature1 to be analyzed(categorical)
            feature2 (str): The feature2 to be analyzed(numerical)
        
        Return:
           None: Display a boxplot showing the relationship betwen the categorical and numerical feature
        """
        plt.tight_layout()
        sns.boxplot(x=feature1, y=feature2, data=df)
        plt.title(f"{feature1} vs {feature2}")
        plt.xlabel(feature1)
        plt.ylabel(feature2)
        plt.xticks(rotation=45)
        plt.show()
    
#Concrete class that uses UnivariateAnalysisStrategy
#---------------------------------------------------------------------------------------------#
class BivariateAnalyzer:
    def __init__(self, strategy: BivariateAnalysisStrategy):
        """
        Initialises Bivariate Analyzer with specific analysis strategy

        Args:
            strategy (BivariateAnalysisStrategy): The strategy to be used 
        """
        self._strategy = strategy

    def set_strategy(self, strategy: BivariateAnalysisStrategy):
        """
        Sets new strategy for the Bivariate analyzer 

        Args:
            strategy (BivariateAnalysisStrategy): The strategy to be analysed. 
        """
       
        self._strategy = strategy
    
    def execute_analysis(self, df: pd.DataFrame, feature1: str, feature2: str):
        """
        Executes analysis using the current strategy

        Args:
            df (pd.DataFrame): The dataframe to containing feature
            feature1 (str): feature1 to be analysed(categorical)
            feature2 (str): feature2 to be analysed(numerical)
        """
        self._strategy.analyse(df, feature1, feature2)                        

#Example Usage 
   
if __name__ == "__main__":
    #Example Usage of data analysisr with different strategies
    
    #Load the data 
    #df = pd.read_csv("C:\\Users\\USER\\Desktop\\MLDefaults\\MLOps_Structure\\steps\\extracted_data\\breast_data.csv")
    
    #Initialise the data analysis with a specific strategy
    #bivariate_analyzer = BivariateAnalyzer(NumericalBivariateAnalysis())
    #bivariate_analyzer.execute_analysis(df, "area_mean", "area_se")
    
    #Change strategy to statistics and execute
    #bivariate_analyzer.set_strategy(CategoricalVsBivariateAnalysis())
    #bivariate_analyzer.execute_analysis(df, "diagnosis", "area_mean")
    pass

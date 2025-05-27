#Design Used: Strategy Design Pattern 
from abc import ABC, abstractmethod

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt 

#Abstract base class for Univariate Analysis Strategy
#-------------------------------------------------------------------------------------------------------------------------------#
#This class defines a common interface for univariate analysis strategies
#Subclasses must implement the analyze method.
class UnivariateAnalysisStrategy(ABC):
    @abstractmethod
    def analyse(self, df: pd.DataFrame, feature: str):
        """
        Performs univarite analysis on specific feature of the dataframe
        
        Args:
            df (pd.DataFrame): The dataframe containing the data
            feature (str): The name of the feature or column to be analyzed 
            
        Return: 
           None: This method visualises the distribution of the feature
        """
        pass
    
# Concrete strategy for Numerical Features 
#-------------------------------------------------------------------------------------------------#
#This strategy analyses numerical features by plotting their distribution 
class NumericalUnivariateAnalysis(UnivariateAnalysisStrategy):
    def  analyse(self, df: pd.DataFrame,  feature: str):
        """
        Plots distribution of the numerical feature using histogram and kde

        Args:
            df (pd.DataFrame): The dataframe containing the data
            feature (str): The feature to be analysed 
            
        Return: 
           None: Displays histogram with a kde plot. 
           
        """
        plt.tight_layout()
        sns.histplot(df[feature], kde=True, bins=30)
        plt.title(f"Distribution of {feature}")
        plt.xlabel(feature)
        plt.ylabel("Frequqncy")
        plt.show()
    
#Concrete strategy for categorical features 
#----------------------------------------------------------------------------------------------#
#This strategy analyses categorical features by plotting their frequency distribution
class CategoricalUnivariateAnalysis(UnivariateAnalysisStrategy):
    def analyse(self, df: pd.DataFrame, feature: str):
        """
        plots the distribution of categorical feature using a bar plot

        Args:
            df (pd.DataFrame): The dataframe containing data
            feature (str): The feature to be analyzed
        
        Return:
           None: Display the bargraph showing  frequency distribution of a give feature
        """
        plt.tight_layout()
        sns.countplot(x=feature, data=df, palette="muted")
        plt.title(f"Distribution of {feature}")
        plt.xlabel(feature)
        plt.ylabel("Count")
        plt.xticks(rotation=45)
        plt.show()
    
#Concrete class that uses UnivariateAnalysisStrategy
#---------------------------------------------------------------------------------------------#
class UnivariateAnalyzer:
    def __init__(self, strategy: UnivariateAnalysisStrategy):
        """
        Initialises Univariate Analyzer with specific analysis strategy

        Args:
            strategy (UnivariateAnalysisStrategy): The strategy to be used 
        """
        self._strategy = strategy

    def set_strategy(self, strategy: UnivariateAnalysisStrategy):
        """
        Sets new strategy for the Univariate analyzer 

        Args:
            strategy (UnivariateAnalysisStrategy): The strategy to be analysed. 
        """
       
        self._strategy = strategy
    
    def execute_analysis(self, df: pd.DataFrame, feature: str):
        """
        Executes analysis using the current strategy

        Args:
            df (pd.DataFrame): The dataframe to containing feature
            feature (str): feature to be analysed
        """
        self._strategy.analyse(df, feature)                        

#Example Usage 
   
if __name__ == "__main__":
    #Example Usage of data analysisr with different strategies
    
    #Load the data 
    #df = pd.read_csv("C:\\Users\\USER\\Desktop\\MLDefaults\\MLOps_Structure\\steps\\extracted_data\\breast_data.csv")
    
    #Initialise the data analysis with a specific strategy
    #univariate_analyzer = UnivariateAnalyzer(NumericalUnivariateAnalysis())
    #univariate_analyzer.execute_analysis(df, "area_mean")
    
    #Initialise the data analysis with a specific strategy
    #univariate_analyzer = UnivariateAnalyzer(NumericalUnivariateAnalysis())
    #univariate_analyzer.execute_analysis(df, "area_se")
    
    #Change strategy to statistics and execute
    #univariate_analyzer.set_strategy(CategoricalUnivariateAnalysis())
    #univariate_analyzer.execute_analysis(df, "diagnosis")
    pass

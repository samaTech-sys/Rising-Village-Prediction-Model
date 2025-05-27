#Design: Template Pattern 
from abc import ABC, abstractmethod

import matplotlib.pyplot as plt 
import pandas as pd 
import seaborn as sns 


#Abstract class for multivariate Analysis 
#------------------------------------------------------------------------------------#
#This class defines a template for multivariate Analysis 
#Subclasses can override specific steps like heatmap 
class MultivariateAnalysisTemplate(ABC):
    #The template method defining skeleton of the dinning experience
    def analyse(self, df: pd.DataFrame):
        """
        Perform a  comprehennsive multivariate Analysis using heatmap and pairplot

        Args:
            df (pd.DataFrame): The dataframe containg data to be analyzed
        
        Return: 
           None: This method orchestrates multicvaraiate analysis 
           
        """
        self.generate_correlation_heatmap(df)
        self.generate_pairplot(df)
        
    #Abstract method to serve each course(to be implemented)
    @abstractmethod
    def generate_correlation_heatmap(self, df: pd.DataFrame):
        """
        Generate and display heatmap between different selected features

        Args:
            df (pd.DataFrame): Dataframe containg data to be analysed 
        
        Return: 
           None: The method generates and displays correlation heatmap. 
           
        """ 
        pass
    
    @abstractmethod
    def generate_pairplot(self, df: pd.DataFrame):
        """
        Displays pair plot of selected features 

        Args:
            df (pd.DataFrame): The dataframe with data to be analysed
            
        Return: 
            None: This method should generate and display pair plot for the selcted features
            
        """
        pass
    
#Step 2: A concrete class that implements multvariate Analysis 
#------------------------------------------------------------------------------------------------------------#
#This class implements methods that generate a correlation heatmap 
class SimpleMultivariateAnalysis(MultivariateAnalysisTemplate):
    def generate_correlation_heatmap(self, df: pd.DataFrame):
        """
        Generates and displays a correlation heatmap for numeric features 
        Args:
            df (pd.DataFrame): The dataframe containg data to be analysed 
        
        Return: 
           None: Displays heatmap showing correlation between numeric features
           
        """
        plt.tight_layout()
        sns.heatmap(df.corr(), annot=True, fmt='.2f', cmap='coolwarm', linewidths=0.5)
        plt.title("Correlation heatmap")
        plt.show()
        
        
    def generate_pairplot(self, df: pd.DataFrame):
        """
        Generates and displays a pairplot for selceted features

        Args:
            df (pd.DataFrame): The dataframe with data to be analysed 
        
        Return: 
           None: Display pairplot showing selected features
        """
        
        sns.pairplot(df)
        plt.suptitle("Pair plot for seleted features", y=1.02)
        plt.show()
        
#Example Usage
if __name__ == "__main__":
    #Example usage of SimpleMultivariateAnalysis class
    
    #Load the data 
    #df = pd.read_csv("C:\\Users\\USER\\Desktop\\MLDefaults\\MLOps_Structure\\steps\\extracted_data\\breast_data.csv")
    
    #Perform Multivariate Analysis
    #multivariate_analyzer  = SimpleMultivariateAnalysis()
    #selected_features = df[["area_mean", "area_se","radius_mean"]]
    #select important features for analysis
    #multivariate_analyzer.analyse(selected_features)
    pass
    
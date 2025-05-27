from abc import ABC, abstractmethod

import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as  sns 

#Abstract Base Class for Missing Value analysis 
#------------------------------------------------------------------------------------------#
#This class defines a template for missing value analysis 
#The subclasses must implement the methods to identify and visualise 
class MissingValuesTemplate(ABC):
    def analyse(self, df: pd.DataFrame):
        """
        Performs a complete missing values analysis by identifying and Visualising 

        Args:
            df (pd.DataFrame): The dataframe to be analyzed
            
        Returns: 
           None: This dataframe performs the analysis and visualises missing values
            
        """
        self.identify_missing_values(df)
        self.visualize_missing_values(df)
        
    @abstractmethod
    def identify_missing_values(self, df: pd.DataFrame):
        """
        Identifys missing values in the dataframe

        Args:
            df (pd.DataFrame): The Dataframe to be analyzed
            
        Return: 
            None: This should print the  output of the missing values 
             
        """
        pass
    
    @abstractmethod
    def visualize_missing_values(self, df: pd.DataFrame):
        """
        Visualise  missing values in the dataframe

        Args:
            df (pd.DataFrame): The Dataframe to be analyzed
            
        Return: 
            None: This should print the  output of the missing values 
             
        """
        pass
    
#Step 2: Concrete class for missing value Identification 
#--------------------------------------------------------------------------------------------#
#This class implements methods to identify and viualize missing values 
class SimpleMissingValueAnalysis(MissingValuesTemplate):
    def identify_missing_values(self, df: pd.DataFrame):
        """
        Prints the count missing values for each column of the dataframe

        Args:
            df (pd.DataFrame): The dataframe to be analysed 
            
        Return: 
            None: Prints the missing value count to the console. 
        """
        print("\n Missing Values Count by Column")
        missing_values = df.isnull().sum()
        print(missing_values[missing_values > 0])
        
    def visualize_missing_values(self, df: pd.DataFrame):
        """
        Creates a heatmap to visualise missing values in the dataframe

        Args:
            df (pd.DataFrame): The dataframe to be analysed 
            
        Return: 
            None: Displays a heatmap of mising values. 
        """
        print("\n Visualising the missing Values")
        plt.tight_layout()
        sns.heatmap(df.isna(), cbar=False, cmap="viridis")
        plt.title("MIssing Values Heatmap")
        plt.show()
        
#Example Usage 
if __name__ == "__main__":
    #Example of using MissingValueAnalysis class
    # Load the data
    #df = pd.read_csv("C:\\Users\\USER\\Desktop\\MLDefaults\\MLOps_Structure\\steps\\extracted_data\\breast_data.csv")
    #Perform missing values analysis 
    #missing_value_analyzer = SimpleMissingValueAnalysis()
    #missing_value_analyzer.analyze(df)
    pass 
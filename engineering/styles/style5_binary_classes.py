from abc import ABC, abstractmethod
import pandas as pd
from raisingVillage import logger

# Abstract Strategy for Target Binarization
class TargetBinarizationStrategy(ABC):
    @abstractmethod
    def binarize(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Abstract method to convert continuous target to binary classes.
        Args:
            df (pd.DataFrame): Input dataframe with continuous target
        Returns:
            pd.DataFrame: Dataframe with binary target column
        """
        pass

# Concrete Strategy: Median Split
class MedianBinarizationStrategy(TargetBinarizationStrategy):
    def binarize(self, df: pd.DataFrame) -> pd.DataFrame:
        # Use the actual column name from your CSV file
        income_column = "HH Income + Production/Day (USD)"  # Change this to match your actual column name
        median_income = df[income_column].median()
        df['income_binary'] = (df[income_column] > median_income).astype(int)
        logger.info(f"Binarized target using median split (threshold={median_income:.2f})")
        return df

# Concrete Strategy: Threshold Split
class ThresholdBinarizationStrategy(TargetBinarizationStrategy):
    def __init__(self, threshold: float):
        self.threshold = threshold

    def binarize(self, df: pd.DataFrame) -> pd.DataFrame:
        income_column = "HH Income + Production/Day (USD)"  # Change this to match your actual column name
        df['income_binary'] = (df[income_column] > self.threshold).astype(int)
        logger.info(f"Binarized target using fixed threshold (threshold={self.threshold})")
        return df

# Concrete Strategy: Percentile Split
class PercentileBinarizationStrategy(TargetBinarizationStrategy):
    def __init__(self, percentile: float):
        self.percentile = percentile  # e.g., 0.6 for top 40%

    def binarize(self, df: pd.DataFrame) -> pd.DataFrame:
        income_column = "HH Income + Production/Day (USD)"  # Change this to match your actual column name
        threshold = df[income_column].quantile(self.percentile)
        df['income_binary'] = (df[income_column] > threshold).astype(int)
        logger.info(f"Binarized target using percentile split (threshold={threshold:.2f}, percentile={self.percentile})")
        return df

class TargetBinarizer:
    def __init__(self, strategy: TargetBinarizationStrategy):
        self._strategy = strategy

    def set_strategy(self, strategy: TargetBinarizationStrategy):
        """Dynamically change the binarization strategy."""
        self._strategy = strategy

    def execute(self, df: pd.DataFrame) -> pd.DataFrame:
        """Apply the selected binarization strategy."""
        logger.info("Executing target binarization...")
        return self._strategy.binarize(df)

if __name__ == "__main__":
    # Example Usage of data analysis with different strategies
    
    # Load the data 
    #df = pd.read_csv(r"C:\Users\USER\Desktop\MLDefaults\Rising-Village-Prediction-Model\artifacts\data_processing\selected_features.csv")
    
    # Print column names to verify the correct income column name
    #print("DataFrame columns:", df.columns.tolist())
    
    # 1. Test Median Strategy
    #median_binarizer = TargetBinarizer(MedianBinarizationStrategy())
    #df_median = median_binarizer.execute(df.copy())
    #print("\nMedian Binarization Results:")
    #print(df_median[["HH Income + Production/Day (USD)", 'income_binary']].head())
    #print("\n" + "="*50 + "\n")
    
    # 3. Test Threshold Strategy ($3.0 threshold)
    #threshold_binarizer = TargetBinarizer(ThresholdBinarizationStrategy(threshold=3.0))
    #df_threshold = threshold_binarizer.execute(df.copy())
    #print("Threshold Binarization Results (Threshold = 3.0):")
    #print(df_threshold[['HH Income + Production/Day (USD)', 'income_binary']])
    #print("\n" + "="*50 + "\n")

    # 4. Test Percentile Strategy (Top 30%)
    #percentile_binarizer = TargetBinarizer(PercentileBinarizationStrategy(percentile=0.7))
    #df_percentile = percentile_binarizer.execute(df.copy())
    #print("Percentile Binarization Results (Top 30% as High Income):")
    #print(df_percentile[['HH Income + Production/Day (USD)', 'income_binary']])
    #print("\n" + "="*50 + "\n")
    pass
    
    # 5. Verify Class Balance
    #for name, result in [('Median', df_median), 
    #                     ('Threshold', df_threshold), 
    #                     ('Percentile', df_percentile)]:
     #   class_ratio = result['income_binary'].value_counts(normalize=True)
     #   print(f"{name} Strategy Class Distribution:")
     #   print(f"Low Income (0): {class_ratio.get(0, 0):.1%}")
     #   print(f"High Income (1): {class_ratio.get(1, 0):.1%}\n")

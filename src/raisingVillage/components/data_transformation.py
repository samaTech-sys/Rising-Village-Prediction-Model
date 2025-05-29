import pandas as pd
import os
from pathlib import Path
from raisingVillage import logger
from raisingVillage.entity.entity_config import DataTransformationConfig

class DataTransformation:
    def __init__(self, config:DataTransformationConfig):
        self.config = config
        self.df = pd.read_csv(self.config.data_path)
        self.processed_df = None
    
    def create_binary_classes(self, df: pd.DataFrame, target_col: str = "HH Income + Production/Day (USD)") -> pd.DataFrame:
        """
        Convert continuous target to binary classes using median split
        Args:
            df: Input DataFrame
            target_col: Name of column to binarize
        Returns:
            DataFrame with new 'target_binary' column
        """
        median_val = df[target_col].median()
        df['target_binary'] = (df[target_col] > median_val).astype(int)
        logger.info(f"Created binary classes (median threshold: {median_val:.2f})")
        return df
    
    def fill_missing_with_mode(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Fill all missing values using mode (most frequent value) for each column
        Args:
            df: Input DataFrame with missing values
        Returns:
            DataFrame with missing values filled
        """
        for col in df.columns:
            if df[col].isnull().any():
                mode_val = df[col].mode()[0] if not df[col].mode().empty else "Unknown"
                df[col] = df[col].fillna(mode_val)
                logger.info(f"Filled missing values in {col} with mode: {mode_val}")
        return df
    
    def process_and_store_data(self) -> None:
        """
        Execute full processing pipeline and store results
        Args:
            df: Raw input DataFrame
        """
        df=self.df.copy() #work on a copy of dataframe
        df = self.create_binary_classes(df) # Step 1: Binarize target
        df = self.fill_missing_with_mode(df)  # Step 2: Handle missing values
        self.processed_df = df # Store processed data
        
        # Save to artifacts
        os.makedirs(self.config.processed_data_dir, exist_ok=True)
        save_path = Path(self.config.processed_data_dir) / "processed_df.csv"
        df.to_csv(save_path, index=False)
        logger.info(f"Processed data stored at: {save_path}")
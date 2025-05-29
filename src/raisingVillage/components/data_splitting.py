import pandas as pd
import os
from pathlib import Path
from raisingVillage import logger
from sklearn.model_selection import train_test_split
from raisingVillage.entity.entity_config import DataSplittingConfig


class DataSplitting: 
    def __init__(self, config: DataSplittingConfig):
        self.config = config
        #You can add all the different transformation techniques needed before splitting the data. 
        
    def train_test_splitting(self):
        data = pd.read_csv(self.config.processed_data_file)
    #Split the data into training and test datasets 
        train, test = train_test_split(
            data,
            test_size=self.config.test_size,
            random_state=self.config.random_state 
            )
        train.to_csv(os.path.join(self.config.root_dir, "train_set.csv"), index=False)
        test.to_csv(os.path.join(self.config.root_dir, "test_set.csv"), index=False)
        
        logger.info("Splitted data into train and test sets")
        logger.info(f"Train set saved to {self.config.train_set_path}")
        logger.info(f"Test set saved to {self.config.test_set_path}")

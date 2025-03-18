from pipelines.training_pipeline import train_pipeline
import os

if __name__ == "__main__":
    #define the data path
    data_path = r"C:/Users/USER/Desktop/interview_package/data/interview_dataset.csv"
    # Run the pipeline
    train_pipeline(data_path=data_path)
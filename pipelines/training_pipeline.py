from zenml import pipeline
from steps.ingest_data import ingest_df
from steps.clean_data import clean_df
from steps.model_train import train_model
from steps.evaluation import evaluate_model

@pipeline
def train_pipeline(data_path: str):
    #Step 1: Ingest Data
    df = ingest_df(data_path)
    #Step 2: Clean Data
    df_cleaned  = clean_df(df)
    #Step 3: Train Model
    model = train_model(df_cleaned)
    #Step 4: Evaluate Model
    evaluate_model(model)
    
    
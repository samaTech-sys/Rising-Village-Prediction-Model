import pandas as pd

def load_selected_data():
    data_path = (r"C:\Users\USER\Desktop\MLDefaults\Rising-Village-Prediction-Model\artifacts\data_ingestion\interview_dataset.csv")
    df = pd.read_csv(data_path)
    
    selected_columns = [
        'HH Income + Production/Day (USD)',
        'most_recommend_rtv_program',
        'least_recommend_rtv_program',
        'most_recommend_rtv_program_reason',
        'least_recommend_rtv_program_reason'
    ]
    return df.loc[:, selected_columns].copy(deep=True)

# Create the variable when module is imported
selected_data = load_selected_data()

# Explicitly expose what should be available when importing from steps
__all__ = ['selected_data']
import pandas as pd 
import os 
import joblib
from raisingVillage import logger
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
import difflib
from raisingVillage.entity.entity_config import ModelTrainingConfig

class ModelTrainer:
    def __init__(self, config: ModelTrainingConfig):
        self.config = config
    
    def train(self):
        try:
            # 1. Load data
            train_data = pd.read_csv(self.config.train_set_path)
            test_data = pd.read_csv(self.config.test_set_path)
            
            # 2. Clean column names
            train_data.columns = train_data.columns.str.strip().str.replace(' ', '_')
            test_data.columns = test_data.columns.str.strip().str.replace(' ', '_')

            # 3. Set target column
            target_column = 'target_binary'
            
            # 4. Verify target exists
            if target_column not in train_data.columns:
                raise ValueError(
                    f"Target column '{target_column}' not found. Available columns: {list(train_data.columns)}"
                )

            # 5. Prepare features and target
            train_x = train_data.drop(columns=[target_column, 'HH_Income_+_Production/Day_(USD)'])
            test_x = test_data.drop(columns=[target_column, 'HH_Income_+_Production/Day_(USD)'])
            train_y = train_data[target_column]
            test_y = test_data[target_column]

            # 6. Fix and validate Tfidf parameters
            tfidf_params = self._validate_tfidf_params(self.config.tfidf_params)

            # 7. Create preprocessing pipeline
            preprocessor = ColumnTransformer(
                transformers=[
                    ('text1', TfidfVectorizer(**tfidf_params), 'most_recommend_rtv_program_reason'),
                    ('text2', TfidfVectorizer(**tfidf_params), 'least_recommend_rtv_program_reason'),
                    ('num', StandardScaler(), ['most_recommend_rtv_program', 'least_recommend_rtv_program'])
                ],
                remainder='passthrough'
            )

            # 8. Create and train pipeline
            pipeline = Pipeline([
                ('preprocessor', preprocessor),
                ('classifier', GradientBoostingClassifier(**self.config.gb_params))
            ])
            
            pipeline.fit(train_x, train_y)
            
            # 9. Save model
            os.makedirs(self.config.root_dir, exist_ok=True)
            joblib.dump(pipeline, os.path.join(self.config.root_dir, self.config.model_name))
            
            return pipeline

        except Exception as e:
            print(f"Error during training: {str(e)}")
            raise

    def _validate_tfidf_params(self, params):
        """Ensure TfidfVectorizer parameters are properly formatted"""
        validated_params = params.copy()
        
        # Convert ngram_range to tuple if needed
        if 'ngram_range' in validated_params:
            if isinstance(validated_params['ngram_range'], str):
                # Convert from string "(1, 2)" to tuple (1, 2)
                validated_params['ngram_range'] = eval(validated_params['ngram_range'])
            elif not isinstance(validated_params['ngram_range'], tuple):
                raise ValueError("ngram_range must be a tuple, e.g. (1, 2)")
        
        return validated_params
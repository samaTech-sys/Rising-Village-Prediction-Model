import pandas as pd
from zenml.materializers.base_materializer import BaseMaterializer

class CustomPandasMaterializer(BaseMaterializer):
    ASSOCIATED_TYPES = (pd.DataFrame,)

    def handle_input(self, data_type: type) -> pd.DataFrame:
        """Reads a pandas DataFrame from a CSV file."""
        return pd.read_csv(self.uri)

    def handle_return(self, df: pd.DataFrame) -> None:
        """Writes a pandas DataFrame to a CSV file."""
        df.to_csv(self.uri, index=False)
import pandas as pd

class DataStore:
    """
    This is a class for pandas operations to store data.

    """
    @staticmethod
    def save(data=None):
        if data is not None:
            return pd.DataFrame(data)
        return None

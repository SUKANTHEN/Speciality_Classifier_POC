import pandas as pd


class KnowYourData:
    """
    Args:
    -----
    df - dataframe is expected as input to process KnowYourData Class functionalities
    
    Description:
    ------------
    KnowYourData class has 4 prominent methods
       - i) analyse_data : to get basic structure and anatomy of data
       - ii) feature_analysis : to get feature level analysis of a dataframe
       - iii) missing_value_estimation : to check and get the count of missing values
       - iv) data_quality_analysis : to check the quality of data
    """

    def __init__(self, df: pd.DataFrame) -> dict:
        self.df = df

    def analyze_data(self) -> dict:
        data = self.df
        data_shape = data.shape
        features_count = data.shape[1]
        sample_count = data.shape[0]
        analyze_data_report = {
            "data_dimensions": data_shape,
            "features_count": features_count,
            "sample_count": sample_count,
        }
        return analyze_data_report

    def feature_analysis(self) -> dict:
        data = self.df
        numerical_features = [f for f in data.columns if data[f].dtypes != "O"]
        count_of_numerical_features = len(numerical_features)
        cat_features = [c for c in data.columns if data[c].dtypes == "O"]
        count_of_categorical_features = len(cat_features)
        feature_analysis_report = {
            "numerical_features": numerical_features,
            "count_of_numerical_features": count_of_numerical_features,
            "categorical_features": cat_features,
            "count_of_categorical_features": count_of_categorical_features,
        }
        return feature_analysis_report

    def missing_value_estimation(self) -> dict:
        data = self.df
        try:
            sum_of_missing_value = data.isna().sum().sum()
        except ValueError:
            sum_of_missing_value = None
        try:
            feature_wise_check = data.isna().sum().to_json()
        except:
            feature_wise_check = None
        missing_value_report = {
            "is_missing_value": 1 if sum_of_missing_value else 0,
            "sum_of_missing_value": sum_of_missing_value,
            "missing_value_feature_wise": feature_wise_check,
        }

        return missing_value_report

    def data_quality_analysis(self) -> dict:
        # missing value estimation
        data = self.df
        try:
            is_missing_values = data.isna().sum()
        except:
            is_missing_values = "Cannot Process Missing Values"

        # duplication check
        try:
            is_duplicates = data.duplicated().sum()
        except:
            is_duplicates = "Cannot Process Missing Values"
        dqa_test_results = {
            "is_missing_values": is_missing_values,
            "is_duplicates": is_duplicates,
        }
        return dqa_test_results
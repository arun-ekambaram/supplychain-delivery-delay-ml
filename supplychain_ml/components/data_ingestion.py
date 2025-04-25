from supplychain_ml.exception.exception import SupplyChainException
from supplychain_ml.logging.logger import logging
from supplychain_ml.entity.config_entity import DataIngestionConfig
from supplychain_ml.entity.artifact_entity import DataIngestionArtifact
from sklearn.model_selection import train_test_split
import pandas as pd

from typing import List
import os, sys


class DataIngestion:
    def __init__(self,data_ingestion_config: DataIngestionConfig):
        try:
            self.data_ingestion_config=data_ingestion_config
            
        except Exception as e:
            raise SupplyChainException(e,sys)
        
    def export_local_csv_as_dataframe(self):
        try:
            file_path = self.data_ingestion_config.file_path
            
            if not os.path.exists(file_path):
                raise FileNotFoundError(f"CSV file not found at path: {file_path}")
            df = pd.read_csv(file_path)
            return df

        except Exception as e:
            raise SupplyChainException(e,sys)
        
    def export_data_into_feature_store(self,dataframe: pd.DataFrame):
        try:
            feature_store_file_path = self.data_ingestion_config.feature_store_file_path
            dir_path = os.path.dirname(feature_store_file_path)
            os.makedirs(dir_path, exist_ok=True)
            dataframe.to_csv(feature_store_file_path,index=False,header=True)
            return dataframe
        except Exception as e:
            raise SupplyChainException(e,sys)
        
    def load_existing_train_test_data(self):
        try:
            logging.info("Loading existing train and test datasets")
            train_set = pd.read_csv(self.data_ingestion_config.training_file)
            test_set = pd.read_csv(self.data_ingestion_config.testing_file)
            logging.info("Successfully loaded train and test data")
            train_dir = os.path.dirname(self.data_ingestion_config.training_file_path)
            test_dir = os.path.dirname(self.data_ingestion_config.testing_file_path)
            os.makedirs(train_dir, exist_ok=True)
            os.makedirs(test_dir, exist_ok=True)
            train_set.to_csv(self.data_ingestion_config.training_file_path, index=False, header=True)
            test_set.to_csv(self.data_ingestion_config.testing_file_path, index=False, header=True)

            logging.info("Successfully saved train and test data to configured paths")
            return train_set, test_set
        except Exception as e:
            raise SupplyChainException(e,sys)
        
    def initiate_data_ingestion(self):
        try:
            dataframe = self.export_local_csv_as_dataframe()
            dataframe = self.export_data_into_feature_store(dataframe)
            self.load_existing_train_test_data()
            dataingestionartifact = DataIngestionArtifact(trained_file_path=self.data_ingestion_config.training_file_path,
                                                          test_file_path=self.data_ingestion_config.testing_file_path)
            return dataingestionartifact

        except Exception as e:
            raise SupplyChainException(e,sys)

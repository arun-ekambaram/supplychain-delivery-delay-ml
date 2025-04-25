from supplychain_ml.components.data_ingestion import DataIngestion
from supplychain_ml.exception.exception import SupplyChainException
from supplychain_ml.logging.logger import logging
from supplychain_ml.entity.config_entity import DataIngestionConfig
from supplychain_ml.entity.config_entity import TrainingPipelineConfig
import os, sys

if __name__=='__main__':
    try:
        trainingpipelineconfig = TrainingPipelineConfig()
        dataingestionconfig = DataIngestionConfig(trainingpipelineconfig)
        dataingestion = DataIngestion(dataingestionconfig)
        logging.info("Initiate the data ingestion")
        dataingestionartifact = dataingestion.initiate_data_ingestion()
        print(dataingestionartifact)

    except Exception as e:
        raise SupplyChainException(e,sys)
import os
import sys
import numpy as np
import pandas as pd



"""
Defining common constant variables for training pipeline
"""
TARGET_COLUMN = "is_late_s"
PIPELINE_NAME: str = "supplychainml"
ARTIFACT_DIR: str = "Artifacts"
TRAIN_FILE_NAME: str = "train.csv"
TEST_FILE_NAME: str =  "test.csv"
FILE_NAME: str = "Supplychain.csv"
FILE_PATH: str = "/Users/arunekambaram/Desktop/supplychain-ml/notebook/intel-train-finn3.csv"
TRAIN_FILE_PATH: str = "/Users/arunekambaram/Desktop/supplychain-ml/notebook/intel-train-finn3.csv"
TEST_FILE_PATH: str = "/Users/arunekambaram/Desktop/supplychain-ml/notebook/intel-test-finn3.csv"

"""
Data Ingestion related constant start with DATA_INGESTION VAR NAME
"""

DATA_INGESTION_DIR_NAME: str = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store"
DATA_INGESTION_INGESTED_DIR: str = "ingested"




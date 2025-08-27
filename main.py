from network_security.components import data_ingestion
from network_security.components.data_ingestion import DataIngestion
from network_security.exception.exception import NetworkSecurityException
from network_security.logging.logger import logging
from network_security.entity.config_entity import DataIngestionConfig
from network_security.entity.config_entity import TrainingPipelineConfig
import sys

if __name__ == '__main__':
    try:
        
        train_pipeline_config = TrainingPipelineConfig()
        data_ingestion_config = DataIngestionConfig(train_pipeline_config)
        data_ingestion = DataIngestion(data_ingestion_config)
        
        logging.info('data ingestion initiate')
        
        artifact = data_ingestion.initiate_data_ingestion()
        
        print(artifact)
        
    except Exception as e:
        raise NetworkSecurityException(e,sys)
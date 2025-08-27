from network_security.components import data_ingestion
from network_security.components.data_ingestion import DataIngestion
from network_security.exception.exception import NetworkSecurityException
from network_security.logging.logger import logging
from network_security.entity.config_entity import DataIngestionConfig, DataTransformationConfig, DataValidationConfig
from network_security.entity.config_entity import TrainingPipelineConfig
from network_security.components.data_validation import DataValidation
from network_security.components.data_transformation import DataTransformation
import sys

if __name__ == '__main__':
    try:
        
        train_pipeline_config = TrainingPipelineConfig()
        data_ingestion_config = DataIngestionConfig(train_pipeline_config)
        data_ingestion = DataIngestion(data_ingestion_config)
        logging.info('data ingestion initiate')
        
        artifact = data_ingestion.initiate_data_ingestion()
        logging.info('data validation complete')
        
        data_validation_config = DataValidationConfig(train_pipeline_config)
        data_validation = DataValidation(artifact,data_validation_config)
        
        logging.info('initiate data validation')
        data_validation_artifact = data_validation.initiate_data_validtion()
        print(artifact)
        logging.info('data validation completed')
        print(data_validation_artifact)
        data_transformation_config = DataTransformationConfig(train_pipeline_config)
        logging.info('data trnasformation started')
        data_transformation = DataTransformation(data_validation_artifact,data_transformation_config)
        data_transformation_artifact = data_transformation.initiate_data_transformation()
        print(data_transformation_artifact)
        logging.info('data trnasformation complete')
        
    except Exception as e:
        raise NetworkSecurityException(e,sys)
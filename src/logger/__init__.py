import logging
import os 
from logger.handlers import RotatingFileHandler
from from_root import from_root 
from datetime import datetime

#Contrants for log comfiguration
LOG_DIR = 'logs'
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
MAX_LOG_SIZE = 5 * 1024 * 1024 # 5MB
BACKUP_COUNT = 3 # Number of backup log files to keep 

# Construct lof file path 
log_dir_path = os.path.join(from_root(), LOG_DIR)
os.makedirs(log_dir_path, exist_ok=True)
log_dir_path  = os.path.join(log_dir_path, LOG_FILE)

def configure_logger():
    """
    Configure logging wit a rotating file handler and a console handler. 
    """

    # Creating a custom logger 
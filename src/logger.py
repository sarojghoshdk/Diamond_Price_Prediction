import logging
import os
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"  # File & Folder Name
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)    # getcwd()-> get current working directory in this directory the "logs" folder is created
os.makedirs(logs_path,exist_ok=True)    # make the "logs" folder & if the folder is present then exit_ok = True

LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)  # To create each log file with name

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
#At production level we can't use exception.py file to chech each code file which has errors so we use logger.py which gives all the code files information of error and other things
#A logger.py file in a project is typically used to handle logging functionality. Logging is crucial in software development for tracking events, debugging, monitoring application behavior, and diagnosing issues.
import logging
import os
import sys
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE) # parameters= (gets the working directory, logs is folder name, then insert the LOG_FILE in that folder)
os.makedirs(logs_path,exist_ok=True) #if logs folder exist then it will help to stop to create same folder again
LOG_FILE_PATH= os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
    filename= LOG_FILE_PATH,
    format= "[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s ", # s= string, d=digit
    level=logging.INFO,
)

'''
if __name__=="__main__":
    logging.info("loggist is started") #logging.info() is used to log info messages
'''
import sys
from random import randint
import os
import requests
import json 
import logging
from config import *


print(LOG_FILE)
with open(LOG_FILE, 'w') as f:
    pass

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format=LOG_FORMAT
)

class Research():

    def __init__(self, file_name):
        self.f = file_name

    def file_reader(self, has_header = True):

        logging.info(f"Reading file: {self.f}")
        data = []

        if not os.path.exists(self.f):
            logging.error(f"File not {self.f} not found")
            raise ValueError("File doesn't exists")

        with open(self.f, 'r') as file:
            logging.info(f"File {self.f} opened")
            lines = file.readlines()
            if not has_header and (lines[0] != "0,1\n" and lines[0] != "1,0\n" and lines[0] != "1,1\n" and lines[0] != "0,0\n"):
                logging.error(f"Wrong header format")
                raise ValueError("Wrong header format")
            ans = []
            if has_header:
                lines = lines[1:]
            for line in lines:
                if not (line == "0,1\n" or line == "1,0\n" or line == "0,1" or line == "1,0"):
                    logging.error(f"Wrong value format")
                    raise ValueError("Wrong values")
                ans.append(line.strip().split(','))
            return(ans)
    
    @staticmethod
    def tg_send(exists):

        if exists:
            payload = {
                "chat_id": TELEGRAM_CHAT_ID,
                "text": success
            }
            response = requests.post(TELEGRAM_API_URL, data=payload)
            response.raise_for_status()
        else:
            payload = {
                "chat_id": TELEGRAM_CHAT_ID,
                "text": failure
            }
            response = requests.post(TELEGRAM_API_URL, data=payload)
            response.raise_for_status()
        

    
    class Calculations():

        @staticmethod
        def counts(values):
            logging.info(f'counts for {values}')
            ans = [0, 0]

            for i in values:
                ans[0] += int(i[0])
                ans[1] += int(i[1])

            return ans
        
        @staticmethod
        def fractions(val):
            logging.info(f'fractions for {val}')
            ans = []
            ans.append(100*(val[0]/(val[0] + val[1])))
            ans.append(100*(val[1]/(val[0] + val[1])))
            return ans

class Analytics(Research):
    @staticmethod
    def predict_random(cnt):
        logging.info(f'predicting {cnt}')
        ans = []
        for i in range(cnt):
            a = randint(0, 1)
            ans.append([a, 1 - a])
        return ans[:len(ans)-1] 

    @staticmethod
    def predict_last():
        logging.info(f'predicting last')
        a = randint(0, 1)
        return [a, 1 - a]

    @staticmethod
    def save_file(data, name, form):
        file_path = name + '.' + form
        logging.info(f'saving report in {file_path}')
        with open(file_path, 'w') as file:
            file.write(data)
        
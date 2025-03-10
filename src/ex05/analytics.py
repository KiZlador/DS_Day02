import sys
from random import randint
from config import *

class Research():

    def __init__(self, filename):
        self.f = filename

    def file_reader(self, has_header = True):        
        with open(self.f, 'r') as file:
            lines = file.readlines()
            if not has_header and (lines[0] != "0,1\n" and lines[0] != "1,0\n" and lines[0] != "1,1\n" and lines[0] != "0,0\n"):
                raise ValueError("Wrong header format")
            ans = []
            if has_header:
                lines = lines[1:]
            for line in lines:
                if not (line == "0,1\n" or line == "1,0\n" or line == "0,1" or line == "1,0"):
                    raise ValueError("Wrong values")
                ans.append(line.strip().split(','))
            return(ans)
    
    class Calculations():

        @staticmethod
        def counts(values):
            ans = [0, 0]

            for i in values:
                ans[0] += int(i[0])
                ans[1] += int(i[1])

            return ans
        
        @staticmethod
        def fractions(val):
            ans = []
            ans.append(100*(val[0]/(val[0] + val[1])))
            ans.append(100*(val[1]/(val[0] + val[1])))
            return ans

class Analytics(Research):
    @staticmethod
    def predict_random(cnt):
        ans = []
        for i in range(cnt):
            a = randint(0, 1)
            ans.append([a, 1 - a])
        return ans[:len(ans)-1] 

    @staticmethod
    def predict_last():
        a = randint(0, 1)
        return [a, 1 - a]

    @staticmethod
    def save_file(data, name, format):
        file_name = name + '.' + format
        with open(file_name, 'w') as file:
            file.write(data)
        
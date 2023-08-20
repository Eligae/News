import numpy as np 
import pandas as pd
import os
from src.function import var


def getData():
    for file in os.listdir(var.DATA_PATH):
        if 'txt' in file:
            print(file.ljust(30) + str(round(os.path.getsize(var.DATA_PATH + file) / 100000, 2)) + 'MB')

import pandas as pd
import numpy as np
import datetime as dt
import itertools
import math

def read_file(file_name):
  with open(file_name) as f:
      lines = f.readlines()
  return lines
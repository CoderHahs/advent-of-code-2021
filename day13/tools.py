import pandas as pd
import numpy as np
import datetime as dt
import itertools
import math
from collections import defaultdict

def read_file(file_name):
  with open(file_name) as f:
      lines = f.readlines()
      lines = [j for j in lines if j != '\n']
  return lines
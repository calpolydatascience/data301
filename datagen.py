from __future__ import absolute_import
from __future__ import print_function

import pandas as pd
import numpy as np

def ages(N, min=0, max=109):
    ages = np.random.randint(min, max+1, size=N)
    return ages

def grades(N):
    letters = [str.upper for letter in list('abcdf')]
    return np.random.choice(letters, size=N)

def genders(N, pfemale=0.5):
    return np.random.choice(['Female', 'Male'], size=N, p=[1.0-pfemale, pfemale])

def categorical(N, items):

def misspell(s):

def makeempty(s):
    return ''

def lower(s):
    return s.lower()

def upper(s):
    return s.upper()


        
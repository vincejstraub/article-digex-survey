#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
The get_summary_statistics module includes methods for computing
summary statistics
"""


import yaml   # 3rd party packages
import warnings
import pandas as pd
import numpy as np
from nltk import flatten
from pathlib import Path
from pandas_profiling import ProfileReport

from . import config   # Local imports
from . import utils
from . import load_data


PARTICIPANT_COUNT = config.PARTICIPANT_COUNT
DECIMAL_PLACES = config.DECIMAL_PLACES


def completed_participants(df, col='finished'):
    return df.loc[df[col] == True][col].sum()


def response_rate(df, 
                  col='finished', 
                  as_percentage=True, 
                  total=PARTICIPANT_COUNT,
                  decimal=DECIMAL_PLACES
):
    if as_percentage:
        percentage = (df.loc[df[col] == True][col].sum() / total) * 100
        return f"%.{decimal}f" % percentage
    else:
        rate = df.loc[df[col] == True][col].sum()
        print(rate, 'per', total)
#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
The get_summary_statistics module includes methods for computing
summary statistics
"""


import yaml   # 3rd party packages
import warnings
import datetime
import pandas as pd
from pathlib import Path

from . import config   # Local imports
from . import utils
from . import load_data


PARTICIPANT_COUNT = config.PARTICIPANT_COUNT
DECIMAL_PLACES = config.DECIMAL_PLACES


def summary_statistics(df):
    print('Completed participants:', completed_participants(df))
    
    print('Response rate:', response_rate(df))
    
    print('Completion time summary:')
    print(completion_time(df))
    
    print('Demographic information:')
    print(demographic_information(df))


def completed_participants(df, col='finished'):
    return df.loc[df[col] == True][col].sum()


def response_rate(df, 
                  col='finished', 
                  as_percentage=True, 
                  total=config.PARTICIPANT_COUNT,
):
    if as_percentage:
        i = (df.loc[df[col] == True][col].sum() / total) * 100
        return i
    else:
        r = df.loc[df[col] == True][col].sum()
        return f'{r} per {total}'
    
    
def completion_time(df, col='duration_sec', time_unit='sec'):
    if time_unit == 'sec':
        return df[col].describe()
    elif time_unit == 'min':
        return pd.to_timedelta(df[col], 's').describe()
    
    
def demographic_information(df,
                            var_list=['age', 'gender_id', 'ethnic_id',
                               'edu', 'politic_views'],
                            age_vars = ['Average', 'Standard deviation', 
                                 'Min', 'Max'],
                            num_val = 'age',
                            num_vars = ['mean', 'std', 'min', 'max'], 
                            dec=DECIMAL_PLACES):
    dic = {}
    for col in var_list:
        if col == num_val:
            dic[col] = age_vars
            dic[str(col+'_vals')] = [df[num_val].describe()[val] 
                for val in num_vars]
        else:
            dic[col] = list(
                df[col].value_counts().keys())
            dic[str(col+'_vals')] = list(
                df[col].value_counts())
            dic[str(col+'_perc')] = list(
                (df[col].value_counts(normalize=True) * 100).round(dec)
            )

    df = pd.DataFrame(
        dict([ (k,pd.Series(v)) for k,v in dic.items() ])
    ).fillna('')
                     
    return df


if __name__ == "__main__": 
    raw_data_df = load_data.load_data_into_df(
        file=RAW_DATA_FILEPATH, data_path=RAW_DATA_DIR
    )
    processed_data = preprocess_data(raw_data_df, generate_reports=False)
    print(summary_statistics(processed_data))
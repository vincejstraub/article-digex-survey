#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
The preprocess module includes methods for preprocessing
the raw survey .xlsx file and generating a preprocessed CSV file.
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


RAW_DATA_DIR = config.RAW_DATA_DIR
RAW_DATA_FILEPATH = config.RAW_DATA_FILEPATH
PROCESSED_DATA_DIR = config.PROCESSED_DATA_DIR
REPORTS_DIR = config.REPORTS_DIR
COLS_TO_DROP = config.COLS_TO_DROP
DTYPES_COLS = config.DTYPES_COLS
NA_RESPONSES = config.NA_RESPONSES
MIN_RESPONSE_LEN = config.MIN_RESPONSE_LEN
MAX_NA_RESPONE_LEN = config.MAX_NA_RESPONE_LEN
COLS_WITH_NA_RESPONSES = config.COLS_WITH_NA_RESPONSES
AWARE_ANSWERS = config.AWARE_ANSWERS
VARIABLE_TABLE_DICT = config.VARIABLE_TABLE_DICT
# COLS_FINAL_ORDER = config.COLS_FINAL_ORDER


def preprocess_data(
    df, 
    generate_reports=True,
    save_to_file=True, 
    filedir=PROCESSED_DATA_DIR, 
    filename='digex-survey-responses-processed',
    main=False
):
    if generate_reports:
        generate_profiling_report(
            df, filename='digex-raw-data-report'
        )
    
    drop(df, drop_cols=COLS_TO_DROP)

    str_vals_to_float(df, [
        'rank_add_fac_1_pos', 'rank_add_fac_2_pos', 'rank_add_fac_3_pos'
    ])

    for col in COLS_WITH_NA_RESPONSES:
        df[col] = filter_responses(
            df, col
        )

    assign_dtypes(df, DTYPES_COLS)

    replace_nan_str_vals(df)

    for col in [
        'aware_sm_advan', 'aware_sm_interact', 'aware_sm_use']:
        df = str_to_list(df, col)

    for col in ['aware_sm_advan', 'aware_sm_interact', 'aware_sm_use']:
        new_col = col + '_score'
        df[new_col] = df[col].apply(
            get_awareness_score, 
            seq2=AWARE_ANSWERS[col].keys(), 
            value_dic=AWARE_ANSWERS[col]
        )
    
    # reorder cols to align variable table
    df = df[config.VARIABLE_TABLE_DICT['variable abbreviation']]    

    generate_html_table_from_df(
        dic=VARIABLE_TABLE_DICT, out_dir=REPORTS_DIR, filename='variable-table'
    )
    
    if generate_reports:
        generate_profiling_report(
            df, filename='digex-processed-data-report'
        )

    if save_to_file:
        # save DataFrame as CSV to data
        if main == True:
            root_dir = utils.get_grandparent_path()
        else:
            root_dir = utils.get_parent_path()
        df.to_csv(
            f"{root_dir.joinpath(filedir, filename)}.csv"
        )
    
    return df


def generate_profiling_report(
    df, filedir=REPORTS_DIR, filename='digex-raw-data-report', 
    main=False, title="Digex Qualtrics Survey Responses"
):
    # See: https://pandas-profiling.ydata.ai/docs/master/index.html
    profile = ProfileReport(
        df, title=title
    )

    # Save report as html to reports/ directory
    if main == True:
        root_dir = utils.get_grandparent_path()
    else:
        root_dir = utils.get_parent_path()
    profile.to_file(
        f"{root_dir.joinpath(filedir, filename)}.html"
    )
        
        
def drop(df, drop_cols=[''], rows=[0]):
    try:
        df.drop(columns=drop_cols, inplace=True)
        df.drop(rows, inplace=True)
    except KeyError:
        print(f'Columns that do not exist in axis: {drop_cols}')
    

def assign_dtypes(df, dtypes_cols: dict):
    for dtype_col in dtypes_cols:
        dtype = list(dtype_col.keys())[0]
        col = flatten(list(dtype_col.values()))
        try:
            df[col] = df[col].apply(lambda x: x.astype(dtype))
        except ValueError:
            print('Dataset contains unexpected values. ' 
                  'Check all invalid responses are recorded as np.nan.')
        
            
def str_vals_to_float(df, cols=[]):
    for col in cols:
        df[col]=df[col].apply(
            lambda x: float(x) if is_float_as_str(x) else np.nan
        )
    return df


def is_float_as_str(x):
    try:
        isinstance(float(x), float)
        return True
    except ValueError:
        return False 
    
    
def filter_responses(df, col):
    funcs = [
        remove_chars_make_lower, 
        check_response_len, 
        detect_na_response
    ]
    for func in funcs:
        df[col] = df[col].apply(func)
    return df[col]


def remove_chars_make_lower(response, chars=['/', '\\', '.', '\n']):
    if type(response) == str:
        for ch in chars:
            if ch in response:
                response = response.replace(ch, '')
        return response.lower().strip()
    else:
        return np.nan
    
    
def check_response_len(response, thresh=MIN_RESPONSE_LEN):
    if type(response) == str and len(response) <= thresh:
        return np.nan
    else:
        return response
    
    
def detect_na_response(
    response, thresh=MAX_NA_RESPONE_LEN, chars=NA_RESPONSES
):
    if isinstance(response, str) and len(response) <=thresh:
        for ch in chars:
            try:
                if ch in response:
                    response = np.nan
            except TypeError:
                return response
    else:
        return response
    
    
def replace_nan_str_vals(df, nan_str='nan', na=np.nan):
    df.replace(nan_str, na, inplace=True)
    

def str_to_list(df, col, char=','):
    df[col] = df[col].str.split(char)
    return df


def get_intersection(seq1, seq2):
    return list(set(seq1).intersection(set(seq2)))


def get_awareness_score(seq1, seq2, value_dic):
    score = 0
    matches = get_intersection(seq1, seq2)
    for answer in matches:
        score += value_dic[answer]
    return score


def generate_html_table_from_df(
    dic=VARIABLE_TABLE_DICT, 
    out_dir=REPORTS_DIR,
    filename='variable-table'
):

    # Create dataframe
    df_marks = pd.DataFrame(dic)

    # Render dataframe as html
    html = df_marks.to_html()

    # Write html to file
    path = utils.get_parent_path()
    text_file = open(
        path.joinpath(out_dir, f"{filename}.html"), "w"
    )
    text_file.write(html)
    text_file.close()

    
if __name__ == "__main__": 
    raw_data_df = load_data.load_data_into_df(
        file=RAW_DATA_FILEPATH, data_path=RAW_DATA_DIR
    )
    processed_data = preprocess_data(raw_data_df, generate_reports=False)
    print(processed_data_df.describe())
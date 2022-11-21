#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
The load_raw_data module includes methods for finding the raw
survey .xlsx file and loading it into a pandas DataFrame.
"""

import yaml   # Standard library
from pathlib import Path

import pandas as pd   # 3rd party packages

from . import config   # Local imports
from . import utils 


RAW_DATA_DIR = config.RAW_DATA_DIR
RAW_DATA_FILEPATH = config.RAW_DATA_FILEPATH


def load_data_into_df(
    file=RAW_DATA_FILEPATH, data_path=RAW_DATA_DIR, main=False
):
    try:
        df = pd.read_excel(file)
        return df
    except FileNotFoundError:
        try:
            df = pd.read_excel(
                get_data_filepath(file, main, data_path)
            )
            return df
        except FileNotFoundError as e:
            if data_dir_exists(data_path):
                print(
                    f"No such file: '{file}'"
                )
            else:
                missing_dir = get_data_filepath(file, main, data_path)
                print(
                    f"No such directory: '{missing_dir}'"
                )
            path_message()
            config_message()

        
def get_data_filepath(
    file=RAW_DATA_FILEPATH, main=False, data_path=RAW_DATA_DIR
):
    if main:    # If module is run as part of main.py
        return (utils.get_parent_path()).joinpath(data_path, file)
    else:    # If function is called in a notebook
        return (utils.get_parent_path()).joinpath(data_path, file)
    

def data_dir_exists(data_path=RAW_DATA_DIR):
    if (utils.get_grandparent_path()).joinpath(data_path).exists():
        return True
    else:
        return False
    

def find_filepath_from_root(filename=RAW_DATA_FILEPATH):
    paths = (utils.get_grandparent_path()).glob(f'**/*{filename}')
    return [path for path in paths if path.is_file()]


def path_message():
    print(f"Your current working directory path: {Path.cwd()}")
    

def config_message():
    print("Set global variables in the file: src/scripts/config.py")


if __name__ == "__main__": 
    raw_data_df = load_data_into_df(
        file=RAW_DATA_FILEPATH, data_path=RAW_DATA_DIR
    )
    print(raw_data_df.describe())
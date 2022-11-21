#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
The run_analysis.py script reproduces the data analysis workflow for 
the digex project.
"""

import yaml    # 3rd party packages

import digex_src.config as config    # Local imports
import digex_src.preprocess as preprocess
from digex_src.load_data import load_data_into_df 


raw_data_df = load_data_into_df()
preprocessed_data_df = preprocess.preprocess_data(
    raw_data_df,
    generate_reports=False)

#### The below scripts still need to be finished #####

# get_summary_statistics(preprocessed_data)
# generate_plots(preprocessed_data)
# text_analysis(preprocessed_data)



if __name__ == "__main__": 
    raw_data_df = load_data_into_df()
    preprocessed_data_df = preprocess.preprocess_data(
        raw_data_df,
        generate_reports=False)
    print(preprocessed_data_df.describe())
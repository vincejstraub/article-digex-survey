#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
The run_analysis.py script reproduces the data analysis workflow for 
the digex project.
"""

import yaml    # 3rd party packages

import digex_src.config as config    # Local imports
import digex_src.preprocess as preprocess
import digex_src.get_summary_statistics as summarize
from digex_src.load_data import load_data_into_df 


def main():
    raw_data_df = load_data_into_df()
    preprocessed_data_df = preprocess.preprocess_data(
        raw_data_df,
        generate_reports=False)
    summarize.summary_statistics(preprocessed_data_df)

#### The below scripts still need to be finished #####

# generate_plots(preprocessed_data)
# text_analysis(preprocessed_data)


if __name__ == "__main__": 
    main()
#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
The main.py script reproduces the workflow.
"""

import yaml    # 3rd party packages


import scripts.config as config    # Local imports
import scripts.preprocess_data as preprocess
from scripts.load_data import load_raw_data_into_df 


raw_data_df = load_raw_data_into_df()
# preprocessed_data = preprocess(raw_data_df)
# get_summary_statistics(preprocessed_data)
#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
The preprocess_data module includes methods for cleaning
the dataset '2022-digex-survey-responses-raw.xlsx'.
"""

import yaml   # Standard library
from pathlib import Path

import pandas as pd   # 3rd party packages
from pandas_profiling import ProfileReport

from . import config   # Local imports
from . import utils


REPORTS_DIR = config.REPORTS_DIR 


def generate_profiling_report(
    df, filedir=REPORTS_DIR, filename='digex-raw-data-report', main=False,
    title="Digex Qualtrics Survey Responses", notebook=False
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
    
    if notebook:
        return profile
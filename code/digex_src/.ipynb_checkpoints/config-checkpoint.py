#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
The config module contains global variables used across notebooks, 
digex_src modules, and the run_digex_analysis.py script.
"""

from pandas.api.types import CategoricalDtype


ROOT_DIR = 'article-digex-survey/'
REPORTS_DIR = 'reports/'
RAW_DATA_DIR = 'data/raw/'
PROCESSED_DATA_DIR = 'data/processed/'
RAW_DATA_FILEPATH = 'digex-survey-responses-raw.xlsx'
PROCESSED_DATA_FILEPATH = 'digex-survey-responses-processed.xlsx'

COLS_TO_DROP = [
    'start_date', 'end_date', 'status', 'progress', 'duration_sec',
    'finished', 'date', 'consent', 'q_recaptcha_scor', 'date'
]

edu_order = [
    "Prefer not to say", "Highschool", "Vocational training", 
    "Some college",  "Associate's degree", "Bachelor's degree",
    "Master's degree or above"
]

edu_cat_dtype = CategoricalDtype(
    categories=edu_order, ordered=True)

sm_res_purp_order = [
    'Not at all aware', 'Slightly aware', 'Moderately aware', 
    'Very aware', 'Extremely aware'
]

sm_res_purp_cat_dtype = CategoricalDtype(
    categories=sm_res_purp_order, ordered=True
)

design_vars_order = [
    'Not at all important', 'Slightly important', 'Moderately important', 
    'Very important', 'Extremely important'
]

design_cat_dtype = CategoricalDtype(
    categories=design_vars_order, ordered=True
)

ethi_acc_order = [
     'Completey unacceptable', 'Somewhat unacceptable', 'Neutral',
     'Somewhat acceptable', 'Completey acceptable'
]

ethic_acc_cat_dtype = CategoricalDtype(
    categories=ethi_acc_order, ordered=True
)


DTYPES_COLS = [
    {'int' : [
        'age', 'rank_sci_repro', 'rank_resp', 'rank_just',
        'rank_anony', 'rank_harms', 'rank_balance', 'rank_pub_interst',
        'rank_add_fac_1_pos', 'rank_add_fac_2_pos', 'rank_add_fac_3_pos'
    ]},
    {'str' : [
        'sm_aware', 'sm_expmt_inerct', 'sm_data_use', 'ethic_appr', 
        'study_1_conc', 'study_1_add_info', 'study_2_conc',
        'study_2_add_info', 'study_3_conc', 'study_3_add_info', 
        'study_4_conc', 'study_4_add_info', 'design_add_fac', 
        'rank_add_fac_1', 'rank_add_fac_2', 'rank_add_fac_3',
    ]},
    {'category': ['sm_use', 'gender_id', 'ethnic_id', 'politic_pref']},
    {edu_cat_dtype: ['edu']},
    {sm_res_purp_cat_dtype: ['sm_res_purp']},
    {design_cat_dtype: [
        'design_cont', 'design_num_users', 'design_res_purp', 'design_len_data',
        'design_admin_inter', 'design_inter_type', 'design_partic_aware', 
        'design_inter_impact', 'design_type_data'
    ]},
    {ethic_acc_cat_dtype: [
        'study_1_ethic_acc', 'study_2_ethic_acc',
        'study_3_ethic_acc', 'study_4_ethic_acc'
    ]}
]

NA_RESPONSES = [
    'na', 'n', 'no', 'none', 'nana', 'nope', 'i don\'t think so', 
    'i do not think so', 'nothing specific','i think this is fine', 
    'i don\'t really think so', 'no concern', 'no additional factors', 
    'can\'t think of any', 'i don\'t think so', 'not really', 'not sure',
    'no other concerns', 'nothing', 'cannot think of any'
]

MIN_RESPONSE_LEN = 2
MAX_NA_RESPONE_LEN = 30

COLS_WITH_NA_RESPONSES = [
    'study_1_conc', 'study_1_add_info', 'study_2_conc',
    'study_2_add_info', 'study_3_conc', 'study_3_add_info',
    'study_4_conc', 'study_4_add_info', 'design_add_fac',
    'rank_add_fac_1', 'rank_add_fac_2', 'rank_add_fac_3'
]
#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
The config module contains global variables used across notebooks, 
digex_src modules, and the run_analysis.py script.
"""

from pandas.api.types import CategoricalDtype


ROOT_DIR = 'article-digex-survey/'
REPORTS_DIR = 'reports/'
RAW_DATA_DIR = 'data/raw/'
PROCESSED_DATA_DIR = 'data/processed/'
RAW_DATA_FILEPATH = 'digex-survey-responses-raw.xlsx'
PROCESSED_DATA_FILEPATH = 'digex-survey-responses-processed.csv'

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

aware_sm_res_order = [
    'Not at all aware', 'Slightly aware', 'Moderately aware', 
    'Very aware', 'Extremely aware'
]

aware_sm_res_cat_dtype = CategoricalDtype(
    categories=aware_sm_res_order, ordered=True
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
    {'float' : [
        'age', 'rank_sci_repro', 'rank_resp', 'rank_just',
        'rank_anony', 'rank_harms', 'rank_balance', 'rank_pub_interst',
        'rank_add_fac_1_pos', 'rank_add_fac_2_pos', 'rank_add_fac_3_pos'
    ]},
    {'str' : [
        'aware_sm_advan', 'aware_sm_interact', 'aware_sm_use', 'ethic_appr', 
        'study_1_conc', 'study_1_add_info', 'study_2_conc',
        'study_2_add_info', 'study_3_conc', 'study_3_add_info', 
        'study_4_conc', 'study_4_add_info', 'design_add_fac', 
        'rank_add_fac_1', 'rank_add_fac_2', 'rank_add_fac_3',
    ]},
    {'category': ['sm_use', 'gender_id', 'ethnic_id', 'politic_views']},
    {edu_cat_dtype: ['edu']},
    {aware_sm_res_cat_dtype: ['aware_sm_res']},
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


AWARE_ANSWERS = {
    'aware_sm_advan': {
        '… are large and can contain millions of data points' : 1,
        '… reflect events in real-time and can be collected continuously over time': 1,
        '… are naturalistic in that they do not require researchers to directly interact with research volunteers': 1,
        '… often capture social relationships not found using traditional methods (e.g. surveys)': 1,
        '… are readily accessible to researchers and easy to collect' : -1,
        '… are always representative of people’s offline behavior' : -1,
        '… are unaffected by the way social media platforms work' : -1, 
        '… are well formatted and never contain any missing data' : -1
    },        
    'aware_sm_interact' : {
        'Privately messaging users' : 1,
        "Publicly posting on users' profiles" : 1,
        'Creating fake accounts ("bots")' : 1,
        'Secretly changing the content of what users see' : -1,
        "Hacking into users\' accounts" : -1
    },
    'aware_sm_use' : {
        'Political elections (e.g. voting behavior)': 1,
        'Economic forecasting' : 1, 
        'Presidential approval ratings' : 1,  
        'Health topics (e.g. spread of diseases)' : 1, 
        'Well-being and economic satisfaction' : 1, 
        'Communication (e.g. spread of opinions and hate-speech)' : 1, 
        'Public sentiment (e.g. environment-related concerns)' : 1, 
        'News consumption (e.g. sharing of misinformation)' : 1,
        'Social networks': 1,
    }
}

VARIABLE_TABLE_DICT = {
    'variable abbreviation': [
        'sm_use', 
        'age', 'gender_id', 'ethnic_id', 'edu', 'politic_views',
        'aware_sm_res', 
        'aware_sm_advan', 'aware_sm_interact', 'aware_sm_use','aware_sm_advan_score', 
        'aware_sm_interact_score', 'aware_sm_use_score', 'ethic_appr', 
        'study_1_ethic_acc', 
        'study_1_conc', 'study_1_add_info',
        'study_2_ethic_acc', 'study_2_conc', 'study_2_add_info',
        'study_3_ethic_acc', 'study_3_conc', 'study_3_add_info',
        'study_4_ethic_acc', 'study_4_conc', 'study_4_add_info', 
        'design_cont', 
        'design_num_users', 'design_res_purp', 'design_len_data',
        'design_admin_inter', 'design_inter_type', 'design_partic_aware',
        'design_inter_impact', 'design_type_data', 'design_add_fac',
        'rank_sci_repro', 'rank_resp', 'rank_just', 'rank_anony', 'rank_harms',
        'rank_balance', 'rank_pub_interst', 'rank_add_fac_1', 'rank_add_fac_1_pos', 
        'rank_add_fac_2', 'rank_add_fac_2_pos','rank_add_fac_3', 'rank_add_fac_3_pos'
    ],
    'variable name': [
        'social media use', 
        'age', 'gender identity', 'ethnic identity', 'education level', 'political viewpoint', 
        'awareness of social media research',
        'awareness of social media data advantages', 'awareness of social media interactions',
        'awareness of social media data uses', 'awareness of social media data advantages score', 
        'awareness of social media interactions score', 'awareness of social media data uses score', 'understanding of ethical approval', 
        'ethical acceptance of study 1', 
        'concerns about study 1', 'addition information wanted for study 1', 'ethical acceptance of study 2', 
        'concerns about study 2', 'addition information wanted for study 2', 'ethical acceptance of study 3', 
        'concerns about study 3', 'addition information wanted for study 3', 'ethical acceptance of study 4', 
        'concerns about study 4', 'addition information wanted for study 4', 
        'content of data', 
        'number of users studied', 'research purpose', 'type of data', 'length of data collection', 'administration of intervention',
        'type of intervention', 'participant awareness of study', 'impact of intervention', 'additional design factors', 
        'scientific reproducibility', 'respect for participants via informed consent', 'just and fair study design', 
        'safeguard participant anonymity', 'avoid harms at all costs', 'balance benefits versus risks', 
        'respect the law and wider public interest', 'additional factor suggested 1', 'additional factor suggested 1 ranking', 
        'additional factor suggested 2', 'additional factor suggested 2 ranking','additional factor suggested 3', 
        'additional factor suggested 3 ranking'
    ], 
    'survey section' : [
        'demographics', 
        'demographics', 'demographics', 'demographics', 'demographics','demographics',  
        'prior awareness', 
        'prior awareness', 'prior awareness', 'prior awareness', 'prior awareness', 
        'prior awareness', 'prior awareness', 'prior awareness', 
        'study descriptions', 
        'study descriptions', 'study descriptions', 'study descriptions', 'study descriptions', 
        'study descriptions', 'study descriptions', 'study descriptions', 'study descriptions', 
        'study descriptions', 'study descriptions', 'study descriptions', 
        'study design features', 
        'study design features', 'study design features', 'study design features', 
        'study design features', 'study design features', 'study design features', 
        'study design features', 'study design features', 'study design features', 
        'study design features', 'study design features', 'study design features', 
        'study design features', 'study design features', 'study design features', 
        'study design features', 'study design features', 'study design features', 
        'study design features', 'study design features', 'study design features', 
        'study design features'
    ]
}
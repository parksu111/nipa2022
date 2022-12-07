import os, joblib
import sys

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
from datetime import datetime, timezone, timedelta
import pickle

from lightgbm.callback import record_evaluation

from models.ML_model import get_ml_model
from modules.utils import load_yaml, load_pkl, make_directory, save_pkl, save_yaml

# CONFIG
PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))

TRAIN_CONFIG_PATH = os.path.join(PROJECT_DIR, 'config/train_config.yaml')
config = load_yaml(TRAIN_CONFIG_PATH)


# DATA
DATA_DIR = config['DIRECTORY']['data']

# SEED
RANDOM_SEED = config['SEED']['random_seed']

# MODEL
MODEL_STR = config['MODEL']
PARAMETER = config['PARAMETER']
#LABEL_ENCODE
LABEL_ENCODING = config['LABEL_ENCODING']

# TRAIN
EARLY_STOPPING_ROUND = config['TRAIN']['early_stopping_round']

# time offset set
KST = timezone(timedelta(hours=9))
TRAIN_TIMESTAMP = datetime.now(tz=KST).strftime("%Y%m%d_%H%M%S")
TRAIN_SERIAL = MODEL_STR + '_' + TRAIN_TIMESTAMP 

# PERFORMANCE RECORD
PERFORMANCE_RECORD_DIR = os.path.join(PROJECT_DIR, 'results', 'train', TRAIN_SERIAL)

if __name__ == '__main__':
    make_directory(PERFORMANCE_RECORD_DIR)
    save_yaml(os.path.join(PERFORMANCE_RECORD_DIR,'train_config.yaml'),config)
    
    train_df = pd.read_csv(os.path.join(DATA_DIR, 'train.csv'))
    valid_df = pd.read_csv(os.path.join(DATA_DIR, 'valid.csv'))
    
    train_X, train_y = train_df.loc[:,train_df.columns!='leaktype'], train_df['leaktype']
    valid_X, valid_y = valid_df.loc[:,train_df.columns!='leaktype'], valid_df['leaktype']
    
    train_y = train_y.replace(LABEL_ENCODING)
    valid_y = valid_y.replace(LABEL_ENCODING)

    
    #MODEL
    model = get_ml_model(MODEL_STR, PARAMETER)
    
    history = dict()
    model.fit(
        train_X,
        train_y,
        eval_set = [(train_X, train_y),(valid_X, valid_y)],
        early_stopping_rounds=EARLY_STOPPING_ROUND,
        verbose=1,
        callbacks=[record_evaluation(history)])
    
    # SAVE MODEL
    
    joblib.dump(model, os.path.join(PERFORMANCE_RECORD_DIR,'model.pkl'))
    save_pkl(os.path.join(PERFORMANCE_RECORD_DIR,'loss_history.pkl'),history)
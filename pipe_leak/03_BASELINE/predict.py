import os, joblib
import sys

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
from datetime import datetime, timezone, timedelta

from lightgbm.callback import record_evaluation

from models.ML_model import get_ml_model
from modules.utils import load_yaml, load_pkl, make_directory, save_pkl, save_yaml

# CONFIG
PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
PREDICT_CONFIG_PATH = os.path.join(PROJECT_DIR, 'config/predict_config.yaml')

# load predict_config
predict_config = load_yaml(PREDICT_CONFIG_PATH)
train_serial = predict_config['EXPERIMENT']['serial']

# load train_config
TRAIN_CONFIG_PATH = os.path.join(PROJECT_DIR,'results/train',train_serial)
train_config = load_yaml(os.path.join(TRAIN_CONFIG_PATH,'train_config.yaml'))

# DATA
#DATASET = predict_config['DIRECTORY']['dataset']
PHASE = predict_config['DIRECTORY']['phase']
DATA_DIR = predict_config['DIRECTORY']['data']
SAMPLE_DIR = predict_config['DIRECTORY']['sample']

#LABEL DECODE
LABEL_ENCODING = predict_config['LABEL_ENCODING']
LABEL_DECODING = {y:x for x,y in LABEL_ENCODING.items()}

# MODEL
MODEL_DIR = os.path.join(PROJECT_DIR,'results/train',train_serial)
MODEL_STR = train_config['MODEL']
print(f'Predict {MODEL_STR} model!')


# PREDICT SERIAL
KST = timezone(timedelta(hours=9))
PREDICT_TIMESTAMP = datetime.now(tz=KST).strftime("%Y%m%d%H%M%S")
PREDICT_SERIAL = f'{PREDICT_TIMESTAMP}' 

# time offset set
PREDICT_SERIAL = train_serial + '_' + PREDICT_SERIAL 

# PERFORMANCE RECORD
RECORD_DIR = os.path.join(PROJECT_DIR, 'results', 'predict')

PREDICT_SAVE_DIR = os.path.join(PROJECT_DIR, 'results', 'predict', PREDICT_SERIAL)
result_path = os.path.join(RECORD_DIR,PREDICT_SERIAL)

if __name__ == '__main__':
    make_directory(result_path)
    # -------- save config
    save_yaml(os.path.join(result_path,'train_config.yaml'),train_config)
    save_yaml(os.path.join(result_path,'predict_config.yaml'),predict_config)
    
    test_df = pd.read_csv(os.path.join(DATA_DIR,'test.csv'))
    test_X = test_df.loc[:,test_df.columns!='id']
    test_ids = test_df['id']
    
    model = joblib.load(os.path.join(MODEL_DIR,'model.pkl'))
    print(f'complete {train_serial} model load')
    
    print('Making predictions')
    
    sample_df = pd.read_csv(SAMPLE_DIR)
    sorter = list(sample_df['id'])
    
    y_pred = model.predict(test_X)
    y_pred_df = pd.DataFrame(y_pred, columns=['leaktype'])
    y_pred_df['leaktype'] = y_pred_df['leaktype'].replace(LABEL_DECODING)
    pred_df = pd.concat([test_ids, y_pred_df],axis=1)
    
    # sort predictions
    resdf = pred_df.set_index('id')
    result = resdf.loc[sorter].reset_index()
    resultpath = os.path.join(result_path, 'predictions.csv')
    result.to_csv(resultpath, index=False)

    print('end')
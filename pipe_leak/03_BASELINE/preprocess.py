import os
import pandas as pd
from sklearn.model_selection import train_test_split
from modules.utils import load_yaml, load_pkl, make_directory, save_pkl, save_yaml


PROJECT_DIR = os.path.dirname(__file__)

PREPROCESS_CONFIG_PATH = os.path.join(PROJECT_DIR, 'config/preprocess_config.yaml')
config = load_yaml(PREPROCESS_CONFIG_PATH)

SRC_DIR = config['DIRECTORY']['srcdir']
DST_DIR = config['DIRECTORY']['dstdir']

# Read in train data
DATA_PATH = os.path.join(SRC_DIR, 'train.csv')
data = pd.read_csv(DATA_PATH)

# Split dataset
cols = list(data.columns)
cols = [x for x in cols if 'HZ' in x]

X = data[cols]
y = data['leaktype']

X_train, X_valid, y_train, y_valid = train_test_split(X,y,test_size = 0.2, shuffle=True, random_state=42)

traindf = pd.concat([X_train, y_train],axis=1)
validdf = pd.concat([X_valid, y_valid],axis=1)

# Save split dataset
trainpath = os.path.join(DST_DIR, 'train.csv')
validpath = os.path.join(DST_DIR, 'valid.csv')

traindf.to_csv(trainpath, index=False)
validdf.to_csv(validpath, index=False)

print('Done')
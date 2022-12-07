from lightgbm import LGBMClassifier
import optuna


'''
import optuna


def get_callback(trial, model_str):
    if model_str == 'lgbm':
            return optuna.integration.LightGBMPruningCallback(trial, "multi_logloss")
'''    

def get_callback(trial, model_str):
    if model_str == 'lgbm':
            return optuna.integration.LightGBMPruningCallback(trial, "multi_logloss")

def get_ml_model(model_str:str,paramenter:dict):
    if model_str == 'lgbm':
        model = LGBMClassifier(**paramenter)
        return model

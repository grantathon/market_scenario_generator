import os
import sys
import argparse
import yaml
from pprint import pprint
# import numpy as np
# import pandas as pd

import market_data


SUPPORTED_DATASOURCES = ['csv']
SUPPORTED_MODELS = ['arima']
SUPPORTED_OPT_METHODS = ['grid search']
SUPPORTED_SCORING_METHODS = ['l2', 'correlation']


def run(datasource,
        data_dir,
        tickers,
        model_name,
        model_window,
        opt_method,
        scoring_method,
        test_time_steps,
        num_scenarios,
        future_time_steps
    ):

    # Make datasource is supported
    if not config['datasource'] in SUPPORTED_DATASOURCES:
        raise ValueError("Datasource in config is not supported.")

    # Make sure data directory exists for CSVs
    if datasource == 'csv' and not os.path.isdir(config['data_dir']):
        raise ValueError("Data directory in config must exist.")

    # Make sure tickers isn't empty
    if not any(config['tickers']):
        raise ValueError("Number of tickers in config cannot be empty.")

    # Make sure model is supported
    if not config['model_name'] in SUPPORTED_MODELS:
        raise ValueError("Model name in config is not supported.")

    # Make sure model window is greater than one
    if not config['model_window'] > 1:
        raise ValueError("Model window in config must be greater than one.")

    # Make sure optimization method is supported
    if not config['optimization_method'] in SUPPORTED_OPT_METHODS:
        raise ValueError("Optimization method in config is not supported.")

    # Make sure scoring method is supported
    if not config['scoring_method'] in SUPPORTED_SCORING_METHODS:
        raise ValueError("Scoring method in config is not supported.")

    # Make sure test time steps is greater than zero
    if not config['test_time_steps'] > 0:
        raise ValueError("Test time steps in config must be greater than zero.")

    # Make sure number of scenarios is greater than zero
    if not config['num_scenarios'] > 0:
        raise ValueError("Number of scenarios in config must be greater than zero.")

    # Make sure future time steps is greater than zero
    if not config['future_time_steps'] > 0:
        raise ValueError("Future ime steps in config must be greater than zero.")

if __name__ == '__main__':
    # Parse arguements
    parser = argparse.ArgumentParser()
    parser.add_argument("config_path", help="the path to the configuration file",
        type=str)
    args = parser.parse_args()

    # Parse configuration file
    with open(args.config_path, 'r') as f:
        config = yaml.load(f)

        datasource = config['datasource'].lower()
        data_dir = config['data_dir']
        tickers = [ticker.lower() for ticker in config['tickers']]
        model_name = config['model_name']
        model_window = config['model_window']
        opt_method = config['optimization_method']
        scoring_method = config['scoring_method']
        test_time_steps = config['test_time_steps']
        num_scenarios = config['num_scenarios']
        future_time_steps = config['future_time_steps']

    # Run market scenario generator
    run(datasource,
        data_dir,
        tickers,
        model_name,
        model_window,
        opt_method,
        scoring_method,
        test_time_steps,
        num_scenarios,
        future_time_steps
    )

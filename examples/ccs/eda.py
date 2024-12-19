"""
Carl's Exploratory Data Analysis.

Here's the strategy:

1. Inspect the data.
    1.1. How many features have a significant number of missing datapoints?
        1.1.1. Should we replace certain values with a mean or median value?
        1.1.2. Or should we drop the feature all together?
    1.2. How many features should we one-hot encode via pd.get_dummies()?
    1.n Save off the pre-processed data as a pickled file for easier data
        retrieval/loading in the future.


"""
import pandas as pd
import numpy as np
from xgboost import XGBRegressor, XGBClassifier

from kaggle.utils.paths import data_dir


if __name__ == '__main__':
    # Load the data
    df = pd.read_csv(data_dir() / 'train.csv')

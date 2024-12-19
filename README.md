# Regression-with-an-Insurance-Dataset
This repo is for participating in [this](https://www.kaggle.com/competitions/playground-series-s4e12/data) Kaggle competition.

*"**Your Goal**: The objectives of this challenge is to predict insurance premiums based on various factors.."*

### Evaluation
Submissions are evaluated using the <ins>Root Mean Squared Logarithmic Error (RMSLE)</ins>.

For each id row in the test set, you must predict the continuous target Premium Amount. The file should contain a header and have the following format:
``` xml
id,Premium Amount
1200000,1102.545
1200001,1102.545
1200002,1102.545
etc.
```

## Setup
This repo uses a Conda environment configured in `environment.yml`. Here are the steps to set these up properly from this repos home folder:
1. Create an new Conda environment `conda env create -f environment.yml`
2. Activate the environment `conda activate Regression-with-an-Insurance-Dataset`

If changes are made to `environment.yml` then update by running `conda env update --file environment.yml --prune`

## Commiting
Please refer to the Conventional Commits specification located [here](https://www.conventionalcommits.org/en/v1.0.0/) for structing your commit messages.

## File Manifest
All models are generated in the `./model/<model-type>` folders. The goal is to try to solve this with many different strategies. Models can predict on the data by running the `./model/model_predict.py` script (after changing the path to the model pickle file). Predictions are automatically formatted for Kaggle and stored in `./submission`.

## TODO 
1. Data Exploration:
    - Perform and EDA on the given dataset
2. Data Pre-Processing & Feature Engineering:
    - Handle missing values via impution or dropping
    - Address class imbalanced with techniques like SMOTE, undersampling, or weighting
    - Create new features if useful
    - Perform encoding on categorical features
    - Bin numerical data
    - Correct mislabeled data
3. Model Development:
    - Build decision tree model in XGBoost to leverage GPU support
    - Build a CatBoost model
    - Build a LightGBM model
    - Build Logistic regression model
    - Build Support Vector Machine model
    - Build Neural Net Model

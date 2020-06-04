import math
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error, mean_absolute_error
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, MinMaxScaler

LABEL = 'NU_NOTA_MT'

def read(filename):
    """Read a csv file and return its content."""
    return pd.read_csv(filename, index_col=0);

def replace_notes(row):
    """Replace NU_NOTA_MT if NU_NOTA_LC is zero."""
    if row['NU_NOTA_LC'] == 0: return 0
    return row['NU_NOTA_MT']

def main():
    df_train = read('train.csv')
    df_validation = read('test.csv')

    feat_columns = [
        'NU_INSCRICAO',
        'NU_NOTA_MT',
        'NU_NOTA_CH',
        'NU_NOTA_CN',
        'NU_NOTA_LC',
        'NU_NOTA_REDACAO',
        'NU_NOTA_COMP1',
        'NU_NOTA_COMP2',
        'NU_NOTA_COMP3',
        'NU_NOTA_COMP4',
        'NU_NOTA_COMP5',
    ]

    df_train = df_train.loc[:, feat_columns]

    # Replace missing data with 0
    df_train.fillna(value=0, inplace=True)
    df_validation.fillna(value=0, inplace=True)

    # Separate feature from target
    y_data = df_train['NU_NOTA_MT']
    x_data = df_train.drop(['NU_NOTA_MT'], axis=1)

    # Split dataset to train and test
    x_train, x_test, y_train, y_test = train_test_split(x_data, y_data, test_size=0.25)

    insc_train = x_train.loc[:, ['NU_INSCRICAO', 'NU_NOTA_LC']].copy()
    insc_test = x_test.loc[:, ['NU_INSCRICAO', 'NU_NOTA_LC']].copy()

    x_train = x_train.drop(['NU_INSCRICAO'], axis=1)
    x_test = x_test.drop(['NU_INSCRICAO'], axis=1)

    regressor = GradientBoostingRegressor(n_estimators=500, learning_rate=0.01).fit(x_train, y_train)
    y_pred = regressor.predict(x_test)

    df_answer = pd.DataFrame({
        'NU_INSCRICAO': insc_test['NU_INSCRICAO'],
        'NU_NOTA_LC': insc_test['NU_NOTA_LC'],
        'Actual': y_test,
        'NU_NOTA_MT': y_pred.clip(0)
    })

    df_answer['NU_NOTA_MT'] = df_answer.apply(replace_notes, axis=1)

    print(mean_absolute_error(y_test, df_answer['NU_NOTA_MT']))
    print(df_answer.drop(['NU_NOTA_LC'], axis=1).head(25))


if __name__ == '__main__':
    # pd.set_option('display.max_columns', 35)
    main()

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, MinMaxScaler

LABEL = 'NU_NOTA_MT'

def read(filename):
    """Read a csv file and return its content."""
    return pd.read_csv(filename, index_col=0);

def main():
    df_train = read('train.csv')
    df_validation = read('test.csv')

    # Remove columns in df_train that are not in df_validation
    drop_columns = [column for column in df_train.columns if column not in df_validation.columns]
    drop_columns.remove(LABEL)  # Except for NU_NOTA_MT

    for column in df_validation.columns:
        # Remove columns that have more null values over non-null on test dataset
        if df_validation[column].isnull().sum() >= df_validation[column].notnull().sum():
            drop_columns.append(column)

    # Remove some other irrelevant data
    drop_columns.extend(['SG_UF_RESIDENCIA', 'CO_UF_RESIDENCIA', 'CO_PROVA_CN',
                         'CO_PROVA_CH', 'IN_SABATISTA', 'CO_PROVA_LC',
                         'CO_PROVA_MT', 'IN_CEGUEIRA', 'IN_DISLEXIA',
                         'IN_DISCALCULIA', 'IN_IDOSO', 'IN_BAIXA_VISAO',
                         'IN_GESTANTE', 'IN_SURDEZ', 'TP_PRESENCA_CN',
                         'TP_PRESENCA_CH', 'TP_PRESENCA_LC', 'NU_NOTA_COMP1',
                         'NU_NOTA_COMP2', 'NU_NOTA_COMP3', 'NU_NOTA_COMP4',
                         'NU_NOTA_COMP5'])

    drop_columns = list(set(drop_columns))
    df_train = df_train.drop(columns=drop_columns)  # Drop columns

    # Create a dictionary containing mapping numbers for categorical features
    question_mapping = {chr(i+64): i for i in range(1, 18)}

    # Create a dictionary for the replacements
    nominal_att = ['Q001', 'Q002', 'Q006', 'Q024', 'Q025', 'Q026', 'Q047']
    question_mapping = {att: question_mapping for att in nominal_att}

    # Add numeric values for 'TP_SEXO'
    question_mapping['TP_SEXO'] = {'F': 1, 'M': 2}

    # Replace nominal by numeric values
    df_train.replace(question_mapping, inplace=True)
    df_validation.replace(question_mapping, inplace=True)

    # Replace missing data with 0
    df_train.fillna(value=0, inplace=True)
    df_validation.fillna(value=0, inplace=True)

    # Separate feature from target
    feat_columns = list(set(df_train.columns) - set([LABEL]))
    x_data = df_train[feat_columns].copy()
    y_data = df_train[LABEL].copy()

    # Split dataset to train and test
    x_train, x_test, y_train, y_test = train_test_split(x_data, y_data, test_size=0.2)

    # Scale features
    scale_columns = ['NU_NOTA_CH', 'NU_NOTA_CN', 'NU_NOTA_LC', 'NU_NOTA_REDACAO']
    x_train[scale_columns] = MinMaxScaler().fit_transform(x_train[scale_columns].values)
    y_train = pd.Series(MinMaxScaler().fit_transform(y_train.values.reshape(-1,1)))

    regressor = LinearRegression().fit(x_train, y_train)
    y_pred = regressor.predict(x_test)
    # print(y_pred)
    # print(y_test.head())

    # df_coeff = pd.DataFrame(regressor.coef_, x_train.columns, columns=['Coefficient'])
    # print(df_coeff.sort_values(by='Coefficient', ascending=False))
    #
    # df = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
    # print(df.head(25))


    # # print(df_train.head())
    # corrmat = df_train.corr()
    # print(corrmat[LABEL].sort_values(ascending=False))

if __name__ == '__main__':
    pd.set_option('display.max_columns', 35)
    main()

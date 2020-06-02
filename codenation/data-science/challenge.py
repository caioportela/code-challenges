import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def read(filename):
    """
    Reads a csv file and return its content
    """
    return pd.read_csv(filename, index_col=0);

def main():
    df_train = read('train.csv')
    df_test = read('test.csv')

    LABEL = 'NU_NOTA_MT'

    # Remove columns in df_train that are not in df_test
    drop_columns = [column for column in df_train.columns if column not in df_test.columns]
    drop_columns.remove(LABEL)  # Except for NU_NOTA_MT

    for column in df_test.columns:
        # Remove columns that have more null values over non-null on dataset
        if df_test[column].isnull().sum() >= df_test[column].notnull().sum():
            drop_columns.append(column)

    # Remove some other irrelevant data
    drop_columns.extend(['SG_UF_RESIDENCIA', 'CO_PROVA_CN', 'CO_PROVA_CH',
                         'CO_PROVA_LC', 'CO_PROVA_MT', 'IN_CEGUEIRA', 'IN_DISLEXIA',
                         'IN_DISCALCULIA', 'IN_IDOSO', 'IN_BAIXA_VISAO',
                         'IN_GESTANTE', 'IN_SURDEZ', 'TP_PRESENCA_CN',
                         'TP_PRESENCA_CH', 'TP_PRESENCA_LC'])

    drop_columns = list(set(drop_columns))
    df_train = df_train.drop(columns=drop_columns)  # Drop columns

    # Create a dictionary containing mapping numbers for categorical features
    question_mapping = {chr(i+64): i for i in range(1, 18)}
    question_mapping[np.nan] = 0

    # Create a dictionary for the replacements
    nominal_att = ['Q001', 'Q002', 'Q006', 'Q024', 'Q025', 'Q026', 'Q047']
    question_mapping = {att: question_mapping for att in nominal_att}

    # Add numeric values for 'TP_SEXO'
    question_mapping['TP_SEXO'] = {'F': 1, 'M': 2}

    # Replace nominal by numeric values
    df_train.replace(question_mapping, inplace=True)
    df_test.replace(question_mapping, inplace=True)

    # Drop rows with missing 'NU_NOTA_MT' data
    df_train.dropna(subset=[LABEL], inplace=True)

    # Replace missing 'NU_NOTA_CH' and 'NU_NOTA_CN' with zero
    df_train.fillna(value=0, inplace=True)

    # corrmat = df_train.corr()
    # print(corrmat[LABEL].sort_values(ascending=False))

    # print(df_train.groupby('CO_UF_RESIDENCIA')['CO_UF_RESIDENCIA'].count())

    # for column in df_train.columns:
    #     print('\n', df_train.groupby(column)[column].count(), df_test.groupby(column)[column].count())

    # total = df_train.isnull().sum().sort_values(ascending=False)
    # percent = (df_train.isnull().sum() / df_train.isnull().count()).sort_values(ascending=False)
    #
    # missing_data = pd.concat([total, percent], axis=1, keys=['Total', 'Percent'])
    # print(missing_data.head())

if __name__ == '__main__':
    pd.set_option('display.max_columns', 35)
    main()

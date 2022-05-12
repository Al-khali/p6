import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def exploration(df):
    print('échontillon  \n')
    print(df.head(5))
    print('\n')
    print('taille du dataframe :\n')
    print(df.shape)
    print('\n')
    # Noms des colonnes, null-count, types d'objets
    print(df.info())

    print('\n')
    print('description du dataset: \n')
    print(df.describe(include='all'))

def NaN_percent(df, column_name):
    row_count = df[column_name].shape[0]
    empty_values = row_count - df[column_name].count()
    return (100.0*empty_values)/row_count

def compare_keys(variable, df1, df1_name, df2, df2_name):
    df1_keys = pd.DataFrame(df1[variable].unique()) # Projection de df1 sur la variable
    df2_keys = pd.DataFrame(df2[variable].unique()) # Projection de df2 sur la variable

    keys_1 = df1_keys.merge( # Clés de df2 non présentes dans df1
        df2_keys, how='outer', indicator=True).loc[lambda x : x['_merge']=='right_only']

    print('Clés de', df2_name, 'non présentes dans', df1_name + ' : ', len(keys_1))
    keys_2 = df2_keys.merge(  # Clés de df1 non présentes dans df2

    df1_keys, how='outer', indicator=True).loc[lambda x : x['_merge']=='right_only']
    print('Clés de', df1_name, 'non présentes dans', df2_name + ' : ', len(keys_2))

def check_doublons(df):
    print(len(df)-len(df.drop_duplicates()), 'doublons')

def lorenz(variable, title):
    X = variable.values
    X = np.sort(X)

    # Indice de Gini
    def gini(array):
        array
        sorted_array = array.copy()
        sorted_array.sort()
        n = array.size
        coef_ = 2. / n
        const_ = (n + 1.) / n
        weighted_sum = sum([(i+1)*yi for i, yi in enumerate(sorted_array)])
        return coef_*weighted_sum/(sorted_array.sum()) - const_
    print('Incide de Gini :', gini(X))

    # Courbe de Lorenz
    X_lorenz = X.cumsum() / X.sum()
    X_lorenz = np.insert(X_lorenz, 0, 0)
    # X_lorenz[0], X_lorenz[-1]
    y = np.arange(X_lorenz.size)/(X_lorenz.size-1)
    lorenz = pd.DataFrame()
    lorenz['X'] = pd.Series(X_lorenz)
    lorenz['Y'] = pd.Series(y)
    sns.scatterplot(data=lorenz, x='Y', y='X', marker='x')

    # Diagonale
    a = np.arange(0,1,.01)
    x = a
    y = a

    # Graphique
    sns.lineplot(x=x,y=y)
    plt.xlim([0,1])
    plt.ylim([0,1])
    plt.title(title)
    plt.show()

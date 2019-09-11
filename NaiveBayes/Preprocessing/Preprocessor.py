##############################################
#Kevin Browder, Nathan Stouffer, Andy Kirby, Eric Kempf
#Program for importing data from CSV
#
#
#############################################
import pandas as pd
import numpy as np
from random import choice      
global runs


class data:
    def __init__(self, classloc, missing, binning, filename):
        df = pd.read_csv("..\\DataFiles\\" + filename + ".data", header = None)
        sets = []
        bins = []
        a = 0
        i = 0
        while(i < len(df)):
            sets.append(a)
            a += 1
            if(a >= 10):
                a = 0
            i += 1
            
        df.rename(columns={classloc:'Class'}, inplace=True)
        cols_to_order = ['Class',]
        new_columns = cols_to_order + (df.columns.drop(cols_to_order).tolist())
        df = df[new_columns]
        df = df.sample(frac=1).reset_index(drop=True)
        fixedcolumns = ['Class']
        for i in range(len(df.columns)-1):
            fixedcolumns.append(i)
        df.columns = fixedcolumns
        df.insert(1, "Sets", sets)

        if missing:
            df = df.replace(to_replace ='?', value = choice(['1', '0']))
            df = df.replace(to_replace ='y', value = '1')
            df = df.replace(to_replace = 'n', value = '0')

        if binning:
            for i in range(len(df.columns)-2):
                df[i] = pd.qcut(df[i], 5, labels=False, duplicates='drop')
                bins.append('5')
        else:
            for i in range(len(df.columns)-2):
                bins.append(str(int(df[i].max()) + 1))  # ANDI added 1 here (so that it is values 0-max)

        header = str(df['Class'].nunique()) + "," + str(len(df.columns)-2) + "," + str(len(df)) + '\n' # ANDI CHANGED IT TO col - 2 to fix
        classes = (df.Class.unique())
        for i in range(len(classes)):
            df['Class'] = df['Class'].replace(classes[i], i)  # KEVIN WHY U PUT i + 100 here?
        template = header + '*,*,' + ','.join(map(str, bins)) + "\n" + ','.join(map(str, classes)) + "\n"
        with open('Datafiles\\' + filename + '.csv', 'w') as fp:
            fp.write(template)
            fp.write((df.to_csv(index=False, header = False)))

glass = data(10, False, True, "glass")
housevotes = data(0, True, False, "house-votes-84")
iris = data(4, False, True, "iris")
soybean = data(35, False, False, "soybean-small")
wdbc = data(1, False, True, "wdbc")
        
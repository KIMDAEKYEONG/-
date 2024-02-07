import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import warnings
warnings.filterwarnings("ignore")

class eta:
    def __init__(self, df, col_name):
        self.df = df
        self.col_name = col_name


    def Nominal(self):
        col_value = self.df[self.col_name].unique()
        col_value.sort()

        # Exited == 1
        df1_in_col_rate = []
        df1_col_rate = []

        # Exited == 0
        df0_in_col_rate = []
        df0_col_rate = []

        #계산
        for index, value in enumerate(col_value):
            df_value = self.df[self.df[self.col_name] == value]


            df1_in_col_rate.append(round(len(df_value[df_value['Exited'] == 1]) /
                                              len(df_value) * 100, 3))

            df1_col_rate.append(round(len(df_value[df_value['Exited'] == 1]) /
                                           len(self.df[self.df['Exited'] == 1]) * 100, 3))


            df0_in_col_rate.append(round(len(df_value[df_value['Exited'] == 0]) /
                                              len(df_value) * 100, 3))

            df0_col_rate.append(round(len(df_value[df_value['Exited'] == 0]) /
                                           len(self.df[self.df['Exited'] == 0]) * 100, 3))

            print('{} 이탈자 수 / {} 수 : {}'.format(value, value, df1_in_col_rate[index]))
            print('{} 이탈자 수 / 전체 이탈자 : {}\n'.format(value, df1_col_rate[index]))

            print('{} 유지자 수 / {} 수 : {}'.format(value, value, df0_in_col_rate[index]))
            print('{} 유지자 수 / 전체 유지자 : {}\n'.format(value, df0_col_rate[index]))
            print('******************************************\n')

        return df0_col_rate, df0_in_col_rate, df1_col_rate, df1_in_col_rate

    # for으로 수정 예정
    def Discrete(self):
        quantiles = (0.25, 0.50, 0.75)

        # 25%, 50%, 75% 기준
        criterions = []
        for i in quantiles:
            criterions.append(int(self.df[self.col_name].quantile(i)))

        criterions_df = []
        # 25%, 50%, 75%
        for index in range(len(criterions)):
            criterions_df.append(self.df[self.df[self.col_name] < criterions[index]])
            criterions_df.append(self.df[self.df[self.col_name] >= criterions[index]])

        rate = []
        rate_1_low = 0
        rate_1_high = 0
        rate_0_low = 0
        rate_0_high = 0

        # 25%, 50%, 75% 비율 계산
        for index, value in enumerate(criterions_df):
            if index % 2 == 0:
                rate_1_low = round(len(value[value['Exited'] == 1]) / len(value) * 100, 3)
                rate_0_low = round(len(value[value['Exited'] == 0]) / len(value) * 100, 3)
                rate.append([rate_1_low, rate_0_low])
                print(index)
            else:
                rate_1_high = round(len(value[value['Exited'] == 1]) / len(self.df[self.df['Exited'] == 1]) * 100, 3)
                rate_0_high = round(len(value[value['Exited'] == 0]) / len(self.df[self.df['Exited'] == 0]) * 100, 3)
                rate.append([rate_1_high, rate_0_high])
                print(index)

        print(rate)



train = pd.read_csv('C:/Users/hyun2/PycharmProjects/pythonProject/datasets/train.csv')

geography = eta(train, 'Geography')
geography.Nominal()

creditscore = eta(train, 'CreditScore')
creditscore.Discrete()

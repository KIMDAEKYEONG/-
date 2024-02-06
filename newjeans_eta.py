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
        #col_value = col_value.sort()

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

    def Discrete(self):
        # mean Exited == 1
        df1_mean_low_rate = 0
        df1_mean_high_rate = 0
        # mean Exited == 0
        df0_mean_low_rate = 0
        df0_mean_high_rate = 0

        # 25% Exited == 1
        df1_25_low_rate = 0
        df1_25_high_rate = 0
        # 25%  Exited == 0
        df0_25_low_rate = 0
        df0_25_high_rate = 0

        # 50% Exited == 1
        df1_50_low_rate = 0
        df1_50_high_rate = 0
        # 50%  Exited == 0
        df0_50_low_rate = 0
        df0_50_high_rate = 0

        # 75%  Exited == 1
        df1_75_low_rate = 0
        df1_75_high_rate = 0
        # 75%  Exited == 0
        df0_75_low_rate = 0
        df0_75_high_rate = 0


        df_mean = int(self.df[self.col_name].mean())
        df_25 = int(self.df[self.col_name].quantile(0.25))
        df_50 = int(self.df[self.col_name].quantile(0.50))
        df_75 = int(self.df[self.col_name].quantile(0.75))


        # 평균
        df_mean_low = self.df[self.df[self.col_name] < df_mean]
        df_mean_high = self.df[self.df[self.col_name] >= df_mean]

        # 하위 25%
        df_25_low = self.df[self.df[self.col_name] < df_25]
        df_25_high = self.df[self.df[self.col_name] >= df_25]

        # 하위 50%
        df_50_low = self.df[self.df[self.col_name] < df_50]
        df_50_high = self.df[self.df[self.col_name] >= df_50]

        # 하위 75%
        df_75_low = self.df[self.df[self.col_name] < df_75]
        df_75_high = self.df[self.df[self.col_name] >= df_75]

        # 평균 비율 계산
        # 이탈
        # Creditscore 평균 미만 이탈자 수 / Creditscore 평균 미만 수
        df1_mean_low_rate = round(len(df_mean_low[df_mean_low['Exited'] == 1]) /
                                         len(df_mean_low) * 100, 3)

        # Creditscore 평균 이상 이탈자 수 / 전체 이탈자 수
        df1_mean_high_rate = round(len(df_mean_high[df_mean_high['Exited'] == 1]) /
                                          len(self.df[self.df['Exited'] == 1]) * 100, 3)

        # 유지
        # Creditscore 평균 미만 유지자 수 / 평균 미만 수
        df0_mean_low_rate = round(len(df_mean_low[df_mean_low['Exited'] == 0]) /
                                         len(df_mean_low) * 100, 3)

        # Creditscore 평균 이상 유지자 수 / 전체 유지자 수
        df0_mean_high_rate = round(len(df_mean_high[df_mean_high['Exited'] == 0]) /
                                          len(self.df[self.df['Exited'] == 0]) * 100, 3)

        # 25% 비율 계산
        # 이탈
        # Creditscore 평균 미만 이탈자 수 / Creditscore 평균 미만 수
        df1_25_low_rate = round(len(df_25_low[df_25_low['Exited'] == 1]) /
                                       len(df_25_low) * 100, 3)

        # Creditscore 평균 이상 이탈자 수 / 전체 이탈자 수
        df1_25_high_rate = round(len(df_25_high[df_25_high['Exited'] == 1]) /
                                        len(self.df[self.df['Exited'] == 1]) * 100, 3)

        # 유지
        # Creditscore 평균 미만 유지자 수 / 평균 미만 수
        df0_25_low_rate = round(len(df_25_low[df_25_low['Exited'] == 0]) /
                                       len(df_25_low) * 100, 3)

        # Creditscore 평균 이상 유지자 수 / 전체 유지자 수
        df0_25_high_rate = round(len(df_25_high[df_25_high['Exited'] == 0]) /
                                        len(self.df[self.df['Exited'] == 0]) * 100, 3)


        # 50% 비율 계산
        # 이탈
        # Creditscore 평균 미만 이탈자 수 / Creditscore 평균 미만 수
        df1_50_low_rate = round(len(df_50_low[df_50_low['Exited'] == 1]) /
                                       len(df_50_low) * 100, 3)

        # Creditscore 평균 이상 이탈자 수 / 전체 이탈자 수
        df1_50_high_rate = round(len(df_50_high[df_mean_high['Exited'] == 1]) /
                                        len(self.df[self.df['Exited'] == 1]) * 100, 3)

        # 유지
        # Creditscore 평균 미만 유지자 수 / 평균 미만 수
        df0_50_low_rate = round(len(df_mean_low[df_50_low['Exited'] == 0]) /
                                       len(df_50_low) * 100, 3)

        # Creditscore 평균 이상 유지자 수 / 전체 유지자 수
        df0_50_high_rate = round(len(df_50_high[df_50_high['Exited'] == 0]) /
                                        len(self.df[self.df['Exited'] == 0]) * 100, 3)


        # 75% 비율 계산
        # 이탈
        # Creditscore 평균 미만 이탈자 수 / Creditscore 평균 미만 수
        df1_75_low_rate = round(len(df_75_low[df_75_low['Exited'] == 1]) /
                                len(df_75_low) * 100, 3)

        # Creditscore 평균 이상 이탈자 수 / 전체 이탈자 수
        df1_75_high_rate = round(len(df_75_high[df_mean_high['Exited'] == 1]) /
                                 len(self.df[self.df['Exited'] == 1]) * 100, 3)

        # 유지
        # Creditscore 평균 미만 유지자 수 / 평균 미만 수
        df0_75_low_rate = round(len(df_mean_low[df_75_low['Exited'] == 0]) /
                                len(df_75_low) * 100, 3)

        # Creditscore 평균 이상 유지자 수 / 전체 유지자 수
        df0_75_high_rate = round(len(df_75_high[df_75_high['Exited'] == 0]) /
                                 len(self.df[self.df['Exited'] == 0]) * 100, 3)

        # 결과 출력
        print(df1_mean_low_rate)
        print(df1_mean_high_rate)
        print(df0_mean_low_rate)
        print(df0_mean_high_rate)

        print(df1_25_low_rate)
        print(df1_25_high_rate)
        print(df0_25_low_rate)
        print(df0_25_high_rate)

        return  (df1_mean_low_rate, df1_mean_high_rate, df0_mean_low_rate, df0_mean_high_rate,
                 df1_25_low_rate, df1_25_high_rate, df0_25_low_rate, df0_25_high_rate,
                 df1_50_low_rate, df1_50_high_rate, df0_50_low_rate, df0_50_high_rate,
                 df1_75_low_rate, df1_75_high_rate, df0_75_low_rate, df0_75_high_rate)



train = pd.read_csv('C:/Users/hyun2/PycharmProjects/pythonProject/datasets/train.csv')

geography = eta(train, 'Geography')
geography.Nominal()

creditscore = eta(train, 'CreditScore')
creditscore.Discrete()

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class eta:
    def __init__(self, dataframe, column_name):
        self.dataframe = dataframe
        self.column_name = column_name
        self.column_value = self.dataframe[self.column_name].unique()

    def Nominal(self):
        # Exited == 1
        dataframe1_in_column_rate = []
        dataframe1_column_rate = []

        # Exited == 0
        dataframe0_in_column_rate = []
        dataframe0_column_rate = []

        for index, value in enumerate(self.column_value):
            dataframe_value = self.dataframe[self.dataframe[self.column_name] == value]


            dataframe1_in_column_rate.append(
                round(len(dataframe_value[dataframe_value['Exited'] == 1]) / len(dataframe_value) * 100, 3))

            dataframe1_column_rate.append(
                round(len(dataframe_value[dataframe_value['Exited'] == 1]) / len(self.dataframe[self.dataframe['Exited'] == 1]) * 100, 3))


            dataframe0_in_column_rate.append(
                round(len(dataframe_value[dataframe_value['Exited'] == 0]) / len(dataframe_value) * 100, 3))

            dataframe0_column_rate.append(
                round(len(dataframe_value[dataframe_value['Exited'] == 0]) / len(self.dataframe[self.dataframe['Exited'] == 0]) * 100, 3))

            print('{} 이탈자 수 / {} 수 : {}'.format(value, value, dataframe1_in_column_rate[index]))
            print('{} 이탈자 수 / 전체 이탈자 : {}\n'.format(value, dataframe1_column_rate[index]))

            print('{} 유지자 수 / {} 수 : {}'.format(value, value, dataframe0_in_column_rate[index]))
            print('{} 유지자 수 / 전체 유지자 : {}\n'.format(value, dataframe0_column_rate[index]))
            print('******************************************\n')

        return dataframe0_column_rate, dataframe0_in_column_rate, dataframe1_column_rate, dataframe1_in_column_rate

    # def Discrete(self):


train = pd.read_csv('C:/Users/hyun2/PycharmProjects/pythonProject/datasets/train.csv')

products = eta(train, 'NumOfProducts')

products.Nominal()
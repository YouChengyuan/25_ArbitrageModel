import efinance as ef
import time
from datetime import datetime
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy import stats
from sklearn.preprocessing import StandardScaler

class Stock(object):
    def __init__(self, stock_code: int|str):
        self.stock_code = str(stock_code)
    
    def get_freq_data(self, freq: int, beg: int, end: int):
        ''' 
        返回股价数据dataFrame

        freq:
            1 : 1分钟，只有最近一天的数据
            5 : 5 分钟
            15 : 15 分钟
            30 : 30 分钟
            60 : 60 分钟
            101 : 日
            102 : 周
            103 : 月
        
        beg/end:
            例如 20240101表示2024年1月1日

            '''
        df_res= ef.stock.get_quote_history(
                self.stock_code,klt=freq,beg=str(beg), end=str(end)
                )
        return df_res

    def get_curr_data(self, freq):
        '''获取实时1min数据'''
        df = ef.stock.get_quote_history(self.stock_code,klt=freq)
        latest_data = df.tail(1)
        return latest_data
    
    def show_price_mean_function(self, freq: int, beg: int, end: int):
        df = self.get_freq_data(freq=freq, beg= beg, end= end)
        ma5 = df['收盘'].rolling(window=5).mean()
        ma10 = df['收盘'].rolling(window=10).mean()
        ma20 = df['收盘'].rolling(window=20).mean()
        
        # 计算线性回归
        slope, intercept, r_value, p_value, std_err = stats.linregress(range(len(ma10.dropna())), ma10.dropna())
        
        # 打印线性回归结果
        if p_value < 0.01 and slope > 0 and r_value**2 > 0.88:
            print(f"斜率: {slope}")
            print(f"截距: {intercept}")
            print(f"R²: {r_value**2}")
        else:
            print('非线性上升')
        
        regress_line = [slope * (x-9) + intercept for x in range(len(ma20))]
        # 绘制结果
        plt.scatter(range(len(df['收盘'])), df['收盘'], label='price_mean')
        # plt.plot(range(len(pma)), pma, label='pma')
        plt.plot(range(len(ma5)), ma5, label= 'ma5')
        plt.plot(range(len(ma10)), ma10, label= 'ma10')
        # plt.plot(range(len(ma20)), ma20, label= 'ma20')
        plt.plot(range(len(regress_line)), regress_line, label= 'reg_line')
        plt.legend()
        plt.title('price_mean_function')
        plt.show()

    def show_price_increament(self, freq: int, beg: int, end: int):
        df = self.get_freq_data(freq=freq, beg= beg, end= end)
        price_increament = df['涨跌额']
        plt.plot(range(len(price_increament)), price_increament)
        plt.title('price_increament')
        plt.show()

    def show_price_increament_rate(self, freq: int, beg: int, end: int):
        df = self.get_freq_data(freq=freq, beg= beg, end= end)
        price_increament = df['涨跌幅']
        plt.plot(range(len(price_increament)), price_increament)
        plt.title('price_increament_rate')
        plt.show()

    def show_VOL(self, freq: int, beg: int, end: int):
        df = self.get_freq_data(freq=freq, beg= beg, end= end)
        VOL = df['成交量']
        plt.plot(range(len(VOL)), VOL)
        plt.title('VOL')
        plt.show()

    def show_turnover(self, freq: int, beg: int, end: int):
        df = self.get_freq_data(freq=freq, beg= beg, end= end)
        turnover = df['成交额']
        plt.plot(range(len(turnover)), turnover)
        plt.title('turnover')
        plt.show()
        
    def show_macd(self, freq: int, beg: int, end: int):
        df = self.get_freq_data(freq=freq, beg= beg, end= end)
        df['EMA12'] = df['收盘'].ewm(span=12, adjust=False).mean()
        df['EMA26'] = df['收盘'].ewm(span=26, adjust=False).mean()

        # 计算MACD线
        df['MACD'] = df['EMA12'] - df['EMA26']

        # 计算信号线
        df['Signal_Line'] = df['MACD'].ewm(span=9, adjust=False).mean()

        # 计算MACD柱线
        df['Histogram'] = df['MACD'] - df['Signal_Line']

        plt.plot(range(len(df['Histogram'])), df['Histogram'])
        plt.plot(range(len(df['Histogram'])), [0]*len(df['Histogram']))
        plt.plot(range(len(df['MACD'])), df['MACD'])
        plt.show()

    def show_fast_macd(self, freq: int, beg: int, end: int):
        df = self.get_freq_data(freq=freq, beg= beg, end= end)
        df['EMA12'] = df['收盘'].ewm(span=5, adjust=False).mean()
        df['EMA26'] = df['收盘'].ewm(span=10, adjust=False).mean()

        # 计算MACD线
        df['MACD'] = df['EMA12'] - df['EMA26']

        # 计算信号线
        df['Signal_Line'] = df['MACD'].ewm(span=9, adjust=False).mean()

        # 计算MACD柱线
        df['Histogram'] = df['MACD'] - df['Signal_Line']

        plt.plot(range(len(df['Histogram'])), df['Histogram'])
        plt.plot(range(len(df['Histogram'])), [0]*len(df['Histogram']))
        plt.plot(range(len(df['MACD'])), df['MACD'])
        plt.show()

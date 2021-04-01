import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns

import platform

from matplotlib import font_manager, rc
plt.rcParams['axes.unicode_minus'] = False

if platform.system() == 'Darwin':
    rc('font', family='AppleGothic')
elif platform.system() == 'Windows':
    path = "c:/Windows/Fonts/malgun.ttf"
    font_name = font_manager.FontProperties(fname=path).get_name()
    rc('font', family=font_name)
else:
    print('Unknown system... sorry~~~~')

subway = pd.read_csv('subway.csv',encoding='cp949',  thousands=',')

subway.head()

subway=subway.set_index('일자')

subway.head()

subway.info()

subway.isna().sum()

slot_data

slot_data = subway.iloc[:,2:].sum()

plt.figure(figsize=(10,10))
explode = (0, 0, 0, 0.1 ,0, 0, 0, 0,0, 0, 0, 0,0, 0, 0, 0,0, 0, 0, 0,0, 0, 0, 0)
plt.pie(slot_data, labels = slot_data.index ,explode = explode , autopct='%1.1f%%', startangle = 90, counterclock = False)
plt.legend(slot_data,
           loc="best",
          title ="시간대 별 이용객 수")

plt.show()

plt.figure(figsize = (12,7))
plt.plot(slot_data, '.-')
plt.title('시간대 별 총 이용 승객수')
plt.xlabel('시간대')
plt.ylabel('승객 수')
plt.show()


ride_subway=subway.loc[subway['구분']=='승차']

ride_subway=ride_subway.drop(['구분','계'], axis=1)

ride_subway.head()

ride_subway=ride_subway.sum()

ride_subway.head()

plt.figure(figsize = (12,7))
plt.plot(ride_subway, '.-')
plt.title('시간대 별 승차 승객 수')
plt.xlabel('시간대')
plt.ylabel('승객 수')
plt.show()



takeoff_subway=subway.loc[subway['구분']=='하차']

takeoff_subway=takeoff_subway.drop(['구분','계'], axis=1)

takeoff_subway= takeoff_subway.sum()

takeoff_subway

plt.figure(figsize = (12,7))
plt.plot(takeoff_subway, '.-')
plt.title('시간대 별 하차 승객 수')
plt.xlabel('시간대')
plt.ylabel('승객 수')
plt.show()


plt.figure(figsize = (12,7))
plt.plot(ride_subway, '.-', label='승차객 수')
plt.plot(takeoff_subway, '.-', label='하차객 수')
plt.title('시간대 별 승차 및 하차 승객 수')
plt.xlabel('시간대')
plt.ylabel('승객 수')
plt.legend()
plt.show()
import csv
from matplotlib import pyplot as plt

from datetime import datetime

filename_1 = 'death_valley_2014.csv'
with open(filename_1) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates_1, highs_1, lows_1 = [], [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], '%Y-%m-%d')
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(current_date, 'missing data')
        else:
            dates_1.append(current_date)
            highs_1.append(high)
            lows_1.append(low)

filename_2 = 'sitka_weather_2014.csv'
with open(filename_2) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates_2, highs_2, lows_2 = [], [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], '%Y-%m-%d')
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(current_date, 'missing data')
        else:
            dates_2.append(current_date)
            highs_2.append(high)
            lows_2.append(low)

# 根据数据绘制图形
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates_1, highs_1, c='red', alpha=0.5)
plt.plot(dates_1, lows_1, c='red', alpha=0.5)
plt.fill_between(dates_1, highs_1, lows_1, facecolor='blue', alpha=0.1)

plt.plot(dates_2, highs_2, c='blue', alpha=0.5)
plt.plot(dates_2, lows_2, c='blue', alpha=0.5)
plt.fill_between(dates_2, highs_2, lows_2, facecolor='red', alpha=0.1)

#  设置图形的格式
plt.title('Daily high and low temperatures - 2014\nDeath Valley, CA', fontsize=20)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel('Temperture (F)', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
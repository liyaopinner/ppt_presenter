from discuz_statistic.data import data1, data2

for key, value in data1.items():
    if data2[key] != value:
        print(key, data2[key], data2[key]-value)
# 隨機模組
import random
# 隨機選取
# data=random.sample([1,4,5,6,7,3], 4)
# 隨機調換順序(就是洗牌的概念)

# data=[1,5,8,20]
# random.shuffle(data)

# 隨機取得亂數
# data=random.uniform(60,100) # 60 ~ 100 之間的隨機亂數

# 取得常態分配亂數
# 平均數 100，標準差 10， 得到的資料「多數」在 90 ~ 110 之間
# data=random.normalvariate(100,10)
# 平均數 0，標準差 5， 得到的資料「多數」在 -5 ~ 5 之間
# data=random.normalvariate(0,5)
# print(data)

# 統計模組
# import statistics as stat
# data=stat.stdev([1,5,7,3,4,8,10])
# print(data)
# 平均數、中位數、標準差、常態分配、
# 載入 pandas 模組
from statistics import median
from traceback import print_tb
import pandas as pd
# 建立 Series
# data=pd.Series([20,10,15])
# 基本 Series 操作
# print(data)
# print("Max",data.max())
# print("Median",data.median())
# data=data*2
# print(data)
# data=data==20
# print(data)
# 建立 Dataframe
data=pd.DataFrame({
    "name":["Amy","Bob","John","Ian"],
    "salary":[30000,50000,40000,45000]
})
# 基本 Dataframe 操作
# print(data)
# 取得特定欄位
# print(data["salary"])
# 取得特定的列
print(data)
print("==========")
print(data.iloc[1]) # 印出第二列
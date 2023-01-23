# 載入 pandas 模組
import pandas as pd
# 篩選練習 - Series
# data=pd.Series([30,15,20])
# condition=data>18
# print(condition)
# filteredData=data[condition]
# print(filteredData)

# data=pd.Series(["您好","Python","Pandas"])
# condition=data.str.contains("P")
# print(condition)
# filteredData=data[condition]
# print(filteredData)

# 篩選練習 - Dataframe
data=pd.DataFrame({
    "name":["Amy","John","Mike","Ian"],
    "salary":[30000,45000,50000,25000]
})
# print(data)
condition=data["name"]=="Amy"
print(condition)
filteredData=data[condition]
print(filteredData)
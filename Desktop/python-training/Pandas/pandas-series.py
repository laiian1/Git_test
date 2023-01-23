# 載入 pandas 模組
import pandas as pd
# 資料索引
# data=pd.Series([3, 4, 6, 1, 2, -1, -4], index=["a", "b", "c", "d", "e", "f", "g"])
# print(data)

# 觀察資料
# print("資料型態", data.dtype)
# print("資料數量", data.size)
# print("資料索引", data.index)

# 取得資料：根據順序、根據索引
# print(data[2], data[4])
# print(data["f"], data["g"])

# data=pd.Series([3, 4, 6, 1, 2, -1, -4], index=["a", "b", "c", "d", "e", "f", "g"])
# 數字運算：基本、統計、順序
# print("最大值", data.max())
# print("加法總和", data.sum())
# print("乘法總和", data.prod())
# print("平均數", data.mean())
# print("標準差", data.std())
# print("中位數", data.median())
# print("取前3大大數字", data.nlargest(3))
# print("取最小的2個數字", data.nsmallest(2))
data=pd.Series(["您好","Python","Pandas"])
# 字串運算：基本、串接、搜尋、取代
# print(data.str.lower()) 全部變小寫
# print(data.str.len()) 算出每個字串的長度
# print(data.str.cat(sep="-")) 把字串串起來，可以自訂中間串接的符號
# print(data.str.contains("好")) 判斷每個字串是否包含特定字元
print(data.str.replace("您好", "Hello"))
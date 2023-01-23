# 有序可變動的列表list
# grades=[12,60,43,69,73]
# # grades[1:4]=[] # 連續刪除列表中從編號 1 到編號 4 (不包括) 的資料
# length=len(grades) # 取得列表的長度 len(列表資料)
# print(length)
# grades=grades+[12,33]
# print(grades)
# grades[0]=55 # 把55 放到列表中的第一個位置
# print(grades[1:4])
# data=[[3,4,5],[6,7,8]]
# print(data)
# data[0][0:2]=[5,5,5]
# print(data[0])
# 有序不可動的列表 Tuple
data=(3,4,5)
# data[0]=5 # 錯誤: Tuple 的資料不可以變動
print(data[0:2])
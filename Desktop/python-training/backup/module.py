# 載入內建的 sys 模組並取得資訊
# import sys as system
# print(system.platform)
# print(system.maxsize)

# 建立 geometry 模組，載入使用
# import geometry
# result=geometry.distance(1,1,5,5)
# print(result)
# result=geometry.slope(1,2,5,6)
# print(result)

# 調整搜尋模組路徑
import sys
sys.path.append("modules") # 在模組的搜尋路徑中
print(sys.path) # 印出模組搜尋路徑
# import geometry
#print(geometry.distance(1,1,5,5))
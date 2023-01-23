# Point 實體物件的設計：平面上的座標
# class Point:
#     def __init__(self,x ,y):
#         self.x=x
#         self.y=y
# # 建立第一個實體物件
# p1=Point(3,4)
# print(p1.x, p1.y)
# # 建立第二個實體物件
# p2=Point(5,6)
# print(p2.x,p2.y)

# Fullname 實體物件的設計： 分開紀錄姓、名資料的全名
class Fullname:
    def __init__(self,first,last):
        self.first=first
        self.last=last
name1=Fullname("Lai","Cian Yi")
print(name1.first, name1.last)
name2=Fullname("U.J","Lin")
print(name2.first, name2.last)
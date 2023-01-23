# 定義建立生成器函式
# def test():
#     print("階段一")
#     yield 5
#     print("階段二")
#     yield 10
# # 呼叫並回傳生成器
# gen=test()
# # 搭配 for 迴圈中使用
# for d in gen:
#     print(d) # 5

def generaEven(maxNumber):
    number=0
    while number<=maxNumber:
        yield number
        number+=2

evenGenerator=generaEven(16)
for data in evenGenerator:
    print(data)
def add(n1,n2,cb):
   cb(n1+n2)

def handle1(result):
    print("結果是", result)

def handle2(result):
    print("Result of A is", result)

add(3, 4, handle1)
add(5, 6, handle1)
add(2, 9, handle2)




# def test(arg):
#     arg("Hello") # 呼叫回乎函式，帶入參數
# # 定義一個回呼函式
# def handle(da):
#     print(da)

# test(handle)

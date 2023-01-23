# 定義類別、與類別屬性（封裝在類別中的變數與函式）
# 定義一個類別 IO，有兩個屬性 supportSrc 和 read
class IO:
    supportSrc=["console","file"]
    def read(src):
        if src not in IO.supportSrc:
            print("Not supported")
        else:
            print("Read from",src)
# 使用類別
print(IO.supportSrc)
IO.read("file")
IO.read("internet")
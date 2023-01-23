# 猜數字遊戲

secret_num = 77
guess = None
guess_count = 0
guess_limit = 3
out_of_limit = False

while secret_num != guess and not(out_of_limit):
    guess_count += 1
    if guess_count <= guess_limit:
            
        guess = int(input("請輸入數字: "))
        if guess > secret_num:
            print("請輸入更小值")
        elif guess < secret_num:   
            print("請輸入更大值")
    else:
        out_of_limit= True
    
if out_of_limit:
    print("抱歉你輸了")        
else:
    print("恭喜猜對答案")
# 寄送 Email 的程式
# 準備訊息物件設定
import email.message
msg=email.message.EmailMessage()
msg["From"]="ian241607@gmail.com"
msg["To"]="U10809022@go.utaipei.edu.tw"
msg["Subject"]="你好, Ian"
# 寄送存純文字內容
# msg.set_content("測試看看")
# 寄送比較多樣式的內容 (html)
msg.add_alternative("<h3>優惠卷</h3>滿五百送一百喔", subtype="html")
# 連線到 STMP Server, 驗證寄件人身份並發送郵件
import smtplib
# 到網路上搜尋 gmail smtp server 或是 yahoo smtp server
server=smtplib.SMTP_SSL("smtp.gmail.com",465)
server.login("ian241607@gmail.com","iAn241312")
server.send_message(msg)
server.close()
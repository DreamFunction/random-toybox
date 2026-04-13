# Copyright (c) 2026 DreamFunction

import secrets

print("命令：d 执行动作 -n 重复执行n次 q 退出程序")
while True:
    do = input("请输入总数（自动四舍五入）：")
    if do.isdigit():
        total = round(float(do))
        break
    else:
        print("请输入数字。")
        
numlist = []
for i in range(total+1):
    numlist.append(i)

while True:
    do = input("请输入：")
    if do=='':
        print("请输入有效指令。")
        continue
    if do[0]=='d':
        if '-' in do:
            put = []
            for i in range(1,int(do[do.index('-')+1: ])+1):
                put.append(secrets.choice(numlist))
            print(put)
        else:
            print(secrets.choice(numlist))
    elif do=='q':
        break
    else:
        print("请输入有效指令。")

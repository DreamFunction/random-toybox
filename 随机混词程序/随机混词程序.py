# Copyright (c) 2026 DreamFunction

import json
import os
import random

print("欢迎使用本程序！输入mN（如m10）生成长度为N的句子，输入q退出")
while True:
    do = input("本程序将解析同级目录下的“data.json”。请确保JSON数据受信任。确定要解码吗？（y/n）")
    if do=='y':
        break
    elif do=='n':
        quit()
    else:
        continue
if 'data.json' not in os.listdir(os.getcwd()):
    raise FileNotFoundError("找不到“data.json”。")
with open(os.getcwd()+'/data.json') as f:
    data = json.loads(f.read())
while True:
    do = input("请输入：")
    if do=='':
        print("请输入有效指令。")
        continue
    if do[0]=='m':
        if do[1: ].isdigit():
            put = []
            for i in range(round(float(do[1: ]))):
                put.append(random.choice(data))
            print("".join(put))
        else:
            print("请输入有效指令。")
            continue
    elif do=='q':
            break
    else:
        print("请输入有效指令。")
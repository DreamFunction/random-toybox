# Copyright (c) 2026 DreamFunction

import json
import os
import random

print("欢迎使用本程序！输入m生成，输入q退出")
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
    if do=='m':
        put = random.choice(data)
        for i in range(0,len(put)):
            if isinstance(put[i],str):
                pass
            elif isinstance(put[i],list):
                put[i] = random.choice(put[i])
            else:
                raise TypeError("解码“data.json”后的列表内出现了除字符串和列表以外的数据类型")
        put = "".join(put)
        print(put)
    elif do=='q':
            break
    else:
        print("请输入有效指令。")
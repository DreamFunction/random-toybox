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
s = data[0]
v = data[1]
o = data[2]
del data
while True:
    do = input("请输入：")
    if do=='m':
        print(''.join([random.choice(s),random.choice(v),random.choice(o)]))
    elif do =='q':
        break
    else:
        print("请输入有效指令")
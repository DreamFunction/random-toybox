# Copyright (c) 2026 DreamFunction

import os

ENCODE = 'utf-8'

print("欢迎使用！输入q退出")
while True:
    do = input("是从文件（同级目录下“obj.txt”）生成还是从命令界面生成？（文件：f 命令界面：c）")
    if do=='f':
        if 'obj.txt' not in os.listdir(os.getcwd()):
            raise FileNotFoundError("找不到“obj.txt”。")
        with open(os.getcwd()+'/obj.txt') as f:
            content = f.readlines()
        content[-1] = content[-1]+'\n'
        with open(os.getcwd()+'/data.json','w',encoding=ENCODE) as f:
            for i in range(len(content)):
                content[i] = "".join(['"',content[i][ :-1],'"'])
            f.write('['+','.join(content)+']')
        print("生成完毕")
        break
    elif do=='c':
        print("输入e结束")
        data = []
        while True:
            userinput = input("请输入：  ")
            if userinput=='e':
                if len(data)==0:
                    print("并未输入")
                else:
                    with open(os.getcwd()+'/data.json','w',encoding=ENCODE) as f:
                        f.write('['+','.join(data)+']')
                    print("生成完毕")
                    break
            elif userinput=='':
                print("输入不能为空")
            elif userinput=='q':
                if len(data)==0:
                    break
                else:
                    do = input("现在退出将丢失已经输入的数据。确认退出吗？（y/n）")
                    if do=='y':
                        break
            else:
                data.append('"'+userinput+'"')
        break
    elif do=='q':
        break
    else:
        print("请输入有效指令。")
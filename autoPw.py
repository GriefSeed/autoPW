#coding:utf-8
'''
这个脚本用于自动生成12位的随机password，password由大小写字母、数字、特殊字符组成，并记录在
特定的文本里,password必须保证每种字符都至少要有一个，否则重新生成
'''
import random,string

num_str = string.digits
up_str = string.ascii_uppercase
low_str = string.ascii_lowercase
sp_str = '!@#$%^&*()'
all = []

def proPwNoSp():
    all.append(num_str)
    all.append(up_str)
    all.append(low_str)
    pw = ''
    while len(pw) <= 11:
        ele = random.choice(all)
        pw += random.choice(ele)
    return pw

def proPw():
    all.append(num_str)
    all.append(up_str)
    all.append(low_str)
    all.append(sp_str)
    pw = ''
    while len(pw) <= 11:
        ele = random.choice(all)
        pw += random.choice(ele)
    return pw
def checkPw(str, model=1):
    if model == 1:
        num_num, up_num, low_num, sp_num = 0,0,0,0
        for e in str:
            if e in num_str:
                num_num += 1
            if e in up_str:
                up_num += 1
            if e in low_str:
                low_num += 1
            if e in sp_str:
                sp_num += 1
        if num_num >= 1 and up_num >= 1 and low_num >= 1 and sp_num >= 1:
            return True
        return False
    if model == 2:
        num_num, up_num, low_num, sp_num = 0,0,0,0
        for e in str:
            if e in num_str:
                num_num += 1
            if e in up_str:
                up_num += 1
            if e in low_str:
                low_num += 1
        if num_num >= 1 and up_num >= 1 and low_num >= 1:
            return True
        return False
    return False

aim_pw = ''
while 1:
    aim_pw = proPwNoSp()#这里可以改成没有特殊字符的
    if checkPw(aim_pw, 2):#这里选模式，1是有特殊字符的，2是没有特殊字符的
        break
print(aim_pw)
account = input('输入你的注释和账号:')
file = open(r'd:\google_drive\all\My_pw\pwFile.txt', 'a')
file.write('\n'+account+'  password:'+aim_pw)
file.close()

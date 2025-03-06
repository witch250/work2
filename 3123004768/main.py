#import jieba
import jieba.analyse
import os
import math
import Levenshtein
from line_profiler import profile #4.2.0 电脑重启再使用......
#cd
#py -m kernprof -l main.py   
#py -m line_profiler main.py.lprof
import numpy as np
def OpenTxt(txtpath):
    try:
        with open(txtpath,"r",encoding='UTF-8') as txt:
            return(txt.read())
    except FileNotFoundError:
        raise FileNotFoundError("找不到文件")

def WriteTxt(op,path):
    try:
        with open(path,'w',encoding='UTF-8') as f:
            f.write("相似度为%.2f"%op)
    except FileNotFoundError:
        raise FileNotFoundError("找不到文件")
#某种哈希算法,将词语转为64位2进制数字符串，照搬的，在找出处，2010年前含
@profile
def hash(source):
    if source == "":
            return 0
    else:
        #unicode16进制转十进制左移7位
        x = ord(source[0]) << 7
        #print (x)
        m = 1000003
        mask = 2 ** 128 - 1
        for c in source:
            x = ((x * m) ^ ord(c)) & mask
        x ^= len(source)
        if x == -1:
            x = -2
        #转为64位2进制数
        x = bin(x).replace('0b', '').zfill(64)[-64:]
    return str(x)
    
@profile
def SimHash1(txt):
    taglist=jieba.analyse.extract_tags(txt, topK=20, withWeight=True)
    T=[]
    for keyword,weight in taglist:
        weight*=20
        weight=math.ceil(weight)
        #某种哈希算法,将词语转为64位2进制数字符串
        keyword=hash(keyword)
        temp=[]
        #根据64位2进制数字符串和权重构造向量
        for i in keyword:
            if i=='1':
                temp.append(weight)
            else:
                temp.append(-weight)
        T.append(temp)
    #64单位的20维向量合并为1维向量
    list1=np.sum(np.array(T),axis=0)
    if(T==[]):
        return '00'
    #64位二进制simhash
    simhash=''
    for i in list1:
        if i<0:
            simhash+='1'
        else:
            simhash+='0'
    return simhash   

#i=[0,64]10内大概相似,3内认为相似
@profile
def hamming(s1,s2):
    t1='0b'+s1
    t2='0b'+s2
    n=int(t1,2)^int(t2,2)
    i=0
    while n:
        n&=(n-1)
        i+=1
    return i
@profile
def Levenshtein1(txt1,txt2):
    s1=jieba.analyse.extract_tags(txt1, topK=30)
    s2=jieba.analyse.extract_tags(txt2, topK=30)
    #list仅位置不同时会得到完全不同，我猜可以这么改
    s1.sort()
    s2.sort()
    #print(s1)
    #print(s2)
    #比较list,返回小数
    return Levenshtein.ratio(s1,s2)*0.5+Levenshtein.ratio(jieba.analyse.extract_tags(txt1, topK=20),jieba.analyse.extract_tags(txt2, topK=20))*0.5

#关键词交集中元素个数除以并集
@profile
def Jaccard(txt1,txt2):
    s1=jieba.analyse.extract_tags(txt1, topK=30)
    s2=jieba.analyse.extract_tags(txt2, topK=30)
    s1=set(s1)
    s2=set(s2)
    num1=len(s1&s2)
    num2=len(s1|s2)
    if num2==0:
        return 1
    return num1/num2

#main
try:
    #获取路径，更改路径
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    print(os.getcwd())
    path1='./orig.txt'
    path2='./orig_0.8_add.txt'
    path3='./output.txt'
    txt1=OpenTxt(path1)
    txt2=OpenTxt(path2)
    simhash1=SimHash1(txt1)
    simhash2=SimHash1(txt2)
    #print(simhash1)
    #print(simhash2)
    result1=hamming(simhash1,simhash2)
    #print(result1)
    #拿leven拟合的,数据不够多,R=0.7
    result1=0.0004*result1*result1-0.039*result1+1
    if result1<0:
        result1=0
    elif result1>1:
        result=1
    print(result1)
    result2=Levenshtein1(txt1,txt2)
    print(result2)
    result3=Jaccard(txt1,txt2)
    print(result3)
    WriteTxt(result1*0.4+result2*0.3+result3*0.3,path3)
    print("OK")
except FileNotFoundError as e:
    print(e)





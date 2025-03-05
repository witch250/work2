#import jieba
import jieba.analyse
import os
import math
import Levenshtein
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
            f.write("相似度为%.2f"%(op*100)+'%')
    except FileNotFoundError:
        raise FileNotFoundError("找不到文件")

def hash(source):
    if source == "":
            return 0
    else:
        x = ord(source[0]) << 7
        m = 1000003
        mask = 2 ** 128 - 1
        for c in source:
            x = ((x * m) ^ ord(c)) & mask
        x ^= len(source)
        if x == -1:
            x = -2
        x = bin(x).replace('0b', '').zfill(64)[-64:]
    return str(x)
    
    
def SimHash1(txt):
    taglist=jieba.analyse.extract_tags(txt, topK=20, withWeight=True)
    T=[]
    for keyword,weight in taglist:
        weight*=20
        weight=math.ceil(weight)
        keyword=hash(keyword)
        temp=[]
        #64位keyword
        for i in keyword:
            if i=='1':
                temp.append(weight)
            else:
                temp.append(-weight)
        T.append(temp)
    #64单位的20维数组合并为1维数组
    list1=np.sum(np.array(T),axis=0)
    #64位二进制simhash
    simhash=''
    for i in list1:
        if i<0:
            simhash+='1'
        else:
            simhash+='0'
    return simhash   

def hamming(s1,s2):
    t1='0b'+s1
    t2='0b'+s2
    n=int(t1,2)^int(t2,2)
    i=0
    while n:
        n&=(n-1)
        i+=1
    return i

def Levenshtein1(txt1,txt2):
    #return Levenshtein.ratio(jieba.analyse.extract_tags(txt1, topK=20),jieba.analyse.extract_tags(txt2, topK=20))
    s1=jieba.analyse.extract_tags(txt1, topK=30)
    s2=jieba.analyse.extract_tags(txt2, topK=30)
    s1.sort()
    s2.sort()
    print(s1)
    print(s2)
    return Levenshtein.ratio(s1,s2)

try:
    #获取路径，更改路径
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    #print(os.getcwd())
    path1='./orig_0.8_add.txt'
    path2='./orig_0.8_del.txt'
    path3='./output.txt'
    txt1=OpenTxt(path1)
    txt2=OpenTxt(path2)
    simhash1=SimHash1(txt1)
    simhash2=SimHash1(txt2)
    #print(simhash1)
    #print(simhash2)
    result1=hamming(simhash1,simhash2)
    #拿leven拟合的
    result1=-0.0276*result1+0.928
    print(result1)
    result2=Levenshtein1(txt1,txt2)
    print(result2)
    WriteTxt(result1*0.5+result2*0.5,path3)
    print("OK")
except FileNotFoundError as e:
    print(e)





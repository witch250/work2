#import jieba
import jieba.analyse
import os
import math
import simhash
import Levenshtein
def OpenTxt(txtpath):
    try:
        with open(txtpath,"r",encoding='UTF-8') as txt:
            return(txt.read())
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
    for keyword,weight in taglist:
        weight*=20
        weight=math.ceil(weight)
        keyword=hash(keyword)
        temp=[]
        for i in keyword:
            if i=='1':
                temp.append(weight)
            else:
                temp.append(-weight)
    print(temp)

def Levenshtein1(txt1,txt2):
    return Levenshtein.ratio(jieba.analyse.extract_tags(txt1, topK=20),jieba.analyse.extract_tags(txt2, topK=20))

try:
    #获取路径，更改路径
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    #print(os.getcwd())
    path1='./orig_0.8_add.txt'
    path2='./orig_0.8_del.txt'
    txt1=OpenTxt(path1)
    txt2=OpenTxt(path2)
    SimHash1(txt1)
    SimHash1(txt2)
    result2=Levenshtein1(txt1,txt2)
    print(result2)
    print("OK")
except FileNotFoundError as e:
    print(e)





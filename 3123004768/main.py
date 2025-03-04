#import jieba
import jieba.analyse
import os
import math
def OpenTxt(txtpath):
    try:
        with open(txtpath,"r",encoding='UTF-8') as txt:
            return(txt.read())
    except FileNotFoundError:
        raise FileNotFoundError("找不到文件")

def hash(word):
    t=ord(word[0])
    t=bin(t)
    print(t)
    return t
    
    
def SimHash(txt):
    taglist=jieba.analyse.extract_tags(txt, topK=20, withWeight=True)
    for keyword,weight in taglist:
        weight*=10
        weight=math.ceil(weight)
        keyword=hash(keyword)


try:
    #获取路径，更改路径
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    #print(os.getcwd())
    path1='./orig_0.8_add.txt'
    path2='./orig_0.8_del.txt'
    txt1=OpenTxt(path1)
    txt2=OpenTxt(path2)
    SimHash(txt1)
    SimHash(txt2)
    print("OK")
except FileNotFoundError as e:
    print(e)





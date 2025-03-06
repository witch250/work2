#import jieba
import jieba.analyse
import os
import math
import Levenshtein
from line_profiler import profile #4.2.0 电脑重启再使用......
#coverage
#memory_profiler-0.61.0 psutil-7.0.0 contourpy-1.3.1 cycler-0.12.1 fonttools-4.56.0 kiwisolver-1.4.8 matplotlib-3.10.1 packaging-24.2 pillow-11.1.0 pyparsing-3.2.1 python-dateutil-2.9.0.post0 six-1.17.0
#cd
#py -m kernprof -l main.py   
#py -m line_profiler main.py.lprof
import numpy as np
import sys

def OpenTxt(txtpath):
    try:
        with open(txtpath,"r",encoding='UTF-8') as txt:
            return(txt.read())
    except FileNotFoundError:
        raise FileNotFoundError("找不到文件")
    except MemoryError:
        raise MemoryError("内存溢出")
    except PermissionError:
        raise PermissionError("不允许访问文件")

def WriteTxt(op,path):
    try:
        with open(path,'w',encoding='UTF-8') as f:
            f.write("相似度为%.2f"%op)
    except FileNotFoundError:
        raise FileNotFoundError("找不到文件")
    except PermissionError:
        raise PermissionError("不允许访问文件")

@profile
def Levenshtein1(txt1,txt2):
    try:
        s1=jieba.analyse.extract_tags(txt1, topK=30)
        s2=jieba.analyse.extract_tags(txt2, topK=30)
        #list仅位置不同时会得到完全不同，我猜可以这么改
        s1.sort()
        s2.sort()
        #print(s1)
        #print(s2)
        #比较list,返回小数
        return Levenshtein.ratio(s1,s2)*0.5+Levenshtein.ratio(jieba.analyse.extract_tags(txt1, topK=20),jieba.analyse.extract_tags(txt2, topK=20))*0.5
    except MemoryError:
        raise MemoryError("内存溢出")

#关键词交集中元素个数除以并集
@profile
def Jaccard(txt1,txt2):
    try:
        s1=jieba.analyse.extract_tags(txt1, topK=30)
        s2=jieba.analyse.extract_tags(txt2, topK=30)
        s1=set(s1)
        s2=set(s2)
        num1=len(s1&s2)
        num2=len(s1|s2)
        if num2==0:
            return 1
        return num1/num2
    except MemoryError:
        raise MemoryError("内存溢出")

#main
if __name__=='__main__':
    try:
        #获取路径，更改路径
        os.chdir(os.path.dirname(os.path.abspath(__file__)))
        #print(os.getcwd())
        path=sys.argv
        if len(path)>1: #调用cmd
            try:
                if path[1]=='' or path[2]=='' or path[3]=='':
                    pass
                else:
                    path1=path[1]
                    path2=path[2]
                    path3=path[3]
            except IndexError:
                raise IndexError("输入不存在")
        if len(path)==1: #脚本内参数
            path1='./orig.txt'
            path2='./orig_0.8_add.txt'
            path3='./output.txt'
        print(path1)
        txt1=OpenTxt(path1)
        txt2=OpenTxt(path2)
        result2=Levenshtein1(txt1,txt2)
        print(result2)
        result3=Jaccard(txt1,txt2)
        print(result3)
        WriteTxt(result1*0.4+result2*0.3+result3*0.3,path3)
        #print("OK")
    except FileNotFoundError as e:
        print(e)
    except IndexError as e:
        print(e)
    except MemoryError as e:
        print(e)
    except PermissionError as e:
        print(e)
        print("程序执行完毕")
        #os.system("pause")





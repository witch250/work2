#import jieba
import jieba.analyse
import os
import Levenshtein
from line_profiler import profile #4.2.0 电脑重启再使用......
#coverage   代码覆盖 py -m coverage run test.py py -m coverage report py -m coverage html -d covhtml
#memory_profiler-0.61.0 内存
#cd 打开文件夹
#py -m kernprof -l main.py   测试时间
#py -m line_profiler main.py.lprof  打开测试时间报告

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
    except OSError:
        raise OSError("请检查斜杠")

def WriteTxt(op,path):
    try:
        with open(path,'w',encoding='UTF-8') as f:
            f.write("相似度为%.2f"%op)
    except FileNotFoundError:
        raise FileNotFoundError("找不到文件")
    except PermissionError:
        raise PermissionError("不允许访问文件")
    except Exception:
        raise Exception("发生错误")

@profile
def Levenshtein1(txt1,txt2):
    if (txt1=='' and txt2!='') or (txt2=='' and txt1!=''):
        return 0
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
def Jaccard1(txt1,txt2):
    if (txt1=='' and txt2!='') or (txt2=='' and txt1!=''):
        return 0
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

def main():
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
        txt1=OpenTxt(path1)
        txt2=OpenTxt(path2)
        result2=Levenshtein1(txt1,txt2)
        #print(result2)
        result3=Jaccard1(txt1,txt2)
        #print(result3)
        WriteTxt(result2*0.5+result3*0.5,path3)
        #print("OK")
    except FileNotFoundError as e:
        print(e)
    except IndexError as e:
        print(e)
    except MemoryError as e:
        print(e)
    except PermissionError as e:
        print(e)
    except OSError as e:
        print(e)
        print("程序执行完毕")
    except Exception as e:
        print(e)
        #os.system("pause")

if __name__=='__main__':
    main()





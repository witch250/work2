import jieba

def OpenTxt(txtpath):
    try:
        with open(txtpath,"r",encoding='UTF-8') as txt:
            return(txt.read())
    except FileNotFoundError:
        raise FileNotFoundError("找不到文件")

def SimHash(txt):
    taglist=jieba.analyse.extract_tags(txt, topK=20, withWeight=True)
    for keyword,weight in taglist:
        pass



def main():
    try:
        path1=""
        path2=""
        txt1=OpenTxt(path1)
        txt2=OpenTxt(path2)
        SimHash(txt1)
        SimHash(txt2)

    except FileNotFoundError as e:
        print(e)


main()
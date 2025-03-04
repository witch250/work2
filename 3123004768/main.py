import jieba

def OpenTxt(txtpath):
    try:
        with open(txtpath,"r",encoding='UTF-8') as txt:
            return(txt.read())
    except FileNotFoundError:
        raise FileNotFoundError("找不到文件")


def main():
    try:
        path1=""
        path2=""
        txt1=OpenTxt(path1)
        txt2=OpenTxt(path2)
    except FileNotFoundError as e:
        print(e)


main()
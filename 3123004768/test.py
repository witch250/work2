from main import Levenshtein1
from main import Jaccard1
from main import OpenTxt
from main import WriteTxt
from main import main
def test():
    s1=""
    s2=""
    a1=Levenshtein1(s1,s2)+Jaccard1(s1,s2)
    print(a1/2)
    s1="asnjnah akfjafa a apple"
    s2="gjghjks hhijvhsch b a apple"
    a1=Levenshtein1(s1,s2)+Jaccard1(s1,s2)
    print(a1/2)
    s1=""
    s2="我是人"
    a1=Levenshtein1(s1,s2)+Jaccard1(s1,s2)
    print(a1/2)
    s1="我爱太阳"
    s2="他爱月亮"
    a1=Levenshtein1(s1,s2)+Jaccard1(s1,s2)
    print(a1/2)
    s1="2024年12月5日，据德国媒体报道，德国总统马卡龙批准了大臣巴尼耶的辞职请求。"
    s2="2024年12月5日，据法国媒体报道，法国总统马克龙批准了总理巴尼耶的辞职请求。"
    a1=Levenshtein1(s1,s2)+Jaccard1(s1,s2)
    print(a1/2)
    s1="截至2023年1月，法国总人口为6804万人。居民中64%信奉天主教，3%信奉伊斯兰教，3%信奉新教，1%信奉犹太教，28%自称无宗教信仰。法兰西民族是由多个民族混合构成的，除了主体法兰西人外，边境地区还有阿尔萨斯人、布列塔尼人、科西嘉人、佛拉芒人、巴斯克人等少数民族，大约占了总人口的7.9%。法国在欧盟各国人口数量排名第二，仅次于德国。巴黎大区是法国人口最多的地区，居民总数1221万人。法国国家经济统计局人口统计中心发布的报告显示，2020年，法国移民人口为680万，占总人口的10.2%，其中250万移民，即36%获得了法国国籍。在法国的外国人口达510万人，占总人口的7.6%。生活在法国的非洲移民占47.5%，欧洲移民占32.2%，一半的移民来自阿尔及利亚、摩洛哥、葡萄牙、突尼斯、意大利、土耳其和西班牙这七个国家。"
    s2="截至2023年1月，德国总人口为6804万人。居民中64%信奉东正教，3%信奉摩门教，3%信奉苯教，1%信奉犹太教，28%自称无宗教信仰。德意志民族是由多个民族混合构成的，除了主体德意志人外，边境地区还有波兰人、萨米人、塞浦路斯人、荷兰人、西班牙人等少数民族，大约占了总人口的2.9%。德国在北约各国人口数量排名第二，仅次于法国。柏林大区是德国人口最多的地区，居民总数1221万人。德国国家经济统计局人口统计中心发布的报告显示，2020年，德国移民人口为680万，占总人口的10.2%，其中250万移民，即36%获得了德国国籍。在德国的外国人口达510万人，占总人口的7.6%。生活在德国的美洲移民占47.5%，南极洲移民占32.2%，一半的移民来自南非、印度、葡萄、几内亚、圣马蒂诺、希腊和Spain这七个国家。"
    a1=Levenshtein1(s1,s2)+Jaccard1(s1,s2)
    print(a1/2)
    s1="截至2023年1月，法国总人口为6804万人。居民中64%信奉天主教，3%信奉伊斯兰教，3%信奉新教，1%信奉犹太教，28%自称无宗教信仰。法兰西民族是由多个民族混合构成的，除了主体法兰西人外，边境地区还有阿尔萨斯人、布列塔尼人、科西嘉人、佛拉芒人、巴斯克人等少数民族，大约占了总人口的7.9%。法国在欧盟各国人口数量排名第二，仅次于德国。巴黎大区是法国人口最多的地区，居民总数1221万人。法国国家经济统计局人口统计中心发布的报告显示，2020年，法国移民人口为680万，占总人口的10.2%，其中250万移民，即36%获得了法国国籍。在法国的外国人口达510万人，占总人口的7.6%。生活在法国的非洲移民占47.5%，欧洲移民占32.2%，一半的移民来自阿尔及利亚、摩洛哥、葡萄牙、突尼斯、意大利、土耳其和西班牙这七个国家。"
    s2="截至2023年1月，法国总人口为6804万人。居民中64%信奉天主教，3%信奉伊斯兰教，3%信奉新教，1%信奉犹太教，28%自称无宗教信仰。法兰西民族是由多个民族混合构成的，除了主体法兰西人外，边境地区还有阿尔萨斯人、布列塔尼人、科西嘉人、佛拉芒人、巴斯克人等少数民族，大约占了总人口的7.9%。法国在欧盟各国人口数量排名第二，仅次于德国。巴黎大区是法国人口最多的地区，居民总数1221万人。法国国家经济统计局人口统计中心发布的报告显示，2020年，法国移民人口为680万，占总人口的10.2%，其中250万移民，即36%获得了法国国籍。德国国家经济统计局人口统计中心发布的报告显示，2020年，德国移民人口为680万，占总人口的10.2%，其中250万移民，即36%获得了德国国籍。在德国的外国人口达510万人，占总人口的7.6%。生活在德国的美洲移民占47.5%，南极洲移民占32.2%，一半的移民来自南非、印度、葡萄、几内亚、圣马蒂诺、希腊和Spain这七个国家。"
    a1=Levenshtein1(s1,s2)+Jaccard1(s1,s2)
    print(a1/2)
    try:
        OpenTxt("c:")
    except PermissionError as e:
        print(e)
    finally:
        try:
            OpenTxt("c:\1.txt")
        except OSError as e:
            print(e)
        finally:
            try:
                OpenTxt("c:/1.txt")
            except FileNotFoundError as e:
                    print(e)              
    #memoryerror不测
    #write不测，怕把自己爆了
    #indexerror不测，不知道怎么测

if __name__=='__main__':
    test()
    main()

import jieba
import re
from collections import defaultdict
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
from wordcloud import WordCloud


def openfile():
    with open('dreamofredmaison.txt', encoding='utf-8') as fp:
        alltext = fp.read()
        # print(type(alltext))
    return alltext


def word_frequency():
    allstr = ''.join(re.findall('[\u4e00-\u9fa5]', openfile()))
    # print(str1)
    strlist = allstr.split("第八十回")
    text_list = jieba.cut(strlist[0])
    # print(text_list)
    # return text_list
    text_dict = defaultdict(int)
    for word in text_list:
        text_dict[word] += 1
    # print(text_dict)
    return text_dict


def common_word():
    all_word_dict = word_frequency()
    common_word_dict = dict()
    new_file1 = open('common_text.csv', 'w')
    new_file1.write('text,value\n')
    for key, value in all_word_dict.items():
        if value > 500:
            common_word_dict[key] = value
            new_file1.write(key)
            new_file1.write(',')
            new_file1.write(str(value))
            new_file1.write('\n')
    # print(common_word_dict)
    new_file1.close()
    # return common_word_dict


def viewable1():
    common_word()
    data = pd.read_csv('common_text.csv', encoding='gbk')
    xlist = list(data['text'])
    # xlist=list(data['text'])print(xlist)
    ylist = list(data['value'])
    
    # print(xlist)
    # print(data['text'])
    # print(type(data))
    # fig=plt.figure()
    # data['text'].plot(kind='bar',title='前80回词频统计')
    # plt.show()
    matplotlib.rc("font", family='YouYuan')
    plt.rcParams['figure.figsize'] = (24.0, 8.0)
    plt.bar(xlist, ylist)
    plt.title('前80回词频统计')
    plt.xlabel('text')
    plt.ylabel('value')

# def viewable2():
#     allstr = ''.join(re.findall('[\u4e00-\u9fa5]', openfile()))
#     # print(str1)
#     strlist = allstr.split("第八十回")
#     text_list = ' '.join(jieba.cut(strlist[0]))
#     wordcloud = WordCloud(font_path="simsun.ttf").generate(text_list)
#     plt.imshow(wordcloud, interpolation='bilinear')
#     plt.axis("off")



# alltext=openfile()
# word_frequency()
# common_word()
# viewable2()


import re

# 正则匹配字符串中的单词，略去空格
def GetWord(text):
    return re.compile(r'\w+').findall(text)  

# 创建字典统计各个单词出现的次数
def Num(wordlist, worddir):  
    #将字典中键值对对应值初始化
    for i in wordlist:
        worddic[i] = 0
    #统计各个单词出现的次数
    for i in wordlist:
        worddic[i] += 1
    return worddic

# 创建字典统计给定关键词列表中单词出现频率
def Frequency(frelist, worddir, fredic):
    #将字典中键值对对应值初始化
    for i in frelist:
        fredic[i] = 0
    #遍历给定列表
    for i in frelist:
        #遍历上题中创建的字典
        for j in worddic:
            if(i == j):
                fredic[i] = worddic[j]
                #将上题中统计的值赋给新字典的值
        

file1 = open(r'EngWords.txt')
text1 = file1.read()
print(text1)
wordlist = GetWord(text1)
# print(wordlist)
worddic = {}
# print(Num(wordlist,worddic))
Num(wordlist, worddic)
print(worddic)
file2 = open(r'frewords.txt')
text2 = file2.read()
frelist = GetWord(text2)
# print(frelist)
fredic = {}
Frequency(frelist, worddic, fredic)
print(fredic)
file1.close()
file2.close()

'''集合实现'''
file = open('words.txt')  # 打开所需读入的文件
new_file = open('rev.txt', 'w')  # 新建需要写入的文件
set1 = set()  # 新建空集合存放源字符串
set2 = set()  # 新建空集合存放反序串

for line in file:
    word = line.strip()
    wordrev = word[::-1]
    if word != wordrev:
        set1.add(word)  # 过滤掉回文字符串并逐个添加到集合

for i in set1:
    set2.add(i[::-1])  # 使用源字符串集合得到反序字符串集合

s = set1 & set2  # 取两集合的交集

s1 = list(s)  # 将集合转化为列表便于格式化输出

for i in s1:
    x = i[::-1]
    for j in s1:
        if(x == j):
            new_file.write('(%s, %s)\n' % (i, j))  # 搜索到反序对，输出到文件
            s1.remove(j)  # 从列表中移除反序串，防止二遍输出
file.close()
new_file.close()


'''列表实现'''

# import time

# f=open('words.txt') #打开所需读入的文件
# new_file = open('rev.txt', 'w') #新建需要写入的文件
# wordlist=[] #存放读取的字符串
# # start=time.time() #计算代码运行时长

# #切片操作获得反序字符串
# def rev(s):
#     return s[::-1]

# #查找现有列表是否已有反序对
# def search(s):
#     sr=rev(s)
#     for i in wordlist: #遍历已有的字符串列表
#         if(sr==i): #有与反序值相等的字符串则写入文件
#             new_file.write('(%s, %s)\n' % (i, sr))

# #for i in range(4):
# for line in f: #从文件对象中按行读入字符串，此种方法不带换行符
#     word=line.strip() #移除字符串头尾的空白字符（空格等）
#     search(word)
#     wordlist.append(word)#将字符串追加至列表末尾

# # print(time.time()-start)
# f.close()
# new_file.close()#关闭打开的文件

'''元组实现'''
# import time

# f=open('words.txt')
# wordlist=() #存放读取的字符串
# a=() #存放临时读取的字符串

# start=time.time()

# #字符串翻转函数（切片实现）
# def rev(s):
#     return s[::-1]

# #搜索反序对函数
# def search(s):
#     sr=rev(s)   #获得反序字符串
#     for i in wordlist: #遍历字符串列表
#         if(sr==i): #如果有与反序值相等的字符串，输出此反序对
#             print('<'+i+','+s+'>')
#             break

# #for i in range(4):
# for line in f:
# #    line=f.readline()
#     word=line.strip() #去掉移除字符串头尾的空白字符
#     search(word) #查找现有元组是否已有反序对
#     a=(word,)
#     wordlist=wordlist+a

# print(time.time()-start)
# #print(wordlist)
# f.close()

'''字典实现'''
# import time

# f=open('words.txt')
# wordlist=dict() #存放读取的字符串
# revlist=dict() #存放反序字符串


# start=time.time()

# #字符串翻转函数（切片实现）
# def rev(s):
#     return s[::-1]

# for line in f:
# #    line=f.readline()
#     word=line.strip() #去掉移除字符串头尾的空白字符
#     if word!=rev(word):
#         wordlist[word]=7 #单词放在键中，值赋任意值皆可
#         revlist[rev(word)]=7

# rel=wordlist.keys()&revlist.keys() #对字典进行集合操作，获得交集


# for i in rel:
#     x=i[::-1]
#     for j in rel:
#         if(x==j):
#             print('(%s, %s)\n' % (i, j))
#             rel.remove(j)
# #print(len(rel))
# print(time.time()-start)

# f.close()


'''最初使用的列表方法'''
# import time
# import os


# def reverseStr(string):
#     t = list(string)
#     l = len(t)-1
#     for i, j in zip(range(l-1, 0, -1), range(l//2)):
#         t[i], t[j] = t[j], t[i]
#     return "".join(t)


# file = open(r'words.txt')
# path = os.getcwd()
# new_file = open('ReverseGroup.txt', 'w')
# wordlist = list(file)
# start = time.time()

# for i in wordlist:

#     s = reverseStr(i)
#     # print(list(s))
#     # s=list(i)
#     # s = i[::-1]#不能用此种方法由于终止符号会一并进行反转
#     for j in wordlist:
#         if(s == j):
#             new_file.write('%s and %s' % (i, j))
#             del j
# file.close()
# new_file.close()
# print(time.time()-start)

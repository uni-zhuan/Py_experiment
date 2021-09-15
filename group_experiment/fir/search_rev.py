import time

f=open('words.txt') #打开所需读入的文件
new_file = open('rev.txt', 'w') #新建需要写入的文件
wordlist=[] #存放读取的字符串
# start=time.time() #计算代码运行时长

#切片操作获得反序字符串
def rev(s):
    return s[::-1]

#查找现有列表是否已有反序对
def search(s):
    sr=rev(s)
    for i in wordlist: #遍历已有的字符串列表
        if(sr==i): #有与反序值相等的字符串则写入文件
            new_file.write('(%s, %s)\n' % (i, sr))

#for i in range(4):
for line in f: #从文件对象中按行读入字符串，此种方法不带换行符
    word=line.strip() #移除字符串头尾的空白字符（空格等）
    search(word) 
    wordlist.append(word)#将字符串追加至列表末尾
    
# print(time.time()-start)
f.close()
new_file.close()#关闭打开的文件
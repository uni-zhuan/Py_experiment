import time

f=open('words.txt') #�����������ļ�
new_file = open('rev.txt', 'w') #�½���Ҫд����ļ�
wordlist=[] #��Ŷ�ȡ���ַ���
# start=time.time() #�����������ʱ��

#��Ƭ������÷����ַ���
def rev(s):
    return s[::-1]

#���������б��Ƿ����з����
def search(s):
    sr=rev(s)
    for i in wordlist: #�������е��ַ����б�
        if(sr==i): #���뷴��ֵ��ȵ��ַ�����д���ļ�
            new_file.write('(%s, %s)\n' % (i, sr))

#for i in range(4):
for line in f: #���ļ������а��ж����ַ��������ַ����������з�
    word=line.strip() #�Ƴ��ַ���ͷβ�Ŀհ��ַ����ո�ȣ�
    search(word) 
    wordlist.append(word)#���ַ���׷�����б�ĩβ
    
# print(time.time()-start)
f.close()
new_file.close()#�رմ򿪵��ļ�
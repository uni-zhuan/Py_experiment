from bisect import bisect_left


def make_word_list():
    """从文件中读入单词列表"""
    word_list = list()
    with open('words.txt') as fp:
        word_list = [x.strip()
                     for x in fp if 'a' in x or 'i' in x]  # 不含'a'和'i'的一定不是可缩减单词
    fp.close()
    return word_list


def in_bisect(word_list, word):
    """二分法进行列表查找"""
    i = bisect_left(word_list, word)
    if i != len(word_list) and word_list[i] == word:
        return True
    else:
        return False

def bisect(word_list, word):
    """二分法进行列表查找"""
    i = bisect_left(word_list, word)
    if i != len(word_list) and word_list[i] == word:
        return i
    else:
        return -1

def setex(word_list, word):
    """#新建空集合存放源字符串"""
    set1 = set(word_list)
    if word in set1:
        return True
    else:
        return False


def getlongest(word_list):
    """得到列表中最长单词"""
    max = 0
    for i in word_list:
        if len(i) > max:
            max = len(i)
    return max


def getdir1(word_list, dec_dir, max):
    """根据字符串长度组建{长度：对应长度单词列表}的所有单词键值对"""
    dec_dir[1] = ['a', 'i']
    for i in range(2, max+1):
        dec_dir[i] = []
    for i in word_list:
        dec_dir[len(i)].append(i)


def getdir2(dec_dir, new_dir, max):
    """根据字符串长度组建{长度：对应长度单词列表}的可缩减单词键值对"""
    new_dir[1] = ['a', 'i']  # 由于使用二分法，列表中单词必须有序
    num = 0
    for i in range(2, max+1):
        new_dir[i] = []
    for i in range(2, max+1):
        count = 0
        for j in dec_dir[i]:
            for k in range(0, len(j)):
                if in_bisect(new_dir[i-1], decrease(j, k)):
                    # 使用二分法查找长度为i的单词缩减后的单词是否在长度为i-1的列表中
                    new_dir[i].append(j)
                    num = num+1
                    count += 1
        if(count == 0):
            # 令循环终止，减少后续不必要操作
            return(num, i-1)  # 返回最长单词和其长度的元组


def decrease(word, i):
    """对传入的参数单词去掉i位置上的字母"""
    newword = ''
    for j in range(0, i):
        newword += word[j]
    for j in range(i+1, len(word)):
        newword += word[j]
    return newword

def process(word,new_dir,length):
    """使用递归方式还原缩减过程"""
    if(length==1):
        print(word)
        return 
    for i in range(0, len(word)):
        tf=bisect(new_dir[i-1], decrease(word, i))
        if tf>-1:
            print(word)
            print("->")
            process(new_dir[i-1][tf],new_dir,length)


if __name__ == '__main__':
    new_file = open('rev.txt', 'w')
    dec_dir = dict()
    new_dir = dict()

    word_list = make_word_list()
    max = getlongest(word_list)
    getdir1(word_list, dec_dir, max)
    numcount = getdir2(dec_dir, new_dir, max)
    print(numcount)
    # print(new_dir[11][0])

    process(new_dir[11][0],new_dir,11)

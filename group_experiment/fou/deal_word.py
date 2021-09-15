import re


def rotateword(strsrc, n):
    strlist = list(strsrc)
    for i in range(len(strlist)):
        strlist[i] = turn(strlist[i], n)
    return ''.join(strlist)


def turn(i, n):
    num = ord(i)
    if num <= 90 and num >= 65:
        return chr((num-65+n) % 26+65)
    elif num <= 122 and num >= 97:
        return chr((num-97+n) % 26+97)


def avoids(word, avoidstr):
    avoid = '|'.join(avoidstr)
    stra = avoid
    pat = re.compile(stra)
    return re.search(pat, word)


def useonly(word, acceptstr):
    stra = '[^'+acceptstr+']'
    print(stra)
    pat = re.compile(stra)
    return re.search(pat, word)


def useall(word, needstr):
    for i in needstr:
        pat = i
        re.compile(pat)
        if not re.search(pat, word):
            # print(i)
            return False
    else:
        return True


def deal_file1():
    with open('words.txt')as fp:
        word_list = [x.strip() for x in fp]
    fp.close()
    for i in word_list:
        if useall(i, 'aeiou'):
            print(i)


def hasnoe(word):
    return re.search('e', word)


def deal_file2():
    with open('words.txt')as fp:
        word_list = [x.strip() for x in fp]
    fp.close()
    num = 0
    for i in word_list:
        if hasnoe(i):
            num += 1
    return num/len(word_list)
# strsrc='wjw'
# str1=rotateword(strsrc,5)
# print(str1)

# print(avoids('vrnvu','racb'))

# print(useonly('vrnvu','vrnuabc'))

# print(useall('abcd','sb'))
# deal_file1()

# print(hasnoe('vidonv'))
# print(deal_file2())
